# IF things in this file continue get messy (I'd say 300+ lines) it may be time to
# find a package that parses https://schema.org/Recipe properly (or create one ourselves).
import extruct
from ._utils import get_minutes, normalize_string
from json.decoder import JSONDecodeError

SCHEMA_ORG_HOST = "schema.org"
SCHEMA_NAMES = ["Recipe", "WebPage"]

SYNTAXES = ["json-ld", "microdata"]


class SchemaOrgException(Exception):
    def __init__(self, message):
        super().__init__(message)


class SchemaOrg:
    def __init__(self, page_data):
        self.format = None
        self.data = {}

        try:
            data = extruct.extract(page_data, syntaxes=SYNTAXES, uniform=True)
        except JSONDecodeError:
            data = {}

        for syntax in SYNTAXES:
            for item in data.get(syntax, []):
                in_context = SCHEMA_ORG_HOST in item.get("@context", "")
                low_schema = [s.lower() for s in SCHEMA_NAMES]
                if in_context and item.get("@type", "").lower() in low_schema:
                    self.format = syntax
                    self.data = item
                    if item.get("@type").lower() == "webpage":
                        self.data = self.data.get("mainEntity")
                    return
                elif in_context and "@graph" in item:
                    for graph_item in item.get("@graph", ""):
                        graph_item_type = graph_item.get("@type", "")
                        if type(graph_item_type) != str:
                            continue
                        if graph_item_type.lower() in low_schema:
                            in_graph = SCHEMA_ORG_HOST in graph_item.get("@context", "")
                            self.format = syntax
                            if graph_item_type.lower() == "webpage" and in_graph:
                                self.data = self.data.get("mainEntity")
                                return
                            elif graph_item_type.lower() == "recipe":
                                self.data = graph_item
                                return
                            continue

    def language(self):
        return self.data.get("inLanguage") or self.data.get("language")

    def title(self):
        return normalize_string(self.data.get("name"))

    def description(self):
        return normalize_string(self.data.get("description"))

    def author(self):
        author = self.data.get("author")
        if author is not None:
            if type(author) == str:
                return author
            elif type(author) == list and len(author) > 0:
                if type(author[0]) == dict:
                    return author[0].get("name")
                elif type(author[0]) == str:
                    return author[0]
                else:
                    return None
            elif type(author) == dict:
                return author.get("name", None)
            else:
                return None

    def total_time(self):
        total_time = get_minutes(self.data.get("totalTime"))
        if not total_time:
            prep_time = get_minutes(self.data.get("prepTime")) or 0
            cook_time = get_minutes(self.data.get("cookTime")) or 0
            total_time = prep_time + cook_time
        return total_time

    def prep_time(self):
        return get_minutes(self.data.get("prepTime")) or 0

    def cook_time(self):
        return get_minutes(self.data.get("cookTime")) or 0

    def yields(self):
        yield_data = self.data.get("recipeYield")
        if isinstance(yield_data, list) and len(yield_data) > 0:
            recipe_yield = str(yield_data[0])
        else:
            recipe_yield = str(yield_data)
        if len(recipe_yield) <= 3:  # probably just a number. append "servings"
            return recipe_yield + " serving(s)"

        if "\n" in recipe_yield:
            recipe_yield = recipe_yield.split("\n")[-1]

        return recipe_yield

    def image(self):
        image = self.data.get("image")

        if image is None:
            return None

        if type(image) == dict:
            return image.get("url")
        elif type(image) == list and len(image) > 0:
            if type(image[0]) == dict:
                return image[0].get("url")
            elif type(image[0]) == str:
                return image[0]

        if "http://" not in image and "https://" not in image:
            # some sites give image path relative to the domain
            # in cases like this handle image url with class methods or og link
            return None

        return image

    def ingredients(self):
        ingredients = (
            self.data.get("recipeIngredient") or self.data.get("ingredients") or []
        )
        return [
            normalize_string(ingredient) for ingredient in ingredients if ingredient
        ]

    def nutrients(self):
        nutrients = self.data.get("nutrition", {})
        return {
            normalize_string(nutrient): normalize_string(value)
            for nutrient, value in nutrients.items()
            if nutrient != "@type"
        }

    def _extract_howto_instructions_text(self, schema_item):
        instructions_gist = []
        if type(schema_item) is str:
            instructions_gist.append(schema_item)
        elif schema_item.get("@type") == "HowToStep":
            if schema_item.get("name", False):
                # some sites have duplicated name and text properties (1:1)
                # others have name same as text but truncated to X chars.
                # ignore name in these cases and add the name value only if it's different from the text
                if not schema_item.get("text").startswith(
                    schema_item.get("name").rstrip(".")
                ):
                    instructions_gist.append(schema_item.get("name"))
            instructions_gist.append(schema_item.get("text"))
        elif schema_item.get("@type") == "HowToSection":
            instructions_gist.append(schema_item.get("name"))
            for item in schema_item.get("itemListElement"):
                instructions_gist += self._extract_howto_instructions_text(item)
        return instructions_gist

    def instructions(self):
        instructions = self.data.get("recipeInstructions") or ""

        if type(instructions) is list:
            instructions_gist = []
            for schema_instruction_item in instructions:
                instructions_gist += self._extract_howto_instructions_text(
                    schema_instruction_item
                )

            return "\n".join(
                normalize_string(instruction) for instruction in instructions_gist
            )

        return normalize_string(instructions)

    def ratings(self):
        ratings = self.data.get("aggregateRating", None)
        if ratings is None:
            raise SchemaOrgException("No ratings data in SchemaOrg.")

        if type(ratings) == dict:
            rating_value = ratings.get("ratingValue", None)
            return round(float(rating_value), 2) if rating_value else None
        return round(float(ratings), 2)

    def cuisine(self):
        cuisine = self.data.get("recipeCuisine")
        if isinstance(cuisine, list):
            return ",".join(cuisine)
        return cuisine
