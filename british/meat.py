from ingredients import Pouch, Ingredients, Units
from recipe import Recipe


def shepherds_pie():
    ingredients = [
        Pouch(Ingredients.LAMB_SHOULDER, 1.5, Units.LB),
        Pouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        Pouch(Ingredients.BUTTER),
        Pouch(Ingredients.ONIONS, 3, Units.CNT),
        Pouch(Ingredients.CARROT, 3, Units.CNT),
        Pouch(Ingredients.CELERY),
        Pouch(Ingredients.CINNAMON, .5, Units.TSP),
        Pouch(Ingredients.THYME, .5, Units.TSP),
        Pouch(Ingredients.ROSEMARY, .5, Units.TSP),
        Pouch(Ingredients.TOMATOE_PUREE, 2, Units.TSP),
        Pouch(Ingredients.KETCHUP, 2, Units.TSP), # ???
        Pouch(Ingredients.RED_WINE, 2, Units.CUP),
        Pouch(Ingredients.FLOUR, 1, Units.OZ),
        Pouch(Ingredients.BEEF_JUS, 14, Units.TBSP),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.BLACK_PEPPER),
        Pouch(Ingredients.WORCESTERSHIRE_SAUCE, 2, Units.TSP),
        Pouch(Ingredients.POTATOES, 2, Units.LB),
        Pouch(Ingredients.BUTTER, 4, Units.OZ),
        Pouch(Ingredients.MILK, 8, Units.TBSP),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.NUTMEG)
    ]

    return Recipe('shepherd\'s pie', ingredients, 1)
