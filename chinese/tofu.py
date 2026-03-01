from ingredients import Ingredients
from recipe import Recipe


def firm_tofu_with_green_bell_peppers():
    ingredients = [
        Ingredients.FIRM_TOFU,
        Ingredients.GREEN_BELL_PEPPERS,
        Ingredients.COOKING_OIL,
        Ingredients.LIGHT_SOY_SAUCE,
        Ingredients.SALT
    ]

    return Recipe('firm tofu with green bell peppers', ingredients)


def silken_tofu_with_pickled_mustard_greens():
    ingredients = [
        Ingredients.PICKLED_MUSTARD_GREENS,
        Ingredients.COOKING_OIL,
        Ingredients.CHICKEN_STOCK,
        Ingredients.SALT,
        Ingredients.WHITE_PEPPER,
        Ingredients.SILKEN_TOFU,
        Ingredients.POTATO_FLOUR,
        Ingredients.SPRING_ONIONS,
    ]

    return Recipe('silken tofu with pickled mustard greens', ingredients)
