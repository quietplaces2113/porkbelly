from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def stir_fried_celery_with_lily_bulbs_and_macadamia_nuts():
    ingredients = [
        IngredientPouch(Ingredients.CELERY_STICKS, 2, Units.CNT),
        IngredientPouch(Ingredients.LILY_BULBS, 4, Units.OZ),
        IngredientPouch(Ingredients.MACADAMIA_NUTS, 2, Units.OZ),
        IngredientPouch(Ingredients.SUGAR, 0.125, Units.TSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.COOKING_OIL, 1.5, Units.TBSP),
        IngredientPouch(Ingredients.GARLIC)
    ]

    return Recipe('stir fried celery with lily bulbs and macadamia nuts', ingredients, 1)


def chopped_celery_with_ground_beef():
    ingredients = [
        IngredientPouch(Ingredients.CELERY_STICKS, 11, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.GROUND_BEEF, 4, Units.OZ),
        IngredientPouch(Ingredients.SICHUAN_CHILLI_BEAN_PASTE, 1.5, Units.TBSP),
        IngredientPouch(Ingredients.GINGER, 1.5, Units.TBSP),
        IngredientPouch(Ingredients.LIGHT_SOY_SAUCE),
        IngredientPouch(Ingredients.CHINKIANG_VINEGAR, 1, Units.TSP)
    ]

    return Recipe('chopped celery with ground beef', ingredients, 1)
