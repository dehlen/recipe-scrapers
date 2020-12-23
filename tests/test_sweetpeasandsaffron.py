from tests import ScraperTest
from recipe_scrapers.sweetpeasandsaffron import SweetPeasAndSaffron


class TestSweetPeasAndSaffron(ScraperTest):

    scraper_class = SweetPeasAndSaffron

    def test_host(self):
        self.assertEqual("sweetpeasandsaffron.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            "7 Healthy Steel Cut Oats Recipes", self.harvester_class.title()
        )

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://sweetpeasandsaffron.com/wp-content/uploads/2017/05/steel-cut-oats-7-ways-TEXT.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            ['1 tablespoon butter ((optional; to toast the oats))',
             '1 cup steel cut oats ((see note *))',
             '3 Instant Pot or 4 (slow cooker, stove-top) cups water',
             '1 teaspoon vanilla extract',
             '1 teaspoon cinnamon',
             'After cooking:',
             '2 tablespoons maple syrup (or more to taste)',
             '1 large apple (peeled and cut into small pieces)',
             '1 cup unsweetened apple sauce ((stir in after cooking if using Instant Pot))',
             '1/3 cup chopped pecans ((to top))',
             '1/4 teaspoon ground nutmeg',
             '1/4 teaspoon ground cloves',
             '1 teaspoon vanilla extract',
             '1 cup pumpkin puree ((stir in after cooking if using Instant Pot))',
             '2 tablespoons pumpkin seeds/pepitas ((to top))',
             'zest from 1 lemon ((add after cooking base recipe))',
             '1-2 cups blueberries ((add after cooking base recipe))',
             'chia seeds ((add after cooking base recipe))',
             '1 tablespoon cocoa powder',
             '2 tablespoons peanut butter ((stir in after cooking base recipe))',
             '1-2 cups berries ((to top))',
             'chia seeds ((add after cooking base recipe))',
             '1 teaspoon coconut extract ((omit cinnamon from base recipe))',
             '1 tablespoon key lime zest ((stir in after cooking base recipe))',
             '1-2 cups strawberries (kiwis or pineapple (to top))',
             '1/4 cup toasted coconut ((to top))',
             '1 cup shredded zucchini ((drained of excess liquid; stir in after cooking '
             'base recipe))',
             '1/4 cup chocolate chips ((to top))',
             '1 teaspoon chai spice blend ((omit cinnamon from base recipe; *see note))',
             '1 cup chopped strawberries',
             '1-2 cups chopped fresh strawberries ((to top))'
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Instant Pot\n(Optional but adds extra flavor). Select the 'sauté' function on the Instant Pot. Add the butter and melt. Add the steel cut oats and sauté, stirring occasionally for 5 or so minutes, until fragrant and golden.\nAdd the water, vanilla and cinnamon (and other ingredients as needed for flavor variations)\nCook on high pressure for 2 minutes, followed by natural pressure release (let the Instant Pot sit for 20 minutes up to 120 minutes).\nRemove lid and stir in maple syrup and any other ingredients for the flavor variations.\nSlow Cooker\n(Optional but adds extra flavor). Heat a pan over medium heat. Add the butter and melt. Add the steel cut oats and sauté, stirring occasionally for 5 or so minutes, until fragrant and golden.\nSpray the inside of your slow cooker with cooking spray or use a slow cooker liner. Transfer steel cut oats and add the water, vanilla and cinnamon (and other ingredients as needed for flavor variations)\nCover and cook on low for 6-8 hours.\nStir in maple syrup and any other ingredients for the flavor variations.\nStove Top\nHeat a 4 quart pot over medium heat. Add the butter and melt. Add the steel cut oats and sauté, stirring occasionally for 5 or so minutes, until fragrant and golden.\nAdd the water, vanilla and cinnamon (and other ingredients as needed for flavor variations).\nReduce heat and simmer, stirring occasionally, for 25-35 minutes.\nRemove from heat and stir in maple syrup and any other ingredients for the flavor variations.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        return self.assertEqual(4.38, self.harvester_class.ratings())

    def test_author(self):
        return self.assertEqual("Denise Bustard", self.harvester_class.author())
