from ingredients import Ingredients, IngredientPouch
from recipe import Recipe
from units import Units


def clams_in_black_bean_sauce():
    ingredients = [
        IngredientPouch(Ingredients.CLAM, 35, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.FERMENTED_BLACK_BEANS, 2.5, Units.TBSP),
        IngredientPouch(Ingredients.GINGER, 2, Units.TSP),
        IngredientPouch(Ingredients.GARLIC, 1, Units.TBSP),
        IngredientPouch(Ingredients.RED_CHILLI_PEPPER, 1.5, Units.CNT),
        IngredientPouch(Ingredients.GREEN_BELL_PEPPER, 3, Units.TBSP),
        IngredientPouch(Ingredients.SHAOXING_WINE, 2, Units.TBSP),
        IngredientPouch(Ingredients.DARK_SOY_SAUCE, 1, Units.TSP),
        IngredientPouch(Ingredients.LIGHT_SOY_SAUCE, 1, Units.TSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.POTATO_FLOUR, 1, Units.TSP),
        IngredientPouch(Ingredients.SPRING_ONION, 2, Units.TBSP),
    ]

    recipe = Recipe('clams in black bean sauce', ingredients, 1)
    return recipe
