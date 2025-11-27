from ingredients import Pouch, Ingredients, Units
from recipe import Recipe


def blanched_choy_sum_with_sizzling_oil():
    ingredients = [
        Pouch(Ingredients.CHOY_SUM, 11, Units.OZ),
        Pouch(Ingredients.SPRING_ONIONS, 2, Units.CNT),
        Pouch(Ingredients.GINGER, .5, Units.OZ),
        Pouch(Ingredients.RED_BELL_PEPPERS),
        Pouch(Ingredients.SALT, 1, Units.TSP),
        Pouch(Ingredients.COOKING_OIL, 4, Units.TBSP),
        Pouch(Ingredients.LIGHT_SOY_SAUCE, 2, Units.TBSP)
    ]

    return Recipe('blanched choy sum with sizzling oil', ingredients, 1)


def spinach_with_chilli_and_fermented_tofu():
    ingredients = [
        Pouch(Ingredients.WATER_SPINACH, 11.5, Units.OZ),
        Pouch(Ingredients.RED_CHILLI_PEPPERS, .5, Units.CNT),
        Pouch(Ingredients.WHITE_FERMENTED_TOFU),
        Pouch(Ingredients.SUGAR, .25, Units.TSP),
        Pouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        Pouch(Ingredients.GARLIC, 2, Units.TSP),
        Pouch(Ingredients.SALT)
    ]

    return Recipe('spinach with chilli and fermented tofu', ingredients, 1)


def chinese_broccoli_in_ginger_sauce():
    ingredients = [
        Pouch(Ingredients.CHINESE_BROCCOLI, .75, Units.LB),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.COOKING_OIL, 4, Units.TBSP),
        Pouch(Ingredients.GINGER, 2, Units.TBSP),
        Pouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        Pouch(Ingredients.SUGAR, .5, Units.TSP),
        Pouch(Ingredients.POTATO_FLOUR, 1, Units.TSP)
    ]

    return Recipe('chinese broccoli in ginger sauce', ingredients, 1)


# +1
def pea_shoots():
    ingredients = [
        Pouch(Ingredients.PEA_SHOOTS),
        Pouch(Ingredients.COOKING_OIL),
        Pouch(Ingredients.GINGER),
        Pouch(Ingredients.GARLIC),
        Pouch(Ingredients.SHAOXING_WINE),
        Pouch(Ingredients.SALT)
    ]

    return Recipe('pea shoots', ingredients, 1)
