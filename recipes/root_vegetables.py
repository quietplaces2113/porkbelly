from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def potato_sliver_bing():
    ingredients = [
        IngredientPouch(Ingredients.POTATOES, 9, Units.OZ),
        IngredientPouch(Ingredients.SPRING_ONIONS, 3, Units.TBSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.SICHUAN_PEPPER, 0.25, Units.TSP)
    ]

    return Recipe('potato and sliver bing', ingredients, 1)


def stir_fried_mashed_potato_with_preserved_mustard_greens():
    ingredients = [
        IngredientPouch(Ingredients.POTATOES, 12, Units.OZ),
        IngredientPouch(Ingredients.SNOW_VEGETABLE, 2.5, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.WHITE_PEPPER),
        IngredientPouch(Ingredients.SPRING_ONIONS)
    ]

    return Recipe('stir fried mashed potato with preserved mustard greens', ingredients, 1)
