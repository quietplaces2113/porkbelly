from collections import defaultdict

from recipe import Recipe


class ShoppingList:
    def __init__(self):
        self.ingredients = set()

    def add_recipe(self, recipe: Recipe):
        self.ingredients.update(recipe.ingredients)

    def print(self):
        print('shopping list:')

        ingredients_by_aisle = defaultdict(list)

        for ingredient in self.ingredients:
            ingredients_by_aisle[ingredient.value.aisle].append(ingredient)

        for aisle, ingredients in ingredients_by_aisle.items():
            print('\n{}\n'.format(aisle))

            for ingredient in ingredients:
                print('{}'.format(ingredient))
