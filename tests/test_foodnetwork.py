from tests import ScraperTest

from recipe_scrapers.foodnetwork import FoodNetwork


class TestFoodNetworkScraper(ScraperTest):

    scraper_class = FoodNetwork
    maxDiff = None

    def test_host(self):
        self.assertEqual("foodnetwork.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Chicken Marsala")

    def test_total_time(self):
        self.assertEqual(0, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(None, self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://d2v9mhsiek5lbq.cloudfront.net/eyJidWNrZXQiOiJsb21hLW1lZGlhLXVrIiwia2V5IjoiZm9vZG5ldHdvcmstaW1hZ2UtZGVmYXVsdC1wbGFjZWhvbGRlci5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjE5MjAsImhlaWdodCI6MTA4MCwiZml0IjoiY292ZXIifX19",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "4 (225g) boneless skinless chicken breasts",
                "Plain flour, for dredging, plus 2 tbsp",
                "85g butter",
                "1 tbsp olive oil",
                "80g sliced mushrooms",
                "2 tbsp minced garlic",
                "4 tbsp Marsala wine",
                "500ml beef stock",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "1) Put the chicken breasts between 2 pieces of waxed paper and flatten with a meat pounder until thin. Cut each chicken breast into 4 pieces. 2) Add some flour to a shallow bowl. Dredge the chicken in the flour and shake off the excess flour. 3) Add the butter and olive oil to a large saute pan over high heat and heat until it sizzles, do NOT let it brown. Add the chicken and saute until brown on both sides. 4) Stir in the sliced mushrooms and saute briefly, then add the garlic. Add the Marsala and simmer for 3 minutes, then stir in the remaining 2 tbsp of flour. 5) Pour in the beef stock and leave to simmer until the sauce thickens, about 3 to 5 minutes. Transfer the chicken to a serving platter and serve. This recipe was provided by professional chefs and has been scaled down from a bulk recipe provided by a restaurant. The Food Network kitchens chefs have not tested this recipe, in the proportions indicated, and therefore we cannot make any representation as to the results.",
            self.harvester_class.instructions(),
        )
