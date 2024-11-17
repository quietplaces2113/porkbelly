from dataclasses import dataclass

from ingredients import IngredientPouch


@dataclass
class Recipe:
    recipe_name: str
    ingredients: list[IngredientPouch]
    servings: int
