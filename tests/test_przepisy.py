from tests import ScraperTest

from recipe_scrapers.przepisy import Przepisy

# test recipe's URL
# https://www.przepisy.pl/przepis/placki-ziemniaczane


class TestPrzepisyScraper(ScraperTest):

    scraper_class = Przepisy

    def test_host(self):
        self.assertEqual("przepisy.pl", self.harvester_class.host())

    def test_language(self):
        self.assertEqual("pl", self.harvester_class.language())

    def test_title(self):
        self.assertEqual("Placki ziemniaczane", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                'ziemniaki',
                'cebula',
                'jajka',
                'Przyprawa w Mini kostkach Czosnek Knorr',
                'Gałka muszkatołowa z Indonezji Knorr',
                'sól',
                'mąka'
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Obierz ziemniaki, zetrzyj na tarce. Odsącz masę przez sito. Zetrzyj cebulę na tarce.\nDodaj do ziemniaków cebulę, jajka, gałkę muszkatołową oraz mini kostkę Knorr.\nWymieszaj wszystko dobrze, dodaj mąkę, aby nadać masie odpowiednią konsystencję.\nRozgrzej na patelni olej, nakładaj masę łyżką. Smaż placki z obu stron na złoty brąz i od razu podawaj.",
            self.harvester_class.instructions(),
        )
