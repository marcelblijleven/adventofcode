from adventofcode.year_2015.day_15_2015 import find_highest_scoring_cookie

test_input = [
    "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
]


def test_find_highest_scoring_cookie():
    assert find_highest_scoring_cookie(test_input) == 62842880


def test_find_highest_scoring_cookie_with_cookies():
    assert find_highest_scoring_cookie(test_input, match_calories=True) == 57600000
