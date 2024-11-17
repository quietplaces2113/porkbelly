from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def chicken_soup():
    ingredients = [
        IngredientPouch(Ingredients.CHICKEN, 1, Units.CNT),
        IngredientPouch(Ingredients.GINGER, 0.5, Units.OZ),
        IngredientPouch(Ingredients.SPRING_ONION, 2, Units.CNT),
        IngredientPouch(Ingredients.SHAOXING_WINE, 1, Units.TBSP),
        IngredientPouch(Ingredients.SALT),
        IngredientPouch(Ingredients.WHITE_PEPPER)
    ]

    return Recipe('chicken soup', ingredients, 1)
