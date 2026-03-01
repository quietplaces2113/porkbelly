from ingredients import Ingredients
from recipe import Recipe


def stir_fried_potato_slivers_with_chilli_and_sichuan_pepper():
    ingredients = [
        Ingredients.DRIED_CHILLIES,
        Ingredients.POTATOES,
        Ingredients.SALT,
        Ingredients.COOKING_OIL,
        Ingredients.SICHUAN_PEPPERS,
        Ingredients.SESAME_OIL,
    ]

    return Recipe('stir fried potato slivers with chilli and sichuan pepper', ingredients)
