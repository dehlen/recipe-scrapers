from tests import ScraperTest

from recipe_scrapers.yummly import Yummly


class TestYummlyScraper(ScraperTest):

    scraper_class = Yummly

    def test_host(self):
        self.assertEqual("yummly.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Carrot Milk shake")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
        [
            "100 grams carrot 4 baby carrots in number or 1 big size",
            "3 teaspoons sugar can add more if you want it sweeter",
            "1 cardamom small, powdered",
            "1 1/2 cups milk",
            "4 cashew badam or pista, for garnishing, optional"
        ],
        self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual("",
                                self.harvester_class.instructions())
