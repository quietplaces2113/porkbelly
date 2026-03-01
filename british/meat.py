from ingredients import Ingredients
from recipe import Recipe


def shepherds_pie():
    ingredients = [
        Ingredients.LAMB_SHOULDER,
        Ingredients.COOKING_OIL,
        Ingredients.BUTTER,
        Ingredients.ONIONS,
        Ingredients.CARROT,
        Ingredients.CELERY,
        Ingredients.CINNAMON,
        Ingredients.THYME,
        Ingredients.ROSEMARY,
        Ingredients.TOMATOE_PUREE,
        Ingredients.KETCHUP, # ???
        Ingredients.RED_WINE,
        Ingredients.FLOUR,
        Ingredients.BEEF_JUS,
        Ingredients.SALT,
        Ingredients.BLACK_PEPPER,
        Ingredients.WORCESTERSHIRE_SAUCE,
        Ingredients.POTATOES,
        Ingredients.BUTTER,
        Ingredients.MILK,
        Ingredients.SALT,
        Ingredients.NUTMEG
    ]

    return Recipe('shepherd\'s pie', ingredients)
