import random

from recipes.recipe_book import cold_dish, hun, shu, soups
from shopping_list import ShoppingList

if __name__ == '__main__':
    random.seed(1222)
    recipes = random.sample(cold_dish(), 1) + random.sample(hun(), 2) + random.sample(shu(), 2) + random.sample(soups(), 1)

    print('selected recipes:')
    for recipe in recipes:
        print(recipe.recipe_name)

    print('---')

    shopping_list = ShoppingList()

    for recipe in recipes:
        shopping_list.add_recipe(recipe)

    shopping_list.print()
