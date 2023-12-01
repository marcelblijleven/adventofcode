import os

import pytest

from adventofcode.year_2020.day_15_2020 import parse_input, part_one, part_two, solve

test_input = [
    "0,3,6",
]


def test_parse_input():
    assert parse_input(test_input) == [0, 3, 6]


@pytest.mark.parametrize(
    ["starting_list", "rounds", "expected"],
    [
        ([0, 3, 6], 10, 0),
        ([0, 3, 6], 2020, 436),
        ([1, 3, 2], 2020, 1),
        ([2, 1, 3], 2020, 10),
        ([1, 2, 3], 2020, 27),
        ([2, 3, 1], 2020, 78),
        ([3, 2, 1], 2020, 438),
        ([3, 1, 2], 2020, 1836),
    ],
)
def test_solve_part_one(starting_list, rounds, expected):
    assert solve(starting_list, rounds) == expected


def test_part_one():
    assert part_one(test_input) == 436


@pytest.mark.skipif(os.getenv("CI", None) == "true", reason="slow test")
def test_part_two():
    assert part_two(test_input) == 175594
