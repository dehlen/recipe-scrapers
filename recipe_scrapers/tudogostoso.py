from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TudoGostoso(AbstractScraper):
    @classmethod
    def host(cls):
        return "tudogostoso.com.br"

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
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions_html = self.soup.findAll(
            "div", {"class": "instructions e-instructions"}
        )

        return "\n".join(
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        )

    def ratings(self):
        return self.schema.ratings()