from recipes.beans_and_peas import stir_fried_beansprouts_with_chinese_chives
from recipes.chicken_and_eggs import oyster_omelette
from recipes.cold_dishes import green_soy_beans
from recipes.cold_dishes import lotus_root_salad
from recipes.cold_dishes import radishes_in_chilli_oil_sauce
from recipes.fish_and_seafood import clams_in_black_bean_sauce
from recipes.leafy_greens import \
    stir_fried_beansprouts_with_chinese_chives
from recipes.meat import slow_cooked_beef_brisket_with_berries
from recipes.mushrooms import stir_fried_oyster_mushrooms_with_chicken
from recipes.root_vegetables import potato_sliver_bing
from recipes.soups import chicken_soup
from recipes.tofu import sour_and_hot_silken_tofu


def cold_dish():
    return [
        green_soy_beans(),
        lotus_root_salad(),
        radishes_in_chilli_oil_sauce()
    ]


def tofu():
    return [
        sour_and_hot_silken_tofu()
    ]


def meat():
    return [
        slow_cooked_beef_brisket_with_berries()
    ]


def chicken_and_eggs():
    return [
        oyster_omelette()
    ]


def fish_and_seafood():
    return [
        clams_in_black_bean_sauce()
    ]


def beans_and_peas():
    return [
        stir_fried_beansprouts_with_chinese_chives()
    ]


def leafy_greens():
    return [
        stir_fried_beansprouts_with_chinese_chives()
    ]


def root_vegetables():
    return [
        potato_sliver_bing()
    ]


def mushrooms():
    return [
        stir_fried_oyster_mushrooms_with_chicken()
    ]


def soups():
    return [
        chicken_soup()
    ]


def hun():
    return tofu() + meat() + chicken_and_eggs() + fish_and_seafood()


def shu():
    return beans_and_peas() + leafy_greens() + root_vegetables() + mushrooms()
