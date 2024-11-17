from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def stir_fried_oyster_mushrooms_with_chicken():
    ingredients = [
        IngredientPouch(Ingredients.CHICKEN_BREAST, 5, Units.OZ),
        IngredientPouch(Ingredients.SPRING_ONION, 1, Units.CNT),
        IngredientPouch(Ingredients.OYSTER_MUSHROOM, 7, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.GINGER),
        IngredientPouch(Ingredients.GARLIC),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.WHITE_PEPPER),
        IngredientPouch(Ingredients.SHAOXING_WINE, 1, Units.TSP),
        IngredientPouch(Ingredients.POTATO_FLOUR, 1, Units.TSP)
    ]

    recipe = Recipe('stir fried oyster mushrooms with chicken', ingredients, 1)
    return recipe
