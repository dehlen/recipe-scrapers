from ._abstract import AbstractScraper


class AtelierDesChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "atelierdeschefs.fr"

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
        yields = self.soup.find("option", {"class": "yield"})
        return f"{yields.get('value')} Servings"

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        # clean the text : remove trailing newlines, and consecutives newlines
        instructions = self.soup.find(
            "ul", {"class": "recipe-steps arial marginT20"}
        ).text.splitlines()
        return "\n".join(
            [paragraph for paragraph in instructions if len(paragraph) > 0]
        )

    def ratings(self):
        return self.schema.ratings()
