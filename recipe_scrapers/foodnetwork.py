from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class FoodNetwork(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodnetwork.com"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    def description(self):
        return None

    def total_time(self):
        return 0

    def prep_time(self):
        return 0

    def cook_time(self):
        return 0

    def yields(self):
        return None

    def ingredients(self):
        ingredients = self.soup.findAll("div", {"class": "ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("div", {"class": "recipe-text"})

        return "\n".join(
            [
                normalize_string(instruction.get_text())
                for instruction in instructions
                if instruction.get_text(strip=True)
                not in ("Watch how to make this recipe.",)
            ]
        )