from ingredients import Pouch, Ingredients, Units
from recipe import Recipe


def stir_fried_potato_slivers_with_chilli_and_sichuan_pepper():
    ingredients = [
        Pouch(Ingredients.DRIED_CHILLIES, 4, Units.CNT),
        Pouch(Ingredients.POTATOES, 14, Units.OZ),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        Pouch(Ingredients.SICHUAN_PEPPERS, .5, Units.TSP),
        Pouch(Ingredients.SESAME_OIL, .5, Units.TSP)
    ]

    return Recipe('stir fried potato slivers with chilli and sichuan pepper', ingredients, 1)
