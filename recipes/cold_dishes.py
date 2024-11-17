from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def green_soy_beans():
    ingredients = [
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.GINGER, 0.5, Units.OZ),
        IngredientPouch(Ingredients.SICHUAN_PEPPER),
        IngredientPouch(Ingredients.SOY_BEAN, 11, Units.OZ)
    ]

    recipe = Recipe('green soy beans', ingredients, 1)
    return recipe


def lotus_root_salad():
    ingredients = [
        IngredientPouch(Ingredients.DRIED_SHRIMP, 1, Units.TBSP),
        IngredientPouch(Ingredients.WOOD_EAR_MUSHROOM),
        IngredientPouch(Ingredients.LOTUS_ROOT, 7, Units.OZ),
        IngredientPouch(Ingredients.GINGER, 1, Units.TSP),
        IngredientPouch(Ingredients.CLEAR_RICE_VINEGAR, 2.5, Units.TSP),
        IngredientPouch(Ingredients.SUGAR, 1, Units.TSP),
        IngredientPouch(Ingredients.RED_CHILLI_PEPPER),
        IngredientPouch(Ingredients.SPRING_ONION, 1, Units.CNT),
        IngredientPouch(Ingredients.SESAME_OIL, 1, Units.TSP),
        IngredientPouch(Ingredients.SALT),
    ]

    recipe = Recipe('lotus root salad', ingredients, 1)
    return recipe


def radishes_in_chilli_oil_sauce():
    ingredients = [
        IngredientPouch(Ingredients.SMALL_RED_RADISH),
        IngredientPouch(Ingredients.SALT, 0.75, Units.TSP),
        IngredientPouch(Ingredients.SUGAR, 1, Units.TSP),
        IngredientPouch(Ingredients.LIGHT_SOY_SAUCE, 2, Units.TBSP),
        IngredientPouch(Ingredients.CHILLI_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.SESAME_OIL, 0.5, Units.TSP),
    ]

    recipe = Recipe('radishes in chilli oil sauce', ingredients, 1)
    return recipe
