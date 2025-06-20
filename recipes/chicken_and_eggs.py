from ingredients import Pouch, Ingredients, Units
from recipe import Recipe


def braised_chicken_with_chestnuts():
    ingredients = [
        Pouch(Ingredients.BONELESS_CHICKEN_THIGHS, .75, Units.LB),
        Pouch(Ingredients.GINGER, .5, Units.OZ),
        Pouch(Ingredients.SPRING_ONIONS, 2, Units.CNT),
        Pouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        Pouch(Ingredients.SHAOXING_WINE, 1.5, Units.TBSP),
        Pouch(Ingredients.CHICKEN_STOCK, 1, Units.CUP),
        Pouch(Ingredients.CHICKEN_STOCK, 2, Units.TBSP),
        Pouch(Ingredients.SUGAR, 1, Units.TBSP),
        Pouch(Ingredients.DARK_SOY_SAUCE, 1.5, Units.TSP),
        Pouch(Ingredients.CHESTNUTS, 7, Units.OZ),
        Pouch(Ingredients.SALT)
    ]

    return Recipe('braised chicken with chestnets', ingredients, 1)


def stir_fried_eggs_with_tomatoes():
    ingredients = [
        Pouch(Ingredients.TOMATOES, 2, Units.CNT),
        Pouch(Ingredients.EGGS, 2, Units.CNT),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.COOKING_OIL, 4, Units.TBSP),
        Pouch(Ingredients.SUGAR, .5, Units.TSP),
        Pouch(Ingredients.POTATO_FLOUR, .5, Units.TSP)
    ]

    return Recipe('stir fried eggs with tomatoes', ingredients, 1)


def steamed_eggs():
    ingredients = [
        Pouch(Ingredients.DRIED_SHIITAKE_MUSHROOMS, 2, Units.CNT),
        Pouch(Ingredients.EGGS, 3, Units.CNT),
        Pouch(Ingredients.CHICKEN_STOCK, 0.66, Units.CUP),
        Pouch(Ingredients.SALT, 0.25, Units.TSP),
        Pouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        Pouch(Ingredients.SPRING_ONIONS, 2, Units.TBSP),
        Pouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        Pouch(Ingredients.LIGHT_SOY_SAUCE, 2, Units.TSP),
        Pouch(Ingredients.COOKING_OIL, 1, Units.TBSP),
        Pouch(Ingredients.GROUND_PORK, 4, Units.OZ),
        Pouch(Ingredients.SHAOXING_WINE, 1, Units.TSP)
    ]

    return Recipe('steamed eggs', ingredients, 1)
