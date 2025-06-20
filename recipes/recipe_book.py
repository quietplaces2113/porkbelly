from recipes.chicken_and_eggs import steamed_eggs, braised_chicken_with_chestnuts, stir_fried_eggs_with_tomatoes
from recipes.fish_and_seafood import steamed_sea_bass_with_ginger_and_spring_onion
from recipes.leafy_greens import blanched_choy_sum_with_sizzling_oil, spinach_with_chilli_and_fermented_tofu, \
    chinese_broccoli_in_ginger_sauce
from recipes.meat import red_braised_pork, beef_with_cumin
from recipes.root_vegetables import stir_fried_potato_slivers_with_chilli_and_sichuan_pepper
from recipes.soups import taro_and_arugula_soup, chicken_soup, soup_of_salted_duck_eggs
from recipes.tofu import silken_tofu_with_pickled_mustard_greens, firm_tofu_with_green_bell_peppers


def tofu():
    return [
        firm_tofu_with_green_bell_peppers(),
        silken_tofu_with_pickled_mustard_greens()
    ]


def meat():
    return [
        red_braised_pork(),
        beef_with_cumin()
    ]


def chicken_and_eggs():
    return [
        braised_chicken_with_chestnuts(),
        stir_fried_eggs_with_tomatoes(),
        steamed_eggs()
    ]


def fish_and_seafood():
    return [
        steamed_sea_bass_with_ginger_and_spring_onion()
    ]


def leafy_greens():
    return [
        blanched_choy_sum_with_sizzling_oil(),
        spinach_with_chilli_and_fermented_tofu(),
        chinese_broccoli_in_ginger_sauce()
    ]


def root_vegetables():
    return [
        stir_fried_potato_slivers_with_chilli_and_sichuan_pepper()
    ]


def soups():
    return [
        soup_of_salted_duck_eggs(),
        taro_and_arugula_soup(),
        chicken_soup()
    ]


def hun():
    return tofu() + meat() + chicken_and_eggs() + fish_and_seafood()


def shu():
    return leafy_greens() + root_vegetables()
