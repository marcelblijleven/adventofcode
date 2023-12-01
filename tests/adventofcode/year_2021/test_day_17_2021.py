import pytest

from adventofcode.year_2021.day_17_2021 import (
    in_target,
    is_out_of_bounds,
    part_one,
    part_one_quick_maths,
    part_two,
)

test_input = []


@pytest.mark.parametrize(
    ["position", "expected"],
    [
        ((0, 0), False),
        ((3, 2), False),
        ((3, 8), False),
        ((6, 2), False),
        ((7, 2), False),
        ((7, 7), False),
        ((6, 8), False),
        ((3, 3), True),
        ((4, 3), True),
        ((3, 4), True),
        ((4, 5), True),
        ((6, 3), True),
        ((6, 7), True),
    ],
)
def test_in_target(position, expected):
    target_area = (3, 6, 3, 7)
    assert in_target(position, target_area) == expected


@pytest.mark.parametrize(
    ["position", "expected"],
    [
        ((0, -8), True),
        ((1, -8), True),
        ((2, -8), True),
        ((3, -8), True),
        ((4, -8), True),
        ((5, -8), True),
        ((6, -8), True),
        ((7, -8), True),
        ((8, -8), True),
        ((9, -8), True),
        ((10, -8), True),
    ],
)
def test_is_out_of_bounds(position, expected):
    target_area = (3, 6, -7, -3)
    assert is_out_of_bounds(position, target_area) == expected


def test_part_one():
    assert part_one(["target area: x=20..30, y=-10..-5"]) == 45


def test_part_one_quick_maths():
    assert part_one_quick_maths(["target area: x=20..30, y=-10..-5"]) == 45


def test_part_two():
    assert part_two(["target area: x=20..30, y=-10..-5"]) == 112
