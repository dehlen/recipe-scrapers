from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class Panelinha(AbstractScraper):
    @classmethod
    def host(cls):
        return "panelinha.com.br"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def description(self):
        desc = self.soup.find("meta", {"property": "og:description", "content": True})
        return desc.get("content")

    def total_time(self):
        return get_minutes(
            self.soup.find("span", string="Tempo de preparo").nextSibling
        )

    def prep_time(self):
        return 0

    def cook_time(self):
        return self.total_time()

    def ingredients(self):
        ingredients = self.soup.find("h4", string="Ingredientes").nextSibling.findAll(
            "li"
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.find(
            "h4", string="Modo de preparo"
        ).nextSibling.findAll("li")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def yields(self):
        return normalize_string(
            self.soup.find("span", string="Serve").nextSibling.get_text()
        )