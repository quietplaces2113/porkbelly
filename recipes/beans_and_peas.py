from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def stir_fried_beansprouts_with_chinese_chives():
    ingredients = [
        IngredientPouch(Ingredients.CHINESE_CHIVE, 4.25, Units.OZ),
        IngredientPouch(Ingredients.BEANSPROUT, 4, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.RED_BELL_PEPPER),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.CHINKIANG_VINEGAR, 1, Units.TSP)
    ]

    recipe = Recipe('stir fried beansprouts with chinese chives', ingredients, 1)
    return recipe
