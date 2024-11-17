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
    BEANSPROUT = Ingredient('beansprout', Aisles.PRODUCE)
    CELERY_STICKS = Ingredient('celery sticks', Aisles.PRODUCE)
    CHINESE_CHIVE = Ingredient('chinese chive', Aisles.PRODUCE)
    CILANTRO = Ingredient('cilantro', Aisles.PRODUCE)
    GARLIC = Ingredient('garlic', Aisles.PRODUCE)
    GINGER = Ingredient('ginger', Aisles.PRODUCE)
    GREEN_BELL_PEPPER = Ingredient('green bell pepper', Aisles.PRODUCE)
    LILY_BULBS = Ingredient('lily bulbs', Aisles.PRODUCE)
    LOTUS_ROOT = Ingredient('lotus root', Aisles.PRODUCE)
    OYSTER_MUSHROOM = Ingredient('oyster mushroom', Aisles.PRODUCE)
    POTATO = Ingredient('potato', Aisles.PRODUCE)
    RED_BELL_PEPPER = Ingredient('red bell pepper', Aisles.PRODUCE)
    RED_CHILLI_PEPPER = Ingredient('red chilli pepper', Aisles.PRODUCE)
    SMALL_RED_RADISH = Ingredient('small red radish', Aisles.PRODUCE)
    SPRING_ONION = Ingredient('spring onion', Aisles.PRODUCE)

    BEEF_BRISKET = Ingredient('beef brisket', Aisles.MEAT)
    CHICKEN = Ingredient('chicken', Aisles.MEAT)
    CHICKEN_BREAST = Ingredient('chicken breast', Aisles.MEAT)
    CLAM = Ingredient('clam', Aisles.MEAT)
    OYSTER = Ingredient('oyster', Aisles.MEAT)

    EGG = Ingredient('egg', Aisles.REFRIGERATED)
    SILKEN_TOFU = Ingredient('silken tofu', Aisles.REFRIGERATED)

    SOY_BEAN = Ingredient('soy bean', Aisles.FROZEN)

    BOMBAY_MIX = Ingredient('bombay mix', Aisles.PANTRY)
    CHICKEN_STOCK = Ingredient('chicken stock', Aisles. PANTRY)
    CHILLI_OIL = Ingredient('chilli oil', Aisles.PANTRY)
    CHINKIANG_VINEGAR = Ingredient('chinkiang vinegar', Aisles.PANTRY)
    CLEAR_RICE_VINEGAR = Ingredient('clear rice vinegar', Aisles.PANTRY)
    COOKING_OIL = Ingredient('cooking oil', Aisles.PANTRY)
    DARK_SOY_SAUCE = Ingredient('dark soy sauce', Aisles.PANTRY)
    DRIED_SHRIMP = Ingredient('dried shrimp', Aisles.PANTRY)
    FERMENTED_BLACK_BEANS = Ingredient('fermented black beans', Aisles.PANTRY)
    GOUQI_BERRY = Ingredient('gouqi berry', Aisles.PANTRY)
    LIGHT_SOY_SAUCE = Ingredient('light soy sauce', Aisles.PANTRY)
    MACADAMIA_NUTS = Ingredient('macadamia nuts', Aisles.PANTRY)
    POTATO_FLOUR = Ingredient('potato flour', Aisles.PANTRY)
    SALT = Ingredient('salt', Aisles.PANTRY)
    SESAME_OIL = Ingredient('sesame oil', Aisles.PANTRY)
    SHAOXING_WINE = Ingredient('shaoxing wine', Aisles.PANTRY)
    SICHUAN_CHILLI_BEAN_PASTE = Ingredient('sichuan chilli bean paste', Aisles.PANTRY)
    SICHUAN_PEPPER = Ingredient('sichuan pepper', Aisles.PANTRY)
    SICHUAN_PRESERVED_VEGETABLE = Ingredient('sichuan preserved vegetable', Aisles.PANTRY)
    SUGAR = Ingredient('sugar', Aisles.PANTRY)
    WHITE_PEPPER = Ingredient('white pepper', Aisles.PANTRY)
    WOOD_EAR_MUSHROOM = Ingredient('wood ear mushroom', Aisles.PANTRY)

    def __str__(self):
        return self.name


@dataclass
class IngredientPouch:
    ingredient: Ingredients
    amount: float = 1
    unit: Units = Units.RCP
