from tests import ScraperTest

from recipe_scrapers.kennymcgovern import KennyMcGovern


class TestKennyMcGovernScraper(ScraperTest):

    scraper_class = KennyMcGovern

    def test_host(self):
        self.assertEqual("kennymcgovern.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Crispy Chicken Strips")

    def test_image(self):
        self.assertEqual(
            self.harvester_class.image(),
            None,
        )

    def test_total_time(self):
        self.assertEqual(16, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("1 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "8 tablespoons panko breadcrumbs",
                "4 tablespoons plain flour",
                "1/4 teaspoon garlic powder",
                "1/4 teaspoon onion granules",
                "1/4 teaspoon cayenne pepper",
                "1/4 teaspoon dried Italian herbs",
                "1/2 teaspoon sea salt",
                "1/4 teaspoon black pepper",
                "4 tablespoons plain flour",
                "1/4 teaspoon sea salt",
                "Pinch black pepper",
                "1 egg",
                "3 tablespoons milk",
                "1 skinless, boneless chicken breast fillet (around 114g)",
                "vegetable oil (for deep frying)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Breading prep\nIn a large bowl, add panko breadcrumbs, plain flour, garlic powder, onion granules, cayenne pepper, dried Italian herbs, sea salt & black pepper. Mix well.\nFlour dusting prep\nOn a plate, mix plain flour, sea salt & black pepper. Mix well.\nEgg prep\nIn a bowl, combine egg and milk and whisk thoroughly.\nChicken prep\nCut the chicken into 6-7 strips. Dip a chicken strip firstly into the plate of seasoned flour, then into the egg / milk mixture and finally into the breadcrumb mix, pressing well to ensure the chicken strip is nicely coated with breadcrumbs. Set the breaded chicken strip aside on a plate and repeat the process until all of the chicken strips are coated. At this stage the chicken strips are ready to cook, or can be covered and kept aside in the fridge for up to 24 hours.\nTime to cook!\nHeat oil for deep frying to around 180c. Carefully place each breaded chicken strip into the hot oil and fry for around 6 minutes, turning occasionally until the chicken strips are crispy and golden. Lift the chicken strips from the oil using a slotted spoon, drain off any excess oil and set aside on a plate.\nServe the crispy chicken strips with hot sauce, BBQ sauce or ranch dressing.",
            self.harvester_class.instructions(),
        )
