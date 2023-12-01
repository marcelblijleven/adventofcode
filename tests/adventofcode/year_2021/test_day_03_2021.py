import pytest

from adventofcode.year_2021.day_03_2021 import (
    filter_list,
    get_life_support,
    part_one,
    part_two,
)

test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


@pytest.mark.parametrize(["most_common", "expected"], [(True, 23), (False, 10)])
def test_filter_list(most_common, expected):
    assert filter_list(test_input, use_most_common=most_common) == expected


def test_get_life_support():
    assert get_life_support(test_input) == 230


def test_part_one():
    answer = part_one(test_input)
    assert answer == 198


def test_part_two():
    answer = part_two(test_input)
    assert answer == 230
