from ingredients import IngredientPouch, Ingredients, Units
from recipe import Recipe


def slow_cooked_beef_brisket_with_berries():
    ingredients = [
        IngredientPouch(Ingredients.BEEF_BRISKET, 1.5, Units.LB),
        IngredientPouch(Ingredients.GINGER, 2, Units.OZ),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 5.25, Units.CUP),
        IngredientPouch(Ingredients.SHAOXING_WINE, 0.33, Units.CUP),
        IngredientPouch(Ingredients.SICHUAN_PEPPER, 1, Units.TSP),
        IngredientPouch(Ingredients.GOUQI_BERRIES, 2, Units.TBSP),
        IngredientPouch(Ingredients.CILANTRO),
        IngredientPouch(Ingredients.COOKING_OIL, 1, Units.TBSP),
        IngredientPouch(Ingredients.SICHUAN_CHILLI_BEAN_PASTE, 4, Units.TBSP),
        IngredientPouch(Ingredients.GINGER, 2, Units.TSP),
        IngredientPouch(Ingredients.SESAME_OIL, 1, Units.TSP),
    ]

    return Recipe('slow cooked beef brisket with berries', ingredients, 1)


def red_braised_beef_with_tofu_bamboo():
    ingredients = [
        IngredientPouch(Ingredients.STEWING_BEEF),
        IngredientPouch(Ingredients.COOKING_OIL, 2, Units.TBSP),
        IngredientPouch(Ingredients.SICHUAN_CHILLI_BEAN_PASTE, 2.5, Units.TBSP),
        IngredientPouch(Ingredients.GINGER, 0.5, Units.OZ),
        IngredientPouch(Ingredients.SPRING_ONIONS, 2, Units.CNT),
        IngredientPouch(Ingredients.STAR_ANISE, 1, Units.CNT),
        IngredientPouch(Ingredients.SWEET_FERMENTED_SAUCE, 1.5, Units.TSP),
        IngredientPouch(Ingredients.CHICKEN_STOCK, 3, Units.CUP),
        IngredientPouch(Ingredients.SHAOXING_WINE, 2, Units.TBSP),
        IngredientPouch(Ingredients.TOFU_BAMBOO, 2, Units.CNT)
    ]

    return Recipe('red braised beef with tofu bamboo', ingredients, 1)
