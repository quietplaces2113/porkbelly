from dataclasses import dataclass

from ingredients import Pouch


@dataclass
class Recipe:
    recipe_name: str
    ingredients: list[Pouch]
    servings: int
