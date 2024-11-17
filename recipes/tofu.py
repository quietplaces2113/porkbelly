from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def sour_and_hot_silken_tofu():
    ingredients = [
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.SILKEN_TOFU, 11, Units.OZ),
        IngredientPouch(Ingredients.CHINKIANG_VINEGAR, 1, Units.TBSP),
        IngredientPouch(Ingredients.LIGHT_SOY_SAUCE, 2, Units.TSP),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 2, Units.TBSP),
        IngredientPouch(Ingredients.CHILLI_OIL, 3, Units.TSP),
        IngredientPouch(Ingredients.SESAME_OIL, 1, Units.TSP),
        IngredientPouch(Ingredients.SPRING_ONION, 2, Units.TBSP),
        IngredientPouch(Ingredients.GARLIC, 0.5, Units.TSP),
        IngredientPouch(Ingredients.SICHUAN_PRESERVED_VEGETABLE, 2, Units.TBSP),
        IngredientPouch(Ingredients.BOMBAY_MIX)
    ]

    recipe = Recipe('sour and hot silken tofu', ingredients, 1)
    return recipe
