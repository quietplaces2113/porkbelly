import random

from recipes.recipe_book import hun, shu, soups
from shopping_list import ShoppingList

if __name__ == '__main__':
    random.seed(0000)
    recipes = random.sample(hun(), 3) + random.sample(shu(), 3) + random.sample(soups(), 1)

    print('selected recipes:')
    for recipe in recipes:
        print(recipe.recipe_name)

    print('---')

    shopping_list = ShoppingList()

    for recipe in recipes:
        shopping_list.add_recipe(recipe)

    shopping_list.print()
