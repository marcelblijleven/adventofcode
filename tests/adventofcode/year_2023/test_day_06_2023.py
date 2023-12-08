import pytest

from adventofcode.year_2023.day_06_2023 import (
    calculate_distance,
    calculate_ways_to_win,
    calculate_ways_to_win_part_two,
    parse_input,
    parse_input_part_two,
    part_one,
    part_two,
)

test_input = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def test_parse_input():
    assert parse_input(test_input) == [(7, 9), (15, 40), (30, 200)]


def test_parse_input_part_two():
    assert parse_input_part_two(test_input) == (71530, 940200)


@pytest.mark.parametrize(
    ["hold", "max_time", "expected"],
    [
        (0, 7, 0),
        (1, 7, 6),
        (2, 7, 10),
        (3, 7, 12),
        (4, 7, 12),
        (5, 7, 10),
        (6, 7, 6),
        (7, 7, 0),
    ],
)
def test_calculate_distance(hold, max_time, expected):
    assert calculate_distance(hold, max_time) == expected


@pytest.mark.parametrize(
    ["duration", "farthest_distance", "expected"],
    [
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),
    ],
)
def test_calculate_ways_to_win(duration, farthest_distance, expected):
    assert calculate_ways_to_win(duration, farthest_distance) == expected


def test_calculate_ways_to_win_part_two():
    assert calculate_ways_to_win_part_two(71530, 940200) == 71503


def test_part_one():
    assert part_one(test_input) == 288


def test_part_two():
    assert part_two(test_input) == 71503
