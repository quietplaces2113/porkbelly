from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def stir_fried_oyster_mushrooms_with_chicken():
    ingredients = [
        IngredientPouch(Ingredients.CHICKEN_BREAST, 5, Units.OZ),
        IngredientPouch(Ingredients.SPRING_ONIONS, 1, Units.CNT),
        IngredientPouch(Ingredients.OYSTER_MUSHROOMS, 7, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.GINGER),
        IngredientPouch(Ingredients.GARLIC),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.WHITE_PEPPER),
        IngredientPouch(Ingredients.SHAOXING_WINE, 1, Units.TSP),
        IngredientPouch(Ingredients.POTATO_FLOUR, 1, Units.TSP)
    ]

    return Recipe('stir fried oyster mushrooms with chicken', ingredients, 1)


def stir_fried_oyster_and_shiitake_mushrooms_with_garlic():
    ingredients = [
        IngredientPouch(Ingredients.OYSTER_MUSHROOMS, 10, Units.OZ),
        IngredientPouch(Ingredients.SHIITAKE_MUSHROOMS, 5, Units.OZ),
        IngredientPouch(Ingredients.COOKING_OIL, 3, Units.TBSP),
        IngredientPouch(Ingredients.GARLIC),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 0.75, Units.CUP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.SPRING_ONIONS, 2, Units.CNT)
    ]

    return Recipe('stir fried oyster and shiitake mushrooms with garlic', ingredients, 1)
