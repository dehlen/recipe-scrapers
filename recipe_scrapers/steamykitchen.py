from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class SteamyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "steamykitchen.com"

    def title(self):
        return self.schema.title()

    def description(self):
        return self.schema.description()

    def total_time(self):
        return self.schema.total_time()

    def prep_time(self):
        return self.schema.prep_time()

    def cook_time(self):
        return self.schema.cook_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        img = self.soup.find("meta", {"property": "og:image", "content": True})
        return img.get("content")

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()