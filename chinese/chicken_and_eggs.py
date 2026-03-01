from ingredients import Ingredients
from recipe import Recipe


def braised_chicken_with_chestnuts():
    ingredients = [
        Ingredients.BONELESS_CHICKEN_THIGHS,
        Ingredients.GINGER,
        Ingredients.SPRING_ONIONS,
        Ingredients.COOKING_OIL,
        Ingredients.SHAOXING_WINE,
        Ingredients.CHICKEN_STOCK,
        Ingredients.SUGAR,
        Ingredients.DARK_SOY_SAUCE,
        Ingredients.CHESTNUTS,
        Ingredients.SALT
    ]

    return Recipe('braised chicken with chestnets', ingredients)


def stir_fried_eggs_with_tomatoes():
    ingredients = [
        Ingredients.TOMATOES,
        Ingredients.EGGS,
        Ingredients.SALT,
        Ingredients.COOKING_OIL,
        Ingredients.SUGAR,
        Ingredients.POTATO_FLOUR
    ]

    return Recipe('stir fried eggs with tomatoes', ingredients)


def steamed_eggs():
    ingredients = [
        Ingredients.DRIED_SHIITAKE_MUSHROOMS,
        Ingredients.EGGS,
        Ingredients.CHICKEN_STOCK,
        Ingredients.SALT,
        Ingredients.SHAOXING_WINE,
        Ingredients.SPRING_ONIONS,
        Ingredients.COOKING_OIL,
        Ingredients.LIGHT_SOY_SAUCE,
        Ingredients.GROUND_PORK,
        Ingredients.SHAOXING_WINE
    ]

    return Recipe('steamed eggs', ingredients)
