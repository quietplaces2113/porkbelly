from ingredients import Ingredients
from recipe import Recipe


# +1
def tomato_sauce_with_onion_and_butter():
    ingredients = [
        Ingredients.CANNED_PLUM_TOMATOES,
        Ingredients.BUTTER,
        Ingredients.ONIONS,
        Ingredients.SALT,
        Ingredients.PASTA,
        Ingredients.PARMESAN
    ]

    return Recipe("tomato sauce with onion and butter", ingredients)


def bolognese_meat_sauce():
    ingredients = [
        Ingredients.COOKING_OIL,
        Ingredients.BUTTER,
        Ingredients.ONIONS,
        Ingredients.CELERY,
        Ingredients.CARROT,
        Ingredients.GROUND_BEEF_CHUCK,
        Ingredients.SALT,
        Ingredients.BLACK_PEPPER,
        Ingredients.MILK,
        Ingredients.NUTMEG,
        Ingredients.DRY_WHITE_WINE,
        Ingredients.CANNED_PLUM_TOMATOES,
        Ingredients.PASTA
    ]

    return Recipe("bolognese meat sauce", ingredients)
