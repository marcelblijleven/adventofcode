from adventofcode.year_2015.day_17_2015 import (
    find_combinations,
    find_different_ways,
    get_containers,
)

test_input = [
    "20",
    "15",
    "10",
    "5",
    "5",
]


def test_get_containers():
    assert get_containers(test_input) == [20, 15, 10, 5, 5]


def test_find_combinations():
    assert find_combinations(test_input, liters=25) == 4


def test_find_different_ways():
    assert find_different_ways(test_input, liters=25) == 3
