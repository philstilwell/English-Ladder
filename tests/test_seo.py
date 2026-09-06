import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import seo

ROOT=Path(__file__).resolve().parents[1]

class CurriculumSearchTests(unittest.TestCase):
    def page(self,relative):
        return BeautifulSoup((ROOT/relative).read_text(),'html.parser')

    def enhance(self,relative):
        s=self.page(relative)
        seo.enhance_page(s,ROOT/relative,'../'*len(Path(relative).parent.parts))
        return s

    def prepare_root(self,root,pdfs=None):
        (root/'content/work').mkdir(parents=True)
        (root/'content/grammar-curriculum.json').write_text('{"concepts":[]}')
        (root/'content/work/documents.json').write_text(json.dumps({'revision':'2026-09-05','documents':pdfs or {}}))

    def publish(self,root,day):
        with patch.object(seo,'ROOT',root):return seo.write_sitemaps(today=day)

    def test_levels_have_distinct_titles_descriptions_and_canonicals(self):
        titles=set();descriptions=set()
        for level in seo.LEVELS:
            relative=f'news/2026-09-06/{level}.html';s=self.enhance(relative)
            title=s.title.get_text();description=s.select_one('meta[name=description]')['content']
            self.assertIn(level.title()+' English',title)
            self.assertIn('2026-09-06',description)
            self.assertEqual(seo.ORIGIN+relative,s.select_one('link[rel=canonical]')['href'])
            titles.add(title);descriptions.add(description)
        self.assertEqual(3,len(titles));self.assertEqual(3,len(descriptions))

    def test_work_description_identifies_actual_material(self):
        p=seo.profile(ROOT/'efsp-manufacturing.html',self.page('efsp-manufacturing.html'))
        self.assertIn('production meetings',p['description'])
        self.assertNotEqual('English for Work · Industry & infrastructure',p['description'])

    def test_published_daily_feeds_and_search_data_include_fourteen_lessons(self):
        archives=sorted((ROOT/'archive/lessons').glob('*.json'),reverse=True)
        self.assertGreater(len(archives),14)
        expected=[p.stem for p in archives[:14]]
        for level in seo.LEVELS:
            with self.subTest(level=level):
                s=self.page(f'{level}.html')
                self.assertEqual(expected,[lesson['data-lesson-key'] for lesson in s.select('#lesson-container details.daily-lesson')])
                self.assertIn('latest 14 news lessons',s.select_one('.index-container > p').get_text())
                self.assertIn('latest 14 news lessons',s.select_one('meta[name=description]')['content'])
                graph=json.loads(s.select_one('[data-seo-schema]').string)['@graph']
                listing=next(n for n in graph if n['@type']=='ItemList')
                self.assertEqual(14,listing['numberOfItems'])
                self.assertEqual([seo.ORIGIN+f'news/{day}/{level}.html' for day in expected],[item['url'] for item in listing['itemListElement']])
                self.assertTrue((ROOT/f'news/{archives[14].stem}/{level}.html').is_file())

    def test_grammar_breadcrumbs_match_schema_and_related_patterns(self):
        s=self.enhance('grammar-concepts/concept-35.html')
        graph=json.loads(s.select_one('[data-seo-schema]').string)['@graph']
        crumbs=next(n for n in graph if n['@type']=='BreadcrumbList')
        self.assertEqual([n.get_text(' ',strip=True) for n in s.select('[data-seo-breadcrumbs] li')],[n['name'] for n in crumbs['itemListElement']])
        self.assertTrue(any(a['href'].endswith('concept-14.html') for a in s.select('[data-seo-related] a')))
        lesson=next(n for n in graph if n['@type']=='LearningResource')
        self.assertEqual('B1–B2',lesson['educationalLevel'])
        self.assertEqual(2,len(lesson['encoding']))
        self.assertTrue(all(p['encodingFormat']=='application/pdf' for p in lesson['encoding']))

    def test_repeat_enhancement_does_not_duplicate_or_hide_teaching_text(self):
        relative='grammar-concepts/concept-35.html';s=self.enhance(relative);before=str(s)
        seo.enhance_page(s,ROOT/relative,'../')
        self.assertEqual(before,str(s))
        self.assertEqual(1,len(s.select('[data-seo-breadcrumbs]')))
        self.assertEqual(1,len(s.select('[data-seo-related]')))
        self.assertIsNotNone(s.select_one('.ai-extension-body[data-nosnippet]'))
        self.assertIsNone(s.select_one('.concept-explanation[data-nosnippet]'))

    def test_structured_text_cannot_escape_its_script(self):
        s=self.page('about.html');text='A </script><script>alert("x")</script> example & explanation'
        seo.write_schema(s,{'@context':'https://schema.org','@graph':[{'name':text}]})
        parsed=BeautifulSoup(str(s),'html.parser')
        self.assertEqual(text,json.loads(parsed.select_one('[data-seo-schema]').string)['@graph'][0]['name'])
        self.assertFalse(any(t.string=='alert("x")' for t in parsed.select('script')))

    def test_root_and_unindexed_pages_have_explicit_policy(self):
        s=self.enhance('index.html')
        self.assertEqual(seo.ORIGIN,s.select_one('link[rel=canonical]')['href'])
        self.assertNotIn('noindex',s.select_one('meta[name=robots]')['content'])
        for relative in ['continue.html','404.html']:
            self.assertIn('noindex',self.enhance(relative).select_one('meta[name=robots]')['content'])

    def test_news_preview_uses_the_same_visible_saved_image(self):
        s=self.enhance('news/2026-09-06/beginner.html');image=s.select_one('.lesson-cover img')
        self.assertEqual(seo.ORIGIN.rstrip('/')+image['src'],s.select_one('meta[property="og:image"]')['content'])
        self.assertIn('not a photograph',s.select_one('.lesson-cover figcaption').get_text())
        self.assertEqual('summary_large_image',s.select_one('meta[name="twitter:card"]')['content'])

    def test_story_preview_preserves_credit_and_license(self):
        s=self.enhance('stories/food-market/beginner.html')
        self.assertEqual('/assets/editorial/food-market.webp',s.select_one('.lesson-cover img')['src'])
        self.assertIn('DZHA',s.select_one('.lesson-cover figcaption').get_text())
        self.assertIsNotNone(s.select_one('.lesson-cover a[href="https://unsplash.com/license"]'))

    def test_sitemap_dates_only_advance_for_changed_content(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);self.prepare_root(root)
            for name in ['about.html','404.html','continue.html']:(root/name).write_text(str(self.enhance(name)))
            self.publish(root,'2026-09-06');before=json.loads((root/'content/seo-index.json').read_text())
            self.publish(root,'2026-09-07');self.assertEqual(before,json.loads((root/'content/seo-index.json').read_text()))
            p=root/'about.html';s=BeautifulSoup(p.read_text(),'html.parser');tag=s.new_tag('p');tag.string='A new explanation of lesson review.';s.main.append(tag);p.write_text(str(s))
            self.publish(root,'2026-09-08');state=json.loads((root/'content/seo-index.json').read_text())['resources']
            self.assertEqual('2026-09-08',state['about.html']['lastmod'])
            self.assertNotIn('404.html',state);self.assertNotIn('continue.html',state)

    def test_relative_age_does_not_make_a_lesson_new(self):
        s=self.enhance('beginner.html');before=seo.fingerprint(s)
        s.select_one('.lesson-age').string='[15 days, 3 hours old]';self.assertEqual(before,seo.fingerprint(s))
        s.select_one('.lesson-title-text').string='A revised headline';self.assertNotEqual(before,seo.fingerprint(s))

    def test_pdf_dates_preserve_known_edition_and_track_byte_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);self.prepare_root(root,{'guide.pdf':{}})
            (root/'guide.pdf').write_bytes(b'%PDF-public guide');(root/'about.html').write_text(str(self.enhance('about.html')))
            self.publish(root,'2026-09-06');state=json.loads((root/'content/seo-index.json').read_text())['resources']
            self.assertEqual('2026-09-05',state['guide.pdf']['lastmod'])
            (root/'guide.pdf').write_bytes(b'%PDF-revised public guide');self.publish(root,'2026-09-07')
            self.assertEqual('2026-09-07',json.loads((root/'content/seo-index.json').read_text())['resources']['guide.pdf']['lastmod'])

    def test_future_releases_can_share_a_headline_without_duplicate_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'archive/lessons').mkdir(parents=True)
            data=json.loads((ROOT/'archive/lessons/2026-09-06.json').read_text())
            data['levels']['beginner']['lesson']['title']='A new community garden'
            s=self.page('news/2026-09-06/beginner.html');s.h1.string='A new community garden'
            results=[]
            for day in ['2030-01-02','2030-01-03']:
                data['release_date']=day;(root/f'archive/lessons/{day}.json').write_text(json.dumps(data))
                with patch.object(seo,'ROOT',root):results.append(seo.profile(root/f'news/{day}/beginner.html',s))
            self.assertNotEqual(results[0]['title'],results[1]['title'])
            self.assertIn('A new community garden',results[0]['description'])

if __name__=='__main__':unittest.main()
