"""Check the published search and discovery contract without network requests."""
import json
from collections import Counter, deque
from datetime import date
from urllib.parse import unquote, urljoin, urlparse
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup
import seo


def audit():
    failures = []
    documents = {}
    titles, descriptions, indexable = [], [], set()
    links = {}
    learning_resources = 0

    def check(ok, message):
        if not ok:
            failures.append(message)

    def local(url):
        parsed = urlparse(url)
        if parsed.netloc != urlparse(seo.ORIGIN).netloc:
            return None
        return unquote(parsed.path.lstrip('/')) or 'index.html'

    for path in seo.published_pages():
        relative = path.relative_to(seo.ROOT).as_posix()
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        documents[relative] = soup
        expected = seo.canonical(relative)
        for selector in ['title', 'meta[name="description"]', 'meta[name="robots"]',
                         'link[rel="canonical"]', 'script[type="application/ld+json"]']:
            check(len(soup.select(selector)) == 1, f'{relative}: expected exactly one {selector}')
        try:
            title = soup.title.get_text()
            description = soup.select_one('meta[name="description"]')['content']
            check(soup.select_one('link[rel="canonical"]')['href'] == expected,
                  f'{relative}: incorrect canonical address')
            robots = soup.select_one('meta[name="robots"]')['content']
            check(('noindex' in robots) == (relative in seo.NOINDEX), f'{relative}: incorrect indexing policy')
            if relative not in seo.NOINDEX:
                indexable.add(relative)
                titles.append(title)
                descriptions.append(description)
            check(len(description) >= 60, f'{relative}: uninformative description')
            for prefix, attribute in [('og', 'property'), ('twitter', 'name')]:
                for field, value in [('title', title), ('description', description)]:
                    node = soup.select_one(f'meta[{attribute}="{prefix}:{field}"]')
                    check(node is not None and node.get('content') == value,
                          f'{relative}: inconsistent {prefix} {field}')
            check(soup.select_one('meta[property="og:url"]')['content'] == expected,
                  f'{relative}: inconsistent sharing address')
            picture = soup.select_one('meta[property="og:image"]')['content']
            image_path = seo.ROOT / local(picture)
            with seo.Image.open(image_path) as image:
                dimensions = image.size
            for field, dimension in zip(['width', 'height'], dimensions):
                check(int(soup.select_one(f'meta[property="og:image:{field}"]')['content']) == dimension,
                      f'{relative}: incorrect sharing image {field}')
            graph = json.loads(soup.select_one('script[type="application/ld+json"]').string)
            check(graph['@context'] == 'https://schema.org', f'{relative}: incorrect schema context')
            entities = graph['@graph']
            identities = [node['@id'] for node in entities]
            check(len(identities) == len(set(identities)), f'{relative}: duplicate schema identity')
            for node in entities:
                check(node['@type'] not in {'Course', 'Review', 'AggregateRating', 'SearchAction'},
                      f'{relative}: unsupported search claim')
                if node['@type'] == 'LearningResource':
                    learning_resources += 1
                    check(bool(node.get('teaches')) and node.get('isAccessibleForFree') is True,
                          f'{relative}: incomplete learning resource')
                    for pdf in node.get('encoding', []):
                        check((seo.ROOT / local(pdf['contentUrl'])).is_file(), f'{relative}: missing schema PDF')
                    for lesson in node.get('hasPart', []):
                        check(soup.find(id=urlparse(lesson['url']).fragment) is not None,
                              f'{relative}: missing schema lesson anchor')
            crumbs = next((n for n in entities if n['@type'] == 'BreadcrumbList'), None)
            if relative not in {'index.html', *seo.NOINDEX}:
                visible = soup.select('[data-seo-breadcrumbs] li')
                expected_crumbs = crumbs['itemListElement'] if crumbs else []
                check(len(visible) == len(expected_crumbs) and len(visible) >= 2,
                      f'{relative}: missing breadcrumbs')
                for item, entry in zip(visible, expected_crumbs):
                    check(item.get_text(' ', strip=True) == entry['name'], f'{relative}: misleading breadcrumb label')
                    href = urljoin(expected, item.a['href']) if item.a else expected
                    # Homepage links may use index.html locally; their canonical form is /.
                    if href == seo.ORIGIN + 'index.html':
                        href = seo.ORIGIN
                    check(href == entry['item'], f'{relative}: inconsistent breadcrumb destination')
            for section in soup.select('.finished-prompts, .finished-dialogue-library, [data-ai-workshop]'):
                check(section.has_attr('data-nosnippet'), f'{relative}: AI instructions may enter search snippets')
        except (AttributeError, KeyError, TypeError, ValueError, OSError) as error:
            failures.append(f'{relative}: {error}')
        links[relative] = {destination for a in soup.select('a[href]')
                           if (destination := local(urljoin(expected, a['href']))) is not None}

    for label, values in [('title', titles), ('description', descriptions)]:
        for value, count in Counter(values).items():
            check(count == 1, f'Duplicate {label} on {count} indexed pages: {value}')

    queue, reached = deque(['index.html']), set()
    while queue:
        page = queue.popleft()
        if page in reached:
            continue
        reached.add(page)
        queue.extend(destination for destination in links.get(page, set()) if destination in documents)
    check(indexable <= reached, 'Pages unreachable from the homepage: ' + ', '.join(sorted(indexable - reached)))

    namespace = {'s': seo.SITEMAP_NS}
    root = ET.parse(seo.ROOT / 'sitemap.xml').getroot()
    check(root.tag == '{' + seo.SITEMAP_NS + '}sitemapindex', 'Expected a sitemap index')
    entries, map_counts = [], {}
    for child in root.findall('s:sitemap/s:loc', namespace):
        name = local(child.text)
        child_root = ET.parse(seo.ROOT / name).getroot()
        urls = child_root.findall('s:url', namespace)
        map_counts[name] = len(urls)
        for entry in urls:
            url = entry.find('s:loc', namespace).text
            relative = local(url)
            entries.append(relative)
            check(relative is not None and url == seo.canonical(relative), f'Noncanonical sitemap URL: {url}')
            check((seo.ROOT / relative).is_file(), f'Missing sitemap destination: {url}')
            modified = entry.find('s:lastmod', namespace).text
            try:
                check(date.fromisoformat(modified) <= date.today(), f'Future sitemap date: {url}')
            except (TypeError, ValueError):
                failures.append(f'Invalid sitemap date: {url}: {modified}')
    expected_pdfs = set(seo.read_json('content/work/documents.json')['documents'])
    expected_pdfs.update(('pdf/students/' if i == 0 else 'pdf/teachers/') + pdf for c in seo.grammar().values() for i, pdf in enumerate(c['pdfs']))
    check(len(entries) == len(set(entries)), 'Duplicate sitemap entries')
    check(set(entries) == indexable | expected_pdfs, 'Sitemaps do not match the full indexed page and PDF inventory')
    manifest = seo.read_json('content/seo-index.json')['resources']
    check(set(manifest) == set(entries), 'Sitemap change history does not match the sitemap inventory')
    check('Sitemap: ' + seo.ORIGIN + 'sitemap.xml' in (seo.ROOT / 'robots.txt').read_text(), 'Missing robots sitemap declaration')
    for category in seo.CATEGORIES:
        soup = documents[seo.category_url(category)]
        expected_courses = {f'efsp-{t["slug"]}.html' for t in seo.tracks().values() if t['category'] == category}
        actual_courses = {local(urljoin(seo.canonical(seo.category_url(category)), a['href']))
                          for a in soup.select('.work-course-card')}
        check(actual_courses == expected_courses, f'{category}: incorrect course grouping')
    if failures:
        raise AssertionError('\n'.join(failures[:80]))
    summary = dict(pages=len(documents), indexable_pages=len(indexable), learning_resources=learning_resources,
                   unique_titles=len(set(titles)), unique_descriptions=len(set(descriptions)),
                   reachable_indexable_pages=len(indexable & reached), pdfs=len(expected_pdfs), sitemaps=map_counts)
    print(json.dumps(summary, indent=2))
    return summary


if __name__ == '__main__':
    audit()
