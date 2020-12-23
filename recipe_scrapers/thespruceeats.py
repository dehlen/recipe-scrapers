from ._abstract import AbstractScraper
from ._utils import normalize_string, get_minutes, get_yields

class TheSpruceEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "thespruceeats.com"

    def title(self):
        name = self.soup.find("meta", {"itemprop": "name", "content": True })
        return name.get("content", None)

    def description(self):
        desc = self.soup.find("meta", {"property": "og:description", "content": True})
        return desc.get("content")

    def total_time(self):
        element = self.soup.find(
            "div", {"class": "total-time"}
        )
        tt = element.get_text() if element else None
        return get_minutes(tt) if tt else 0
    
    def prep_time(self):
        element = self.soup.find(
            "div", {"class": "prep-time"}
        )
        pt = element.get_text() if element else None
        return get_minutes(pt) if pt else 0
    
    def cook_time(self):
        element = self.soup.find(
            "div", {"class": "cook-time"}
        )
        ct = element.get_text() if element else None
        return get_minutes(ct) if ct else 0

    def image(self):
        img = self.soup.find("meta", {"property": "og:image", "content": True})
        return img.get("content", None)

    def ingredients(self):
        ingredients = self.soup.find("ul", {"class": "ingredient-list"}).find_all(
            "li", {"class": "simple-list__item"}
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find(
            "section", {"class": "section--instructions"}
        ).find_all("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        return 0

    def yields(self):
        element = self.soup.find(
            "div", {"class": "recipe-serving"}
        )
        yield_text = element.get_text() if element else None
        return get_yields(yield_text) if yield_text else None