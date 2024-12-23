from recipes.beans_and_peas import stir_fried_beansprouts_with_chinese_chives, \
    stir_fried_green_soy_beans_with_snow_vegetable
from recipes.chicken_and_eggs import oyster_omelette, steamed_eggs
from recipes.cold_dishes import green_soy_beans
from recipes.cold_dishes import lotus_root_salad
from recipes.cold_dishes import radishes_in_chilli_oil_sauce
from recipes.fish_and_seafood import clams_in_black_bean_sauce, salt_and_pepper_squid
from recipes.leafy_greens import \
    stir_fried_celery_with_lily_bulbs_and_macadamia_nuts, chopped_celery_with_ground_beef
from recipes.meat import slow_cooked_beef_brisket_with_berries, red_braised_beef_with_tofu_bamboo
from recipes.mushrooms import stir_fried_oyster_mushrooms_with_chicken, \
    stir_fried_oyster_and_shiitake_mushrooms_with_garlic
from recipes.root_vegetables import potato_sliver_bing, stir_fried_mashed_potato_with_preserved_mustard_greens
from recipes.soups import chicken_soup, taro_and_arugula_soup
from recipes.tofu import sour_and_hot_silken_tofu, silken_tofu_with_pickled_mustard_greens


def cold_dish():
    return [
        green_soy_beans(),
        lotus_root_salad(),
        radishes_in_chilli_oil_sauce()
    ]


def tofu():
    return [
        sour_and_hot_silken_tofu(),
        silken_tofu_with_pickled_mustard_greens()
    ]


def meat():
    return [
        slow_cooked_beef_brisket_with_berries(),
        red_braised_beef_with_tofu_bamboo()
    ]


def chicken_and_eggs():
    return [
        oyster_omelette(),
        steamed_eggs()
    ]


def fish_and_seafood():
    return [
        clams_in_black_bean_sauce(),
        salt_and_pepper_squid()
    ]


def beans_and_peas():
    return [
        stir_fried_beansprouts_with_chinese_chives(),
        stir_fried_green_soy_beans_with_snow_vegetable()
    ]


def leafy_greens():
    return [
        stir_fried_celery_with_lily_bulbs_and_macadamia_nuts(),
        chopped_celery_with_ground_beef()
    ]


def root_vegetables():
    return [
        potato_sliver_bing(),
        stir_fried_mashed_potato_with_preserved_mustard_greens()
    ]


def mushrooms():
    return [
        stir_fried_oyster_mushrooms_with_chicken(),
        stir_fried_oyster_and_shiitake_mushrooms_with_garlic()
    ]


def soups():
    return [
        chicken_soup(),
        taro_and_arugula_soup()
    ]


def hun():
    return tofu() + meat() + chicken_and_eggs() + fish_and_seafood()


def shu():
    return beans_and_peas() + leafy_greens() + root_vegetables() + mushrooms()
