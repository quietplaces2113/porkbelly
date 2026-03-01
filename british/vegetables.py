from ingredients import Ingredients
from recipe import Recipe

def egg_and_bacon_salad():
    ingredients = [
        Ingredients.BREAD,
        Ingredients.EGGS,
        Ingredients.BACON,
        Ingredients.LETTUCE,
        Ingredients.RED_WINE_VINEGAR,
        Ingredients.OLIVE_OIL,
        Ingredients.SPRING_ONIONS,
        Ingredients.SALT,
        Ingredients.BLACK_PEPPER
    ]

    return Recipe('egg and bacon salad', ingredients)
