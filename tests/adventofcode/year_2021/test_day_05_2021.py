import pytest

from adventofcode.year_2021.day_05_2021 import (
    count_intersections,
    get_line,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def test_parse_input():
    parsed_input_all = parse_input(test_input, False)
    assert len(parsed_input_all) == 10

    parsed_input_no_diagonals = parse_input(test_input, True)
    assert len(parsed_input_no_diagonals) == 6


@pytest.mark.parametrize(
    ["positions", "expected"],
    [(((0, 9), (5, 9)), [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)])],
)
def test_get_line(positions, expected):
    assert get_line(positions) == expected


@pytest.mark.parametrize(
    ["exclude_diagonals", "expected"],
    [
        (True, 5),
        (False, 12),
    ],
)
def test_count_intersections(exclude_diagonals, expected):
    parsed_input = parse_input(test_input, exclude_diagonals)
    assert count_intersections(parsed_input) == expected


def test_part_one():
    answer = part_one(test_input)
    assert answer == 5


def test_part_two():
    answer = part_two(test_input)
    assert answer == 12
