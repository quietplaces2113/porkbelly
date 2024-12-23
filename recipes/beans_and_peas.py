from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def stir_fried_beansprouts_with_chinese_chives():
    ingredients = [
        IngredientPouch(Ingredients.CHINESE_CHIVES, 4.25, Units.OZ),
        IngredientPouch(Ingredients.BEANSPROUTS, 4, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.RED_BELL_PEPPERS),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.CHINKIANG_VINEGAR, 1, Units.TSP)
    ]

    return Recipe('stir fried beansprouts with chinese chives', ingredients, 1)


def stir_fried_green_soy_beans_with_snow_vegetable():
    ingredients = [
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.SOY_BEANS, 9, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.DRIED_CHILLIES, 5, Units.CNT),
        IngredientPouch(Ingredients.SICHUAN_PEPPER, 0.5, Units.TSP),
        IngredientPouch(Ingredients.SNOW_VEGETABLE, 2, Units.OZ),
        IngredientPouch(Ingredients.SESAME_OIL, 0.5, Units.TSP),
    ]

    return Recipe('stir fried green soy beans with snow vegetable', ingredients, 1)
