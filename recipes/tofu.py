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
        IngredientPouch(Ingredients.SPRING_ONIONS, 2, Units.TBSP),
        IngredientPouch(Ingredients.GARLIC, 0.5, Units.TSP),
        IngredientPouch(Ingredients.SICHUAN_PRESERVED_VEGETABLE, 2, Units.TBSP),
        IngredientPouch(Ingredients.BOMBAY_MIX)
    ]

    return Recipe('sour and hot silken tofu', ingredients, 1)


def silken_tofu_with_pickled_mustard_greens():
    ingredients = [
        IngredientPouch(Ingredients.PICKLED_MUSTARD_GREENS, 1, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 1.5, Units.TBSP),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 1 + 2.0/16, Units.CUP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.WHITE_PEPPER),
        IngredientPouch(Ingredients.SILKEN_TOFU, 11, Units.OZ),
        IngredientPouch(Ingredients.POTATO_FLOUR, 1.5, Units.TSP),
        IngredientPouch(Ingredients.SPRING_ONIONS, 2, Units.TBSP)
    ]

    return Recipe('silken tofu with pickled mustard greens', ingredients, 1)
