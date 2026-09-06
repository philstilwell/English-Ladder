import copy
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
import seo

ROOT=Path(__file__).resolve().parents[1]


class SearchPublishingTests(unittest.TestCase):
    def page(self, relative):
        return BeautifulSoup((ROOT/relative).read_text(),'html.parser')

    def enhance(self, relative):
        soup=self.page(relative)
        seo.enhance_page(soup,ROOT/relative,'../'*len(Path(relative).parent.parts))
        return soup

    def test_reading_levels_have_distinct_titles_descriptions_and_canonicals(self):
        titles=set();descriptions=set()
        for level in seo.LEVELS:
            relative=f'news/2026-09-06/{level}.html'
            info=seo.metadata(self.page(relative),relative)
            self.assertIn(level.title()+' English',info['title'])
            self.assertIn('2026-09-06',info['description'])
            self.assertEqual(seo.ORIGIN+relative,info['canonical'])
            self.assertEqual('2026-09-06',info['published'])
            titles.add(info['title']);descriptions.add(info['description'])
        self.assertEqual(3,len(titles));self.assertEqual(3,len(descriptions))

    def test_work_description_uses_field_material_instead_of_category_kicker(self):
        relative='efsp-manufacturing.html'
        info=seo.metadata(self.page(relative),relative)
        self.assertIn('Manufacturing English',info['description'])
        self.assertNotEqual('English for Work · Industry & infrastructure',info['description'])

    def test_breadcrumb_schema_matches_visible_navigation_and_related_lessons(self):
        s=self.enhance('grammar-concepts/concept-35.html')
        data=json.loads(s.select_one('[data-seo-schema]').string)
        breadcrumb=next(n for n in data['@graph'] if n['@type']=='BreadcrumbList')
        self.assertEqual([n.get_text(' ',strip=True) for n in s.select('[data-seo-breadcrumb] li')],
                         [n['name'] for n in breadcrumb['itemListElement']])
        self.assertIsNotNone(s.select_one('[data-seo-related]').find('a',href='/grammar-concepts/concept-14.html'))
        lesson=next(n for n in data['@graph'] if n['@type']=='LearningResource')
        self.assertEqual('B1–B2',lesson['educationalLevel'])
        self.assertEqual(2,len(lesson['hasPart']))
        self.assertTrue(all(p['encodingFormat']=='application/pdf' for p in lesson['hasPart']))
        self.assertNotIn('Course',{n['@type'] for n in data['@graph']})

    def test_rebuilding_replaces_search_elements_without_duplicating_them(self):
        relative='grammar-concepts/concept-35.html';s=self.enhance(relative)
        before=str(s)
        seo.enhance_page(s,ROOT/relative,'../')
        self.assertEqual(before,str(s))
        self.assertEqual(1,len(s.select('[data-seo-breadcrumb]')))
        self.assertEqual(1,len(s.select('[data-seo-related]')))
        self.assertIsNone(s.select_one('[data-seo-nosnippet]'))
        self.assertIsNotNone(s.select_one('.ai-extension-body[data-nosnippet]'))
        self.assertIsNone(s.select_one('.concept-explanation[data-nosnippet]'))

    def test_structured_data_cannot_close_its_script_element(self):
        s=self.page('about.html')
        text='A </script><script>alert("x")</script> example & explanation'
        seo.write_schema(s,{'@context':'https://schema.org','@graph':[{'name':text}]})
        roundtrip=BeautifulSoup(str(s),'html.parser')
        self.assertEqual(text,json.loads(roundtrip.select_one('[data-seo-schema]').string)['@graph'][0]['name'])
        self.assertFalse(any(t.string=='alert("x")' for t in roundtrip.select('script')))

    def test_home_and_unindexed_pages_have_explicit_canonical_policy(self):
        home=self.enhance('index.html')
        self.assertEqual(seo.ORIGIN,home.select_one('link[rel=canonical]')['href'])
        for name in ['continue.html','404.html']:
            s=self.enhance(name)
            self.assertIn('noindex',s.select_one('meta[name=robots]')['content'])
        self.assertNotIn('noindex',home.select_one('meta[name=robots]')['content'])

    def test_news_preview_uses_its_saved_image_and_visible_caption(self):
        s=self.enhance('news/2026-09-06/beginner.html')
        image=s.select_one('.lesson-cover img')
        self.assertIsNotNone(image)
        self.assertEqual(seo.ORIGIN.rstrip('/')+image['src'],s.select_one('meta[property="og:image"]')['content'])
        self.assertIn('not a photograph',s.select_one('.lesson-cover figcaption').get_text())
        self.assertEqual('summary_large_image',s.select_one('meta[name="twitter:card"]')['content'])

    def test_evergreen_preview_preserves_existing_photo_credit_and_license(self):
        s=self.enhance('stories/food-market/beginner.html')
        self.assertEqual('/assets/editorial/food-market.webp',s.select_one('.lesson-cover img')['src'])
        self.assertIn('DZHA',s.select_one('.lesson-cover figcaption').get_text())
        self.assertIsNotNone(s.select_one('.lesson-cover a[href="https://unsplash.com/license"]'))

    def test_sitemap_uses_content_dates_and_excludes_private_or_error_pages(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for name in ['about.html','continue.html','404.html']:
                (root/name).write_text(str(self.enhance(name)))
            self.assertEqual(1,seo.publish_search_assets(root,today='2026-09-06'))
            original=json.loads((root/seo.STATE_PATH).read_text())
            seo.publish_search_assets(root,today='2026-09-07')
            self.assertEqual(original,json.loads((root/seo.STATE_PATH).read_text()))
            p=root/'about.html';s=BeautifulSoup(p.read_text(),'html.parser')
            paragraph=s.new_tag('p');paragraph.string='A substantive new explanation of how lessons are reviewed.';s.main.append(paragraph);p.write_text(str(s))
            seo.publish_search_assets(root,today='2026-09-08')
            self.assertEqual('2026-09-08',json.loads((root/seo.STATE_PATH).read_text())['pages']['about.html']['modified'])
            xml=ET.parse(root/'sitemap.xml')
            self.assertEqual([seo.url('about.html')],[n.text for n in xml.findall(f'{{{seo.NS}}}url/{{{seo.NS}}}loc')])

    def test_relative_age_alone_does_not_advance_modification_date(self):
        s=self.enhance('beginner.html');before=seo.fingerprint(s)
        s.select_one('.lesson-age').string='[15 days, 3 hours old]'
        self.assertEqual(before,seo.fingerprint(s))
        s.select_one('.lesson-title-text').string='A revised lesson headline'
        self.assertNotEqual(before,seo.fingerprint(s))

    def test_pdf_first_seen_has_no_invented_date_and_later_changes_are_tracked(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);s=self.enhance('about.html')
            a=s.new_tag('a',href='guide.pdf');a.string='Study guide';s.main.append(a)
            (root/'about.html').write_text(str(s));(root/'guide.pdf').write_bytes(b'%PDF-public guide')
            seo.publish_search_assets(root,today='2026-09-06')
            state=json.loads((root/seo.STATE_PATH).read_text())['pages']
            self.assertIsNone(state['guide.pdf']['modified'])
            (root/'guide.pdf').write_bytes(b'%PDF-revised public guide')
            seo.publish_search_assets(root,today='2026-09-07')
            self.assertEqual('2026-09-07',json.loads((root/seo.STATE_PATH).read_text())['pages']['guide.pdf']['modified'])

    def test_future_news_automatically_receives_level_schema_and_source_context(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'archive/lessons').mkdir(parents=True)
            data=json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())
            data['release_date']='2030-01-02'
            data['levels']['beginner']['lesson']['title']='A new community garden'
            data['levels']['beginner']['lesson']['overview']='Neighbors share a place to grow food.'
            (root/'archive/lessons/2030-01-02.json').write_text(json.dumps(data))
            s=self.page('news/2026-09-06/beginner.html');s.h1.string='A new community garden'
            info=seo.metadata(s,'news/2030-01-02/beginner.html',root)
            self.assertIn('A new community garden',info['title'])
            self.assertIn('A new community garden',info['description'])
            self.assertEqual('2030-01-02',info['published'])
            data['release_date']='2030-01-03'
            (root/'archive/lessons/2030-01-03.json').write_text(json.dumps(data))
            later=seo.metadata(s,'news/2030-01-03/beginner.html',root)
            self.assertNotEqual(info['title'],later['title'])
            self.assertNotEqual(info['canonical'],later['canonical'])


if __name__=='__main__':unittest.main()
