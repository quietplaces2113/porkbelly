from ingredients import Ingredients
from recipe import Recipe


def red_braised_pork():
    ingredients = [
        Ingredients.PORK_BELLY,
        Ingredients.COOKING_OIL,
        Ingredients.GINGER,
        Ingredients.SPRING_ONIONS,
        Ingredients.SHAOXING_WINE,
        Ingredients.CHICKEN_STOCK,
        Ingredients.STAR_ANISE,
        Ingredients.CASSIA_BARK,
        Ingredients.DARK_SOY_SAUCE,
        Ingredients.SUGAR,
        Ingredients.SALT,
    ]

    return Recipe('red braised pork', ingredients)


def beef_with_cumin():
    ingredients = [
        Ingredients.SIRLOIN,
        Ingredients.RED_BELL_PEPPERS,
        Ingredients.GREEN_BELL_PEPPERS,
        Ingredients.COOKING_OIL,
        Ingredients.GINGER,
        Ingredients.GARLIC,
        Ingredients.RED_CHILLI_PEPPERS,
        Ingredients.CUMIN,
        Ingredients.DRIED_CHILLI_FLAKES,
        Ingredients.SPRING_ONIONS,
        Ingredients.SESAME_OIL
    ]

    return Recipe('beef with cumin', ingredients)
