import pytest

from adventofcode.year_2023.day_03_2023 import (
    find_gear_coords,
    find_symbol_coords,
    neighbour_has_adjacent_symbol,
    neighbouring_gear_coords,
    part_one,
    part_two,
)

test_input = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def test_find_symbol_coords():
    assert find_symbol_coords(test_input) == {
        (3, 8),
        (5, 5),
        (3, 4),
        (5, 8),
        (3, 1),
        (6, 3),
    }


def test_find_gear_coords():
    assert find_gear_coords(test_input) == {(3, 1): [], (3, 4): [], (5, 8): []}


@pytest.mark.parametrize(
    ["current_position", "expected"],
    [
        ((0, 0), True),
        ((0, 1), True),
        ((1, 1), True),
        ((1, 0), True),
        ((2, 2), True),
        ((3, 3), False),
    ],
)
def test_neighbour_has_adjacent_symbol(current_position, expected):
    symbols = {(1, 1)}
    assert neighbour_has_adjacent_symbol(current_position, symbols) == expected


@pytest.mark.parametrize(
    ["current_position", "expected"],
    [
        ((0, 0), (1, 1)),
        ((0, 1), (1, 1)),
        ((1, 1), (1, 1)),
        ((1, 0), (1, 1)),
        ((2, 2), (1, 1)),
        ((3, 3), None),
    ],
)
def test_neighbouring_gear_coords(current_position, expected):
    gears = {(1, 1)}
    assert neighbouring_gear_coords(current_position, gears) == expected


def test_part_one():
    assert part_one(test_input) == 4361


def test_part_two():
    assert part_two(test_input) == 467835
