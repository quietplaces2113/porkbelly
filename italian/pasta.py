from ingredients import Pouch, Ingredients
from recipe import Recipe
from units import Units


# +1
def tomato_sauce_with_onion_and_butter():
    ingredients = [
        Pouch(Ingredients.TOMATOES, 2, Units.CNT),
        Pouch(Ingredients.BUTTER, 5, Units.TBSP),
        Pouch(Ingredients.ONIONS, 1, Units.CNT),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.PASTA, 1, Units.LB),
        Pouch(Ingredients.PARMESAN)
    ]

    return Recipe("tomato sauce with onion and butter", ingredients, 1)
