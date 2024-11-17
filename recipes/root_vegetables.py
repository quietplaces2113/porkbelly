from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def potato_sliver_bing():
    ingredients = [
        IngredientPouch(Ingredients.POTATO, 9, Units.OZ),
        IngredientPouch(Ingredients.SPRING_ONION, 3, Units.TBSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.SICHUAN_PEPPER, 0.25, Units.TSP)
    ]

    return Recipe('potato and sliver bing', ingredients, 1)
