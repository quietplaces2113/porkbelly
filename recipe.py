from dataclasses import dataclass

from ingredients import Ingredients


@dataclass
class Recipe:
    recipe_name: str
    ingredients: list[Ingredients]
