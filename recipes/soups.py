from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def chicken_soup():
    ingredients = [
        IngredientPouch(Ingredients.CHICKEN, 1, Units.CNT),
        IngredientPouch(Ingredients.GINGER, 0.5, Units.OZ),
        IngredientPouch(Ingredients.SPRING_ONIONS, 2, Units.CNT),
        IngredientPouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.WHITE_PEPPER)
    ]

    return Recipe('chicken soup', ingredients, 1)


def taro_and_arugula_soup():
    ingredients = [
        IngredientPouch(Ingredients.TARO, 1.75, Units.LB),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 6.33, Units.CUP),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.ARUGULA_LEAVES, 7, Units.OZ),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.WHITE_PEPPER),
        IngredientPouch(Ingredients.SPRING_ONIONS, 3, Units.CNT)
    ]

    return Recipe('taro and arugula soup', ingredients, 1)
