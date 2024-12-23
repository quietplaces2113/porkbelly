from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def oyster_omelette():
    ingredients = [
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.OYSTERS, 8, Units.CNT),
        IngredientPouch(Ingredients.EGGS, 3, Units.CNT),
        IngredientPouch(Ingredients.POTATO_FLOUR, 1.5, Units.TSP),
        IngredientPouch(Ingredients.WHITE_PEPPER),
        IngredientPouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.SPRING_ONIONS, 4, Units.TBSP)
    ]

    return Recipe('oyster omelette', ingredients, 1)


def steamed_eggs():
    ingredients = [
        IngredientPouch(Ingredients.DRIED_SHIITAKE_MUSHROOMS, 2, Units.CNT),
        IngredientPouch(Ingredients.EGGS, 3, Units.CNT),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 0.66, Units.CUP),
        IngredientPouch(Ingredients.SALT, 0.25, Units.TSP),
        IngredientPouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        IngredientPouch(Ingredients.SPRING_ONIONS, 2, Units.TBSP),
        IngredientPouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.LIGHT_SOY_SAUCE, 2, Units.TSP),
        IngredientPouch(Ingredients.COOKING_OIL, 1, Units.TBSP),
        IngredientPouch(Ingredients.GROUND_PORK, 4, Units.OZ),
        IngredientPouch(Ingredients.SHAOXING_WINE, 1, Units.TSP)
    ]
    return Recipe('steamed eggs', ingredients, 1)
