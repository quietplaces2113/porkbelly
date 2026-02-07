from dataclasses import dataclass
from enum import Enum

from units import Units


class Aisles(Enum):
    PRODUCE = 0
    MEAT = 1
    REFRIGERATED = 2
    FROZEN = 3
    SPICES = 4
    PANTRY = 5

    def __str__(self):
        return self.name


@dataclass
class Ingredient:
    ingredient_name: str
    aisle: Aisles


class Ingredients(Enum):
    ARUGULA_LEAVES = Ingredient('arugula leaves', Aisles.PRODUCE)
    CARROT = Ingredient('carrot', Aisles.PRODUCE)
    CELERY = Ingredient('celery', Aisles.PRODUCE)
    CHINESE_BROCCOLI = Ingredient('chinese broccoli', Aisles.PRODUCE)
    CHOY_SUM = Ingredient('choy sum', Aisles.PRODUCE)
    GREEN_BELL_PEPPERS = Ingredient('green bell pepper', Aisles.PRODUCE)
    GARLIC = Ingredient('garlic', Aisles.PRODUCE)
    GINGER = Ingredient('ginger', Aisles.PRODUCE)
    MUSTARD_GREENS = Ingredient('芥菜', Aisles.PRODUCE)
    ONIONS = Ingredient('onions', Aisles.PRODUCE)
    PEA_SHOOTS = Ingredient('pea shoots', Aisles.PRODUCE)
    POTATOES = Ingredient('potatoes', Aisles.PRODUCE)
    RED_CHILLI_PEPPERS = Ingredient('red chilli peppers', Aisles.PRODUCE)
    RED_BELL_PEPPERS = Ingredient('red bell pepper', Aisles.PRODUCE)
    ROSEMARY = Ingredient('rosemary', Aisles.PRODUCE)
    THYME = Ingredient('thyme', Aisles.PRODUCE)
    WATER_SPINACH = Ingredient('water spinach', Aisles.PRODUCE)
    SPRING_ONIONS = Ingredient('spring onions', Aisles.PRODUCE)
    TARO = Ingredient('taro', Aisles.PRODUCE)
    TOMATOES = Ingredient('tomatoes', Aisles.PRODUCE)

    BONELESS_CHICKEN_THIGHS = Ingredient('boneless chicken thighs', Aisles.MEAT)
    CHICKEN = Ingredient('chicken', Aisles.MEAT)
    LAMB_SHOULDER = Ingredient('lamb shoulder', Aisles.MEAT)
    GROUND_BEEF_CHUCK = Ingredient('ground beef chuck', Aisles.MEAT)
    GROUND_PORK = Ingredient('ground pork', Aisles.MEAT)
    PORK_BELLY = Ingredient('pork belly', Aisles.MEAT)
    PORK_RIBS = Ingredient('pork ribs', Aisles.MEAT)
    PORK_TENDERLOIN = Ingredient('pork tenderloin', Aisles.MEAT)
    SEA_BASS = Ingredient('sea bass', Aisles.MEAT)
    SIRLOIN = Ingredient('sirloin', Aisles.MEAT)

    BUTTER = Ingredient('butter', Aisles.REFRIGERATED)
    EGGS = Ingredient('eggs', Aisles.REFRIGERATED)
    FIRM_TOFU = Ingredient('firm tofu', Aisles.REFRIGERATED)
    MILK = Ingredient('milk', Aisles.REFRIGERATED)
    PARMESAN = Ingredient('parmesan', Aisles.REFRIGERATED)
    SILKEN_TOFU = Ingredient('silken tofu', Aisles.REFRIGERATED)

    BEEF_JUS = Ingredient('beef jus', Aisles.SPICES)
    BLACK_PEPPER = Ingredient('black pepper', Aisles.SPICES)
    CASSIA_BARK = Ingredient('cassia bark', Aisles.SPICES)
    CHICKEN_STOCK = Ingredient('chicken stock', Aisles.SPICES)
    CHINKIANG_VINEGAR = Ingredient('chinkiang vinegar', Aisles.SPICES)
    CINNAMON = Ingredient('cinnamon', Aisles.SPICES)
    COOKING_OIL = Ingredient('cooking oil', Aisles.SPICES)
    CUMIN = Ingredient('cumin', Aisles.SPICES)
    DARK_SOY_SAUCE = Ingredient('dark soy sauce', Aisles.SPICES)
    DRIED_CHILLIES = Ingredient('dried chillies', Aisles.SPICES)
    DRIED_CHILLI_FLAKES = Ingredient('dried chilli flakes', Aisles.SPICES)
    DRY_WHITE_WINE = Ingredient('dry white wine', Aisles.SPICES)
    KETCHUP = Ingredient('ketchup', Aisles.SPICES)
    LIGHT_SOY_SAUCE = Ingredient('light soy sauce', Aisles.SPICES)
    NUTMEG = Ingredient('nutmeg', Aisles.SPICES)
    POTATO_FLOUR = Ingredient('potato flour', Aisles.SPICES)
    RED_FERMENTED_TOFU = Ingredient('red fermented tofu', Aisles.SPICES)
    RED_WINE = Ingredient('red wine', Aisles.SPICES)
    SALT = Ingredient('salt', Aisles.SPICES)
    SESAME_OIL = Ingredient('sesame oil', Aisles.SPICES)
    SHAOXING_WINE = Ingredient('shaoxing wine', Aisles.SPICES)
    SICHUAN_PEPPERS = Ingredient('sichuan peppers', Aisles.SPICES)
    STAR_ANISE = Ingredient('star anise', Aisles.SPICES)
    SUGAR = Ingredient('sugar', Aisles.SPICES)
    WHITE_FERMENTED_TOFU = Ingredient('white fermented tofu', Aisles.SPICES)
    WHITE_PEPPER = Ingredient('white pepper', Aisles.SPICES)
    WORCESTERSHIRE_SAUCE = Ingredient('worcestershire sauce', Aisles.SPICES)

    CANNED_PLUM_TOMATOES = Ingredient('canned plum tomatoes', Aisles.PANTRY)
    CHESTNUTS = Ingredient('chestnuts', Aisles.PANTRY)
    DRIED_SHIITAKE_MUSHROOMS = Ingredient('dried shiitake mushrooms', Aisles.PANTRY)
    FLOUR = Ingredient('flour', Aisles.PANTRY)
    PASTA = Ingredient('pasta', Aisles.PANTRY)
    PICKLED_MUSTARD_GREENS = Ingredient('酸菜', Aisles.PANTRY)
    SALTED_DUCK_EGGS = Ingredient('salted duck eggs', Aisles.PANTRY)
    TOMATOE_PUREE = Ingredient('tomato puree', Aisles.PANTRY)

    def __str__(self):
        return self.name


@dataclass
class Pouch:
    ingredient: Ingredients
    amount: float = 1
    unit: Units = Units.RCP
