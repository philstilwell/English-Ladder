"""Directory artwork keeps a fixed, complete 6-by-11 layout."""
import unittest

from bs4 import BeautifulSoup
from PIL import Image

from work_curriculum import ROOT
from work_icons import (
    DIRECTORY_COLLAGE_CROPS, DIRECTORY_COLLAGE_SIZE, ICON_SLUGS,
    directory_collage,
)


class DirectoryCollageTests(unittest.TestCase):
    def test_every_field_appears_once_in_the_published_grid(self):
        generated = BeautifulSoup(directory_collage(), 'html.parser')
        published = BeautifulSoup((ROOT / 'efsp.html').read_text(), 'html.parser')
        for page in (generated, published):
            collage = page.select_one('.work-directory-collage')
            self.assertEqual(collage['role'], 'img')
            self.assertIn('66', collage['aria-label'])
            cells = collage.select('.work-collage-cell')
            self.assertEqual([cell['data-collage-field'] for cell in cells], list(ICON_SLUGS))
            self.assertTrue(all(cell['aria-hidden'] == 'true' for cell in cells))
            self.assertEqual(len(collage.select('.work-collage-art')), 66)

    def test_all_illustrations_fit_the_same_padding_without_stretching(self):
        self.assertEqual(len(DIRECTORY_COLLAGE_CROPS), 11)
        self.assertTrue(all(len(row) == 6 for row in DIRECTORY_COLLAGE_CROPS))
        crops = [crop for row in DIRECTORY_COLLAGE_CROPS for crop in row]
        art = BeautifulSoup(directory_collage(), 'html.parser').select('.work-collage-art')
        image_width, image_height = DIRECTORY_COLLAGE_SIZE
        for element, (x, y, width, height) in zip(art, crops, strict=True):
            style = dict(rule.split(':', 1) for rule in element['style'].split(';'))
            display_width = float(style['width'].rstrip('%'))
            display_height = float(style['height'].rstrip('%'))
            self.assertGreater(display_width, 0)
            self.assertGreater(display_height, 0)
            self.assertLessEqual(display_width, 80)
            self.assertLessEqual(display_height, 80)
            self.assertAlmostEqual(max(display_width, display_height), 80)
            self.assertAlmostEqual(display_width / display_height * 200 / 120, width / height, places=6)
            px, py = [float(v.rstrip('%')) for v in style['background-position'].split()]
            self.assertAlmostEqual(px / 100 * (image_width - width), x, places=4)
            self.assertAlmostEqual(py / 100 * (image_height - height), y, places=4)
            self.assertGreaterEqual(x, 0)
            self.assertGreaterEqual(y, 0)
            self.assertLessEqual(x + width, image_width)
            self.assertLessEqual(y + height, image_height)

    def test_published_artwork_matches_the_crop_map_and_keeps_transparency(self):
        for extension in ('png', 'webp'):
            with Image.open(ROOT / f'assets/work/industry-collage-66.{extension}') as image:
                self.assertEqual(image.size, DIRECTORY_COLLAGE_SIZE)
                self.assertIn('A', image.getbands())
                self.assertEqual(image.getchannel('A').getextrema(), (0, 255))
                for row in DIRECTORY_COLLAGE_CROPS:
                    for x, y, width, height in row:
                        crop = image.getchannel('A').crop((x, y, x + width, y + height))
                        self.assertIsNotNone(crop.getbbox())


if __name__ == '__main__':
    unittest.main()
