from ingredients import Ingredients
from recipe import Recipe


def blanched_choy_sum_with_sizzling_oil():
    ingredients = [
        Ingredients.CHOY_SUM,
        Ingredients.SPRING_ONIONS,
        Ingredients.GINGER,
        Ingredients.RED_BELL_PEPPERS,
        Ingredients.SALT,
        Ingredients.COOKING_OIL,
        Ingredients.LIGHT_SOY_SAUCE,
    ]

    return Recipe('blanched choy sum with sizzling oil', ingredients)


def spinach_with_chilli_and_fermented_tofu():
    ingredients = [
        Ingredients.WATER_SPINACH,
        Ingredients.RED_CHILLI_PEPPERS,
        Ingredients.WHITE_FERMENTED_TOFU,
        Ingredients.SUGAR,
        Ingredients.COOKING_OIL,
        Ingredients.GARLIC,
        Ingredients.SALT
    ]

    return Recipe('spinach with chilli and fermented tofu', ingredients)


def chinese_broccoli_in_ginger_sauce():
    ingredients = [
        Ingredients.CHINESE_BROCCOLI,
        Ingredients.SALT,
        Ingredients.COOKING_OIL,
        Ingredients.GINGER,
        Ingredients.SHAOXING_WINE,
        Ingredients.SUGAR,
        Ingredients.POTATO_FLOUR
    ]

    return Recipe('chinese broccoli in ginger sauce', ingredients)


# +1
def pea_shoots():
    ingredients = [
        Ingredients.PEA_SHOOTS,
        Ingredients.COOKING_OIL,
        Ingredients.GINGER,
        Ingredients.GARLIC,
        Ingredients.SHAOXING_WINE,
        Ingredients.SALT
    ]

    return Recipe('pea shoots', ingredients)
