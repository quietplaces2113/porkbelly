import random

from british.meat import shepherds_pie
from chinese.fish_and_seafood import steamed_sea_bass_with_ginger_and_spring_onion
from chinese.leafy_greens import pea_shoots
from shopping_list import ShoppingList

if __name__ == '__main__':
    random.seed(0000)
    recipes = [pea_shoots(), steamed_sea_bass_with_ginger_and_spring_onion(), shepherds_pie()]

    print('selected recipes:')
    for recipe in recipes:
        print(recipe.recipe_name)

    print('---')

    shopping_list = ShoppingList()

    for recipe in recipes:
        shopping_list.add_recipe(recipe)

    shopping_list.print()
