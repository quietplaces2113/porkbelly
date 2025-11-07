import random

from chinese.meat import red_braised_pork
from chinese.chinese import hun, shu, soups
from shopping_list import ShoppingList

if __name__ == '__main__':
    random.seed(0000)
    recipes = red_braised_pork()

    print('selected chinese:')
    for recipe in recipes:
        print(recipe.recipe_name)

    print('---')

    shopping_list = ShoppingList()

    for recipe in recipes:
        shopping_list.add_recipe(recipe)

    shopping_list.print()
