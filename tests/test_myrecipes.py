from tests import ScraperTest

from recipe_scrapers.myrecipes import MyRecipes


class TestMyRecipesScraper(ScraperTest):

    scraper_class = MyRecipes
    scraper_options = {"exception_handling": True}
    maxDiff = None

    def test_host(self):
        self.assertEqual("myrecipes.com", self.harvester_class.host())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F19%2F2018%2F01%2F25%2Fmyrecipestrending_1-09-18_1772_1-2000.jpg",
            self.harvester_class.image(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Cacio e Pepe")

    def test_total_time(self):
        self.assertEqual(20, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual(
            "Serves 2 (serving size: 1 1/2 cups)", self.harvester_class.yields()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "6 bucatini pasta",
                "1 ½ kosher salt, divided",
                "3 olive oil",
                "1 black pepper, plus more for garnish",
                "1 ½ pecorino Romano, grated (about 3/4 cups), plus more for garnish",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Add pasta to a large skillet over high; cover with water, and add 1 teaspoon of the salt. Bring to a boil, and cook, stirring occasionally, until nearly tender, about 6 minutes.\nMeanwhile, heat oil in a medium skillet over medium; stir in black pepper, and cook until toasted, about 1 minute. Remove from heat.\nWhisk 3 tablespoons of the pasta cooking water into oil and pepper. Using tongs, transfer pasta into oil and pepper mixture, reserving pasta cooking water in skillet. Cook over low, stirring constantly, while sprinkling in cheese.\nAdd more cooking water as needed, 1 tablespoon at a time, to create a creamy sauce. Stir in remaining 1/2 teaspoon salt. Divide pasta between 2 bowls, and garnish with pepper and cheese. Serve immediately.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(-1, self.harvester_class.ratings())


# https://www.myrecipes.com/recipe/cacio-e-pepe
