import random

from chinese.leafy_greens import chinese_broccoli_in_ginger_sauce
from chinese.meat import slow_cooked_ribs_with_red_fermented_tofu
from italian.meat import oven_roasted_chicken_with_garlic_and_rosemary
from shopping_list import ShoppingList

if __name__ == '__main__':
    random.seed(0000)
    recipes = [chinese_broccoli_in_ginger_sauce(), slow_cooked_ribs_with_red_fermented_tofu(), oven_roasted_chicken_with_garlic_and_rosemary()]

    print('selected chinese:')
    for recipe in recipes:
        print(recipe.recipe_name)

    print('---')

    shopping_list = ShoppingList()

    for recipe in recipes:
        shopping_list.add_recipe(recipe)

    shopping_list.print()
