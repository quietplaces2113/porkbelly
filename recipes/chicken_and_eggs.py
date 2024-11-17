from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def oyster_omelette():
    ingredients = [
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.OYSTER, 8, Units.CNT),
        IngredientPouch(Ingredients.EGG, 3, Units.CNT),
        IngredientPouch(Ingredients.POTATO_FLOUR, 1.5, Units.TSP),
        IngredientPouch(Ingredients.WHITE_PEPPER),
        IngredientPouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.SPRING_ONION, 4, Units.TBSP)
    ]

    recipe = Recipe('oyster omelette', ingredients, 1)
    return recipe
