from dataclasses import dataclass
from enum import Enum

from units import Units


class Aisles(Enum):
    PRODUCE = 0
    MEAT = 1
    REFRIGERATED = 2
    FROZEN = 3
    PANTRY = 4
    OTHER = 5

    def __str__(self):
        return self.name


@dataclass
class Ingredient:
    ingredient_name: str
    aisle: Aisles


class Ingredients(Enum):
    ARUGULA_LEAVES = Ingredient('arugula leaves', Aisles.PRODUCE)
    CHINESE_BROCCOLI = Ingredient('chinese broccoli', Aisles.PRODUCE)
    CHOY_SUM = Ingredient('choy sum', Aisles.PRODUCE)
    GREEN_BELL_PEPPERS = Ingredient('green bell pepper', Aisles.PRODUCE)
    GARLIC = Ingredient('garlic', Aisles.PRODUCE)
    GINGER = Ingredient('ginger', Aisles.PRODUCE)
    POTATOES = Ingredient('potatoes', Aisles.PRODUCE)
    RED_CHILLI_PEPPERS = Ingredient('red chilli peppers', Aisles.PRODUCE)
    RED_BELL_PEPPERS = Ingredient('red bell pepper', Aisles.PRODUCE)
    WATER_SPINACH = Ingredient('water spinach', Aisles.PRODUCE)
    SPRING_ONIONS = Ingredient('spring onions', Aisles.PRODUCE)
    TARO = Ingredient('taro', Aisles.PRODUCE)
    TOMATOES = Ingredient('tomatoes', Aisles.PRODUCE)

    BONELESS_CHICKEN_THIGHS = Ingredient('boneless chicken thighs', Aisles.MEAT)
    CHICKEN = Ingredient('chicken', Aisles.MEAT)
    GROUND_PORK = Ingredient('ground pork', Aisles.MEAT)
    PORK_BELLY = Ingredient('pork belly', Aisles.MEAT)
    PORK_TENDERLOIN = Ingredient('pork tenderloin', Aisles.MEAT)
    SEA_BASS = Ingredient('sea bass', Aisles.MEAT)
    SIRLOIN = Ingredient('sirloin', Aisles.MEAT)

    EGGS = Ingredient('eggs', Aisles.REFRIGERATED)
    FIRM_TOFU = Ingredient('firm tofu', Aisles.REFRIGERATED)
    SILKEN_TOFU = Ingredient('silken tofu', Aisles.REFRIGERATED)

    CASSIA_BARK = Ingredient('cassia bark', Aisles.PANTRY)
    CHESTNUTS = Ingredient('chestnuts', Aisles.PANTRY)
    CHICKEN_STOCK = Ingredient('chicken stock', Aisles.PANTRY)
    CHINKIANG_VINEGAR = Ingredient('chinkiang vinegar', Aisles.PANTRY)
    COOKING_OIL = Ingredient('cooking oil', Aisles.PANTRY)
    CUMIN = Ingredient('cumin', Aisles.PANTRY)
    DARK_SOY_SAUCE = Ingredient('dark soy sauce', Aisles.PANTRY)
    DRIED_CHILLIES = Ingredient('dried chillies', Aisles.PANTRY)
    DRIED_CHILLI_FLAKES = Ingredient('dried chilli flakes', Aisles.PANTRY)
    DRIED_SHIITAKE_MUSHROOMS = Ingredient('dried shiitake mushrooms', Aisles.PANTRY)
    LIGHT_SOY_SAUCE = Ingredient('light soy sauce', Aisles.PANTRY)
    PICKLED_MUSTARD_GREENS = Ingredient('pickled mustard greens', Aisles.PANTRY)
    POTATO_FLOUR = Ingredient('potato flour', Aisles.PANTRY)
    PRESERVED_MUSTARD_GREENS = Ingredient('preserved mustard greens', Aisles.PANTRY)
    SALT = Ingredient('salt', Aisles.PANTRY)
    SALTED_DUCK_EGGS = Ingredient('salted duck eggs', Aisles.PANTRY)
    SESAME_OIL = Ingredient('sesame oil', Aisles.PANTRY)
    SHAOXING_WINE = Ingredient('shaoxing wine', Aisles.PANTRY)
    SICHUAN_PEPPERS = Ingredient('sichuan peppers', Aisles.PANTRY)
    STAR_ANISE = Ingredient('star anise', Aisles.PANTRY)
    SUGAR = Ingredient('sugar', Aisles.PANTRY)
    WHITE_FERMENTED_TOFU = Ingredient('white fermented tofu', Aisles.PANTRY)
    WHITE_PEPPER = Ingredient('white pepper', Aisles.PANTRY)

    def __str__(self):
        return self.name


@dataclass
class Pouch:
    ingredient: Ingredients
    amount: float = 1
    unit: Units = Units.RCP
