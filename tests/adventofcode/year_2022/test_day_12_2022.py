from collections import defaultdict

import pytest

from adventofcode.year_2022.day_12_2022 import (
    can_climb,
    get_directions_for_position,
    get_possible_routes_for_position,
    part_one,
    part_two,
)

test_input = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]


@pytest.mark.parametrize(
    ["current", "next_position", "expected"],
    [
        ("S", "a", True),
        ("S", "E", True),
        ("a", "E", False),
        ("z", "E", True),
        ("a", "a", True),
        ("a", "b", True),
        ("a", "c", False),
        ("c", "b", True),
        ("c", "a", True),
    ],
)
def test_can_climb(current, next_position, expected):
    assert can_climb(current, next_position) == expected


@pytest.mark.parametrize(
    ["position", "expected"],
    [
        ((0, 0), {(0, 1), (1, 0)}),
        ((1, 0), {(0, 0), (1, 1), (2, 0)}),
        ((2, 0), {(1, 0), (2, 1)}),
        ((1, 1), {(0, 1), (2, 1), (1, 0), (1, 2)}),
    ],
)
def test_get_directions_for_position(position, expected):
    grid = {}

    for y in range(3):
        for x in range(3):
            grid[x, y] = "a"

    assert get_directions_for_position(position, grid) == expected


def test_part_one():
    assert part_one(test_input) == 31


def test_part_two():
    assert part_two(test_input) == 29
