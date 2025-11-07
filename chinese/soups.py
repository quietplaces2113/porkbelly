from ingredients import Pouch, Ingredients, Units
from recipe import Recipe


def soup_of_salted_duck_eggs():
    ingredients = [
        Pouch(Ingredients.PORK_TENDERLOIN, 5, Units.OZ),
        Pouch(Ingredients.SALTED_DUCK_EGGS, 2, Units.CNT),
        Pouch(Ingredients.MUSTARD_GREENS, 11, Units.OZ),
        Pouch(Ingredients.GINGER, .5, Units.OZ),
        Pouch(Ingredients.CHICKEN_STOCK, 6.33, Units.CUP),
        Pouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.SALT, .5, Units.TSP),
        Pouch(Ingredients.SHAOXING_WINE, .5, Units.TBSP),
        Pouch(Ingredients.POTATO_FLOUR, 1.5, Units.TSP)
    ]

    return Recipe('soup of salted duck eggs', ingredients, 1)


def taro_and_arugula_soup():
    ingredients = [
        Pouch(Ingredients.TARO, 1.75, Units.LB),
        Pouch(Ingredients.CHICKEN_STOCK, 6.33, Units.CUP),
        Pouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        Pouch(Ingredients.ARUGULA_LEAVES, 7, Units.OZ),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.WHITE_PEPPER),
        Pouch(Ingredients.SPRING_ONIONS, 3, Units.CNT)
    ]

    return Recipe('taro and arugula soup', ingredients, 1)


def chicken_soup():
    ingredients = [
        Pouch(Ingredients.CHICKEN, 1, Units.CNT),
        Pouch(Ingredients.GINGER, 0.5, Units.OZ),
        Pouch(Ingredients.SPRING_ONIONS, 2, Units.CNT),
        Pouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.WHITE_PEPPER)
    ]

    return Recipe('chicken soup', ingredients, 1)
