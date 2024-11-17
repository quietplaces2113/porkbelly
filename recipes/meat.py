from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def slow_cooked_beef_brisket_with_berries():
    ingredients = [
        IngredientPouch(Ingredients.BEEF_BRISKET, 1.5, Units.LB),
        IngredientPouch(Ingredients.GINGER, 2, Units.OZ),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 5.25, Units.CUP),
        IngredientPouch(Ingredients.SHAOXING_WINE, 0.33, Units.CUP),
        IngredientPouch(Ingredients.SICHUAN_PEPPER, 1, Units.TSP),
        IngredientPouch(Ingredients.GOUQI_BERRY, 2, Units.TBSP),
        IngredientPouch(Ingredients.CILANTRO),
        IngredientPouch(Ingredients.COOKING_OIL, 1, Units.TBSP),
        IngredientPouch(Ingredients.SICHUAN_CHILLI_BEAN_PASTE, 4, Units.TBSP),
        IngredientPouch(Ingredients.GINGER, 2, Units.TSP),
        IngredientPouch(Ingredients.SESAME_OIL, 1, Units.TSP),
    ]

    recipe = Recipe('slow cooked beef brisket with berries', ingredients, 1)
    return recipe
