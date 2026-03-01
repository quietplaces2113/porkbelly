from ingredients import Ingredients
from recipe import Recipe


def soup_of_salted_duck_eggs():
    ingredients = [
        Ingredients.PORK_TENDERLOIN,
        Ingredients.SALTED_DUCK_EGGS,
        Ingredients.MUSTARD_GREENS,
        Ingredients.GINGER,
        Ingredients.CHICKEN_STOCK,
        Ingredients.COOKING_OIL,
        Ingredients.SALT,
        Ingredients.SHAOXING_WINE,
        Ingredients.POTATO_FLOUR,
    ]

    return Recipe('soup of salted duck eggs', ingredients)


def taro_and_arugula_soup():
    ingredients = [
        Ingredients.TARO,
        Ingredients.CHICKEN_STOCK,
        Ingredients.COOKING_OIL,
        Ingredients.ARUGULA_LEAVES,
        Ingredients.SALT,
        Ingredients.WHITE_PEPPER,
        Ingredients.SPRING_ONIONS
    ]

    return Recipe('taro and arugula soup', ingredients)


def chicken_soup():
    ingredients = [
        Ingredients.CHICKEN,
        Ingredients.GINGER,
        Ingredients.SPRING_ONIONS,
        Ingredients.SHAOXING_WINE,
        Ingredients.SALT,
        Ingredients.WHITE_PEPPER
    ]

    return Recipe('chicken soup', ingredients)
