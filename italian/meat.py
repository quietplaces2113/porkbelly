from ingredients import Ingredients, Pouch
from recipe import Recipe
from units import Units


def oven_roasted_chicken_with_garlic_and_rosemary():
    ingredients = [
        Pouch(Ingredients.CHICKEN, 1, Units.CNT),
        Pouch(Ingredients.ROSEMARY, 2, Units.CNT),
        Pouch(Ingredients.GARLIC),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.BLACK_PEPPER),
        Pouch(Ingredients.COOKING_OIL, 2, Units.TBSP)
    ]

    return Recipe('oven roasted chicken with garlic and rosemary', ingredients, 1)
