from tests import ScraperTest
from recipe_scrapers.thespruceeats import TheSpruceEats

class TestTheSpruceEatsScraper(ScraperTest):

    scraper_class = TheSpruceEats
    maxDiff = None

    def test_host(self):
        self.assertEqual("thespruceeats.com", self.harvester_class.host())

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "A Refreshing Old-Fashioned Potato Salad With Oil and Vinegar Dressing"
        )

    def test_total_time(self):
        self.assertEqual(40, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.thespruceeats.com/thmb/hRuKK09q9XpCBpjdYwBSg0QjcVA=/2048x1365/filters:fill(auto,1)/old-fashioned-potato-salad-3059757-hero-01-5c3e8ea0c9e77c0001930557.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "1 1/2 to 2 pounds large potatoes (about 3 large potatoes)",
                "1 large onion",
                "1/4 cup extra virgin olive oil",
                "3 tablespoons apple cider vinegar",
                "1 clove garlic (mashed and finely minced)",
                "2 tablespoons fresh parsley (minced)",
                "2 tablespoons granulated sugar",
                "1/2 teaspoon salt (or to taste)",
                "1/4 teaspoon black pepper",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Gather the ingredients. The Spruce\nPeel the potatoes and put them in a medium saucepan. Add water to cover and about 1 teaspoon of salt. Bring to a boil over high heat. The Spruce\nCover and reduce the heat to medium-low and continue cooking until the potatoes are fork-tender—about 20 to 25 minutes. The Spruce\nDrain and cool completely in the pan with the cover ajar. The Spruce\nSlice the cooled potatoes into 1/4 inch slices and put them in a large bowl. The Spruce\nPeel the onion and slice it in half lengthwise. Cut it crosswise into thin slices and add to the bowl with the potatoes. The Spruce\nIn a small bowl, whisk together the olive oil, vinegar, garlic, minced parsley, sugar, salt, and black pepper. The Spruce\nPour the dressing mixture over the potatoes and onions, then toss gently to combine the ingredients. The Spruce\nTaste and season the salad with additional salt and pepper, as needed. Cover the bowl with plastic wrap and chill until serving time. The Spruce\nFor best flavor, make the salad at least 2 hours before you plan to serve it.\nEnjoy!\nChoose low-starch potatoes for salads, such as red-skinned, Yukon Gold, fingerlings, or new potatoes. Those types of potatoes are lower in starch than russets and other baking potatoes, and they tend to hold their shape better.\nIf you want to make this dish in advance, up to 24 hours before serving, cook and cube the potatoes, slice the onions, and combine the dressing ingredients. Refrigerate the ingredients in separate containers. About 2 hours before serving time, combine the ingredients and toss to blend. Refrigerate until serving time.\nThis potato salad is an excellent choice for a picnic or cookout. Even though there's no mayonnaise included, you should still keep the salad as cold as possible. Make sure it doesn't stay out of a cooler or refrigerator for more than 2 hours (no more than 1 hour if the temperature is above 90 F) or nestle the salad bowl in a bed of ice to keep it at the safe temperature of 40 F or below for serving.\nThe salad is versatile as well. Consider adding fresh chives or dill to the salad along with the parsley. If you don't care for raw garlic in a salad, use about 1/2 teaspoon of garlic powder in the dressing or leave it out altogether.\nAlternatively, add some sliced cucumber to the salad. Cut the cucumber—peeled or not—in half lengthwise, scoop out the seeds, and slice the halves thinly. Toss the cucumber with the potatoes and onions.\npotato\nno mayo potato salad\nside dish\namerican",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(0, self.harvester_class.ratings())
