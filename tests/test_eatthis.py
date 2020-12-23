from tests import ScraperTest

from recipe_scrapers.eatthis import EatThis


class TestEatThis(ScraperTest):

    scraper_class = EatThis

    def test_host(self):
        self.assertEqual("eat-this.org", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Cremige, vegane Rahmchampignons"
        )

    def test_description(self):
        self.assertEqual(
            self.harvester_class.description(), "Leckere, cremige Rahmchampignons – das war mein Soulfood aus den Kindertagen! Unsere vegane Version kann da locker mithalten, ach was, eigentlich schmeckt sie noch viel besser. Und Kalorien müssen bei unserer Sauce auch nicht großartig gezählt werden. Soulfood deluxe! 💚"
        )

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_prep_time(self):
        self.assertEqual(5, self.harvester_class.prep_time())

    def test_cook_time(self):
        self.assertEqual(20, self.harvester_class.cook_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 Zwiebeln",
                "4 EL Olivenöl",
                "1 Zweig Thymian",
                "2 TL Salz",
                "600 g braune Champignons (möglichst klein)",
                "2 EL Mehl",
                "100 ml Weißwein",
                "300 ml Gemüsebrühe",
                "200 ml Sojamilch",
                "2 TL schwarzer Pfeffer (grob gemahlen)",
                "1 Prise Muskat",
                "4 EL Sojajoghurt",
                "1/2 Bund Petersilie",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Zwiebeln fein würfeln. Olivenöl in einen heißen Topf geben, Zwiebel und Thymian bei mittlerer bis hoher Hitze 5 Minuten glasig dünsten. Mit Salz würzen.\nChampignons putzen, mit in den Topf geben und 5 Minuten schmoren.\nMehl hinzufügen, 1 Minute unter Rühren anrösten. Anschließend mit Weißwein und Gemüsebrühe ablöschen.\nMit Sojamilch aufgießen, mit Pfeffer und Muskat würzen und aufkochen. 15 Minuten mit geschlossenem Deckel schmoren lassen. Zum Schluss den Sojajoghurt unterrühren und eine Minute mitköcheln lassen.\nVegane Rahmchampignons mit frisch gehackter Petersilie auf Basmati-Wildreismischung servieren."
            ,self.harvester_class.instructions(),
        )
