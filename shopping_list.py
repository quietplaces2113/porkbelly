from collections import defaultdict

from ingredients import IngredientPouch
from recipe import Recipe


class ShoppingList:
    def __init__(self):
        self.ingredients = defaultdict(lambda: defaultdict(float))

    def add_recipe(self, recipe: Recipe):
        for ingredient_pouch in recipe.ingredients:
            self.ingredients[ingredient_pouch.ingredient][ingredient_pouch.unit] += ingredient_pouch.amount

    def print(self):
        print('shopping list:')

        ingredients_by_aisle = defaultdict(list)

        for ingredient, v in self.ingredients.items():
            for unit, amount in v.items():
                ingredients_by_aisle[ingredient.value.aisle].append(IngredientPouch(ingredient, amount, unit))

        for aisle, ingredients in ingredients_by_aisle.items():
            print('\n{}\n'.format(aisle))

            for ingredient_pouch in ingredients:
                print('{ingredient} - {amount} {unit}'.format(
                    ingredient=ingredient_pouch.ingredient, amount=ingredient_pouch.amount, unit=ingredient_pouch.unit))
