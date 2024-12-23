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
    BEANSPROUTS = Ingredient('beansprouts', Aisles.PRODUCE)
    CELERY_STICKS = Ingredient('celery sticks', Aisles.PRODUCE)
    CHINESE_CHIVES = Ingredient('chinese chives', Aisles.PRODUCE)
    CILANTRO = Ingredient('cilantro', Aisles.PRODUCE)
    GARLIC = Ingredient('garlic', Aisles.PRODUCE)
    GINGER = Ingredient('ginger', Aisles.PRODUCE)
    GREEN_BELL_PEPPERS = Ingredient('green bell peppers', Aisles.PRODUCE)
    LILY_BULBS = Ingredient('lily bulbs', Aisles.PRODUCE)
    LOTUS_ROOT = Ingredient('lotus root', Aisles.PRODUCE)
    OYSTER_MUSHROOMS = Ingredient('oyster mushrooms', Aisles.PRODUCE)
    POTATOES = Ingredient('potatoes', Aisles.PRODUCE)
    RED_BELL_PEPPERS = Ingredient('red bell peppers', Aisles.PRODUCE)
    RED_CHILLI_PEPPERS = Ingredient('red chilli peppers', Aisles.PRODUCE)
    SHIITAKE_MUSHROOMS = Ingredient('shiitake mushrooms', Aisles.PRODUCE)
    SMALL_RED_RADISHES = Ingredient('small red radishes', Aisles.PRODUCE)
    SPRING_ONIONS = Ingredient('spring onions', Aisles.PRODUCE)
    TARO = Ingredient('taro', Aisles.PRODUCE)

    BEEF_BRISKET = Ingredient('beef brisket', Aisles.MEAT)
    CHICKEN = Ingredient('chicken', Aisles.MEAT)
    CHICKEN_BREAST = Ingredient('chicken breast', Aisles.MEAT)
    CLAMS = Ingredient('clams', Aisles.MEAT)
    GROUND_BEEF = Ingredient('ground beef', Aisles.MEAT)
    GROUND_PORK = Ingredient('ground pork', Aisles.MEAT)
    OYSTERS = Ingredient('oysters', Aisles.MEAT)
    SQUID = Ingredient('squid', Aisles.MEAT)
    STEWING_BEEF = Ingredient('stewing beef', Aisles.MEAT)

    EGGS = Ingredient('eggs', Aisles.REFRIGERATED)
    SILKEN_TOFU = Ingredient('silken tofu', Aisles.REFRIGERATED)

    SOY_BEANS = Ingredient('soy beans', Aisles.FROZEN)

    BOMBAY_MIX = Ingredient('bombay mix', Aisles.PANTRY)
    CHICKEN_STOCK = Ingredient('chicken stock', Aisles. PANTRY)
    CHILLI_OIL = Ingredient('chilli oil', Aisles.PANTRY)
    CHINKIANG_VINEGAR = Ingredient('chinkiang vinegar', Aisles.PANTRY)
    CLEAR_RICE_VINEGAR = Ingredient('clear rice vinegar', Aisles.PANTRY)
    COOKING_OIL = Ingredient('cooking oil', Aisles.PANTRY)
    DARK_SOY_SAUCE = Ingredient('dark soy sauce', Aisles.PANTRY)
    DRIED_CHILLIES = Ingredient('dried chillies', Aisles.PANTRY)
    DRIED_SHIITAKE_MUSHROOMS = Ingredient('dried shiitake mushrooms', Aisles.PANTRY)
    DRIED_SHRIMP = Ingredient('dried shrimp', Aisles.PANTRY)
    FERMENTED_BLACK_BEANS = Ingredient('fermented black beans', Aisles.PANTRY)
    GOUQI_BERRIES = Ingredient('gouqi berries', Aisles.PANTRY)
    LIGHT_SOY_SAUCE = Ingredient('light soy sauce', Aisles.PANTRY)
    MACADAMIA_NUTS = Ingredient('macadamia nuts', Aisles.PANTRY)
    PICKLED_MUSTARD_GREENS = Ingredient('pickled mustard greens', Aisles.PANTRY)
    POTATO_FLOUR = Ingredient('potato flour', Aisles.PANTRY)
    SALT = Ingredient('salt', Aisles.PANTRY)
    SESAME_OIL = Ingredient('sesame oil', Aisles.PANTRY)
    SHAOXING_WINE = Ingredient('shaoxing wine', Aisles.PANTRY)
    SICHUAN_CHILLI_BEAN_PASTE = Ingredient('sichuan chilli bean paste', Aisles.PANTRY)
    SICHUAN_PEPPER = Ingredient('sichuan pepper', Aisles.PANTRY)
    SICHUAN_PRESERVED_VEGETABLE = Ingredient('sichuan preserved vegetable', Aisles.PANTRY)
    SNOW_VEGETABLE = Ingredient('snow vegetable', Aisles.PANTRY)
    STAR_ANISE = Ingredient('star anise', Aisles.PANTRY)
    SUGAR = Ingredient('sugar', Aisles.PANTRY)
    SWEET_FERMENTED_SAUCE = Ingredient('sweet fermented sauce', Aisles.PANTRY)
    TOFU_BAMBOO = Ingredient('tofu bamboo', Aisles.PANTRY)
    WHITE_PEPPER = Ingredient('white pepper', Aisles.PANTRY)
    WOOD_EAR_MUSHROOMS = Ingredient('wood ear mushrooms', Aisles.PANTRY)

    def __str__(self):
        return self.name


@dataclass
class IngredientPouch:
    ingredient: Ingredients
    amount: float = 1
    unit: Units = Units.RCP
