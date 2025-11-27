from ingredients import Pouch, Ingredients, Units
from recipe import Recipe


def red_braised_pork():
    ingredients = [
        Pouch(Ingredients.PORK_BELLY, 1.25, Units.LB),
        Pouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        Pouch(Ingredients.GINGER),
        Pouch(Ingredients.SPRING_ONIONS, 1, Units.CNT),
        Pouch(Ingredients.SHAOXING_WINE, 2, Units.TBSP),
        Pouch(Ingredients.CHICKEN_STOCK, 2, Units.CUP),
        Pouch(Ingredients.CHICKEN_STOCK, 2, Units.TBSP),
        Pouch(Ingredients.STAR_ANISE, 1, Units.CNT),
        Pouch(Ingredients.CASSIA_BARK),
        Pouch(Ingredients.DARK_SOY_SAUCE),
        Pouch(Ingredients.SUGAR, 2, Units.TBSP),
        Pouch(Ingredients.SALT),
        Pouch(Ingredients.SPRING_ONIONS)
    ]

    return Recipe('red braised pork', ingredients, 1)


def beef_with_cumin():
    ingredients = [
        Pouch(Ingredients.SIRLOIN, 9, Units.OZ),
        Pouch(Ingredients.RED_BELL_PEPPERS, .5, Units.CNT),
        Pouch(Ingredients.GREEN_BELL_PEPPERS, .5, Units.CNT),
        Pouch(Ingredients.COOKING_OIL, 4, Units.TBSP),
        Pouch(Ingredients.GINGER, 1.5, Units.TSP),
        Pouch(Ingredients.GARLIC, 2, Units.TSP),
        Pouch(Ingredients.RED_CHILLI_PEPPERS, 1, Units.CNT),
        Pouch(Ingredients.CUMIN, 2, Units.TSP),
        Pouch(Ingredients.DRIED_CHILLI_FLAKES, 2, Units.TSP),
        Pouch(Ingredients.SPRING_ONIONS, 2, Units.CNT),
        Pouch(Ingredients.SESAME_OIL, 1, Units.TSP)
    ]

    return Recipe('beef with cumin', ingredients, 1)


def slow_cooked_ribs_with_red_fermented_tofu():
    ingredients = [
        Pouch(Ingredients.PORK_RIBS, 1.5, Units.LB),
        Pouch(Ingredients.SHAOXING_WINE, .5, Units.CUP),
        Pouch(Ingredients.WHITE_FERMENTED_TOFU, 2, Units.OZ),
        Pouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        Pouch(Ingredients.GINGER, .5, Units.OZ),
        Pouch(Ingredients.SPRING_ONIONS, 2, Units.CNT),
        Pouch(Ingredients.SUGAR, 1, Units.TBSP),
    ]

    return Recipe('slow cooked ribs with red fermented tofu', ingredients, 1)
