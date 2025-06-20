from ingredients import Pouch, Ingredients, Units
from recipe import Recipe


def firm_tofu_with_green_bell_peppers():
    ingredients = [
        Pouch(Ingredients.FIRM_TOFU, 4.25, Units.OZ),
        Pouch(Ingredients.GREEN_BELL_PEPPERS, 1, Units.CNT),
        Pouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        Pouch(Ingredients.LIGHT_SOY_SAUCE),
        Pouch(Ingredients.SALT)
    ]

    return Recipe('firm tofu with green bell peppers', ingredients, 1)


def silken_tofu_with_pickled_mustard_greens():
    ingredients = [
        Pouch(Ingredients.PICKLED_MUSTARD_GREENS, 1, Units.OZ),
        Pouch(Ingredients.COOKING_OIL, 1.5, Units.TBSP),
        Pouch(Ingredients.CHICKEN_STOCK, 1 + 2.0 / 16, Units.CUP),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.WHITE_PEPPER),
        Pouch(Ingredients.SILKEN_TOFU, 11, Units.OZ),
        Pouch(Ingredients.POTATO_FLOUR, 1.5, Units.TSP),
        Pouch(Ingredients.SPRING_ONIONS, 2, Units.TBSP)
    ]

    return Recipe('silken tofu with pickled mustard greens', ingredients, 1)
