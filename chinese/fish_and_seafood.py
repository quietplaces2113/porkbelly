from ingredients import Ingredients, Pouch
from recipe import Recipe
from units import Units


# +1
def steamed_sea_bass_with_ginger_and_spring_onion():
    ingredients = [
        Pouch(Ingredients.SPRING_ONIONS, 5, Units.CNT),
        Pouch(Ingredients.GINGER, 2, Units.OZ),
        Pouch(Ingredients.SEA_BASS, 1.5, Units.LB),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        Pouch(Ingredients.LIGHT_SOY_SAUCE, 3, Units.TBSP),
        Pouch(Ingredients.COOKING_OIL, 4, Units.TBSP)
    ]

    return Recipe('steamed sea bass with ginger and spring onion', ingredients, 1)
