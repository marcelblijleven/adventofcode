import pytest

from adventofcode.year_2021.day_21_2021 import (
    get_new_position,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "Player 1 starting position: 4",
    "Player 2 starting position: 8",
]


def test_parse_input():
    assert parse_input(test_input) == (4, 8)


@pytest.mark.parametrize(
    ["current", "moves", "expected"],
    [
        (1, 5, 6),
        (2, 5, 7),
        (3, 5, 8),
        (4, 5, 9),
        (5, 5, 10),
        (6, 5, 1),
        (7, 5, 2),
        (8, 5, 3),
        (9, 5, 4),
        (10, 5, 5),
    ],
)
def test_get_new_position(current, moves, expected):
    assert get_new_position(current, moves) == expected


def test_part_one():
    assert part_one(test_input) == 739785


def test_part_two():
    assert part_two(test_input) == 444356092776315
