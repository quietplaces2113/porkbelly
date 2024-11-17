from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def stir_fried_beansprouts_with_chinese_chives():
    ingredients = [
        IngredientPouch(Ingredients.CELERY_STICKS, 2, Units.CNT),
        IngredientPouch(Ingredients.LILY_BULBS, 4, Units.OZ),
        IngredientPouch(Ingredients.MACADAMIA_NUTS, 2, Units.OZ),
        IngredientPouch(Ingredients.SUGAR, 0.125, Units.TSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.COOKING_OIL, 1.5, Units.TBSP),
        IngredientPouch(Ingredients.GARLIC)
    ]

    recipe = Recipe('stir fried bean sprouts with chinese chives', ingredients, 1)
    return recipe
