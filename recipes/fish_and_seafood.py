from ingredients import Ingredients, IngredientPouch
from recipe import Recipe
from units import Units


def clams_in_black_bean_sauce():
    ingredients = [
        IngredientPouch(Ingredients.CLAMS, 35, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.FERMENTED_BLACK_BEANS, 2.5, Units.TBSP),
        IngredientPouch(Ingredients.GINGER, 2, Units.TSP),
        IngredientPouch(Ingredients.GARLIC, 1, Units.TBSP),
        IngredientPouch(Ingredients.RED_CHILLI_PEPPERS, 1.5, Units.CNT),
        IngredientPouch(Ingredients.GREEN_BELL_PEPPERS, 3, Units.TBSP),
        IngredientPouch(Ingredients.SHAOXING_WINE, 2, Units.TBSP),
        IngredientPouch(Ingredients.DARK_SOY_SAUCE, 1, Units.TSP),
        IngredientPouch(Ingredients.LIGHT_SOY_SAUCE, 1, Units.TSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.POTATO_FLOUR, 1, Units.TSP),
        IngredientPouch(Ingredients.SPRING_ONIONS, 2, Units.TBSP),
    ]

    return Recipe('clams in black bean sauce', ingredients, 1)


def salt_and_pepper_squid():
    ingredients = [
        IngredientPouch(Ingredients.SQUID, 2, Units.CNT),
        IngredientPouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        IngredientPouch(Ingredients.POTATO_FLOUR, 3, Units.TBSP),
        IngredientPouch(Ingredients.COOKING_OIL, 1 + 10.0/16, Units.CUP),
        IngredientPouch(Ingredients.GARLIC, 2, Units.TBSP),
        IngredientPouch(Ingredients.SPRING_ONIONS, 4, Units.TBSP),
        IngredientPouch(Ingredients.RED_CHILLI_PEPPERS, 2, Units.TBSP),
        IngredientPouch(Ingredients.SICHUAN_PEPPER, 0.25, Units.TSP),
        IngredientPouch(Ingredients.SALT, 0.75, Units.TSP),
    ]

    return Recipe('salt and pepper squid', ingredients, 1)
