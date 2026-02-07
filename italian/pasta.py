from ingredients import Pouch, Ingredients
from recipe import Recipe
from units import Units


# +1
def tomato_sauce_with_onion_and_butter():
    ingredients = [
        Pouch(Ingredients.CANNED_PLUM_TOMATOES, 2, Units.CNT),
        Pouch(Ingredients.BUTTER, 5, Units.TBSP),
        Pouch(Ingredients.ONIONS, 1, Units.CNT),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.PASTA, 1, Units.LB),
        Pouch(Ingredients.PARMESAN)
    ]

    return Recipe("tomato sauce with onion and butter", ingredients, 1)

def bolognese_meat_sauce():
    ingredients = [
        Pouch(Ingredients.COOKING_OIL, 1, Units.TBSP),
        Pouch(Ingredients.BUTTER, 3, Units.TBSP),
        Pouch(Ingredients.ONIONS, .5, Units.CNT),
        Pouch(Ingredients.CELERY, .66, Units.CUP),
        Pouch(Ingredients.CARROT, .66, Units.CUP),
        Pouch(Ingredients.GROUND_BEEF_CHUCK, .75, Units.LB),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.BLACK_PEPPER),
        Pouch(Ingredients.MILK, 1, Units.CUP),
        Pouch(Ingredients.NUTMEG, 1, Units.CNT),
        Pouch(Ingredients.DRY_WHITE_WINE, 1, Units.CUP),
        Pouch(Ingredients.CANNED_PLUM_TOMATOES),
        Pouch(Ingredients.PASTA, 1.5, Units.LB)
    ]

    return  Recipe("bolognese meat sauce", ingredients, 1)
