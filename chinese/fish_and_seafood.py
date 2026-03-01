from ingredients import Ingredients
from recipe import Recipe


# +1
def steamed_sea_bass_with_ginger_and_spring_onion():
    ingredients = [
        Ingredients.SPRING_ONIONS,
        Ingredients.GINGER,
        Ingredients.SEA_BASS,
        Ingredients.SALT,
        Ingredients.SHAOXING_WINE,
        Ingredients.LIGHT_SOY_SAUCE,
        Ingredients.COOKING_OIL
    ]

    return Recipe('steamed sea bass with ginger and spring onion', ingredients)
