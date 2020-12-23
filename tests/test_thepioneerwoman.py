from tests import ScraperTest

from recipe_scrapers.thepioneerwoman import ThePioneerWoman


class TestThePioneerWomanScraper(ScraperTest):

    scraper_class = ThePioneerWoman
    maxDiff = None

    def test_host(self):
        self.assertEqual("thepioneerwoman.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Patty Melts")

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/patty-melt-1597698088.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 stick butter",
                "1 whole large onion, halved and sliced",
                "1 1/2 lb. ground beef",
                "salt and pepper, to taste",
                "5 dashes Worcestershire sauce",
                "8 slices Swiss cheese",
                "8 slices rye bread",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a medium skillet, melt 2 tablespoons of butter over medium-low heat. Throw in the sliced onions and cook slowly for 20 to 25 minutes, stirring occasionally, until the onions are golden brown and soft.&nbsp; In a medium bowl, mix together the ground beef, salt & pepper, and Worcestershire. Form into 4 patties. Melt 2 tablespoons butter in a separate skillet over medium heat. Cook the patties on both sides until totally done in the middle.&nbsp; Assemble patty melts this way: Slice of bread, slice of cheese, hamburger patty, 1/4 of the cooked onions, another slice of cheese, and another slice of bread. On a clean griddle or in a skillet, melt 2 tablespoons butter and grill the sandwiches over medium heat until golden brown. Remove the sandwiches and add the remaining 2 tablespoons of butter to the skillet. Turn the sandwiches to the skillet, flipping them to the other side. Cook until golden brown and crisp, and until cheese is melted.&nbsp; Slice in half and serve immediately!",
            self.harvester_class.instructions(),
        )
