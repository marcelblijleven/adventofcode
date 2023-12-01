import asyncio

import pytest

from adventofcode.year_2021.day_09_2021 import (
    calculate_basin,
    calculate_basin_async,
    calculate_basin_mp,
    find_basin_size_product,
    find_basin_size_product_async,
    find_basin_size_product_mp,
    get_low_points,
    get_risk_level,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def test_parse_input():
    cave_floor, width, height = parse_input(test_input)
    assert width == 9
    assert height == 4
    assert dict(cave_floor) == {
        (0, 0): 2,
        (0, 1): 3,
        (0, 2): 9,
        (0, 3): 8,
        (0, 4): 9,
        (1, 0): 1,
        (1, 1): 9,
        (1, 2): 8,
        (1, 3): 7,
        (1, 4): 8,
        (2, 0): 9,
        (2, 1): 8,
        (2, 2): 5,
        (2, 3): 6,
        (2, 4): 9,
        (3, 0): 9,
        (3, 1): 7,
        (3, 2): 6,
        (3, 3): 7,
        (3, 4): 9,
        (4, 0): 9,
        (4, 1): 8,
        (4, 2): 7,
        (4, 3): 8,
        (4, 4): 9,
        (5, 0): 4,
        (5, 1): 9,
        (5, 2): 8,
        (5, 3): 9,
        (5, 4): 6,
        (6, 0): 3,
        (6, 1): 4,
        (6, 2): 9,
        (6, 3): 6,
        (6, 4): 5,
        (7, 0): 2,
        (7, 1): 9,
        (7, 2): 8,
        (7, 3): 7,
        (7, 4): 6,
        (8, 0): 1,
        (8, 1): 2,
        (8, 2): 9,
        (8, 3): 8,
        (8, 4): 7,
        (9, 0): 0,
        (9, 1): 1,
        (9, 2): 2,
        (9, 3): 9,
        (9, 4): 8,
    }


def test_get_low_points():
    assert get_low_points(*parse_input(test_input)) == [(1, 0), (9, 0), (2, 2), (6, 4)]


def test_get_risk_level():
    assert get_risk_level(*parse_input(test_input)) == 15


@pytest.mark.parametrize(
    ["position", "expected"],
    [
        ((1, 0), 3),
        ((9, 0), 9),
        ((2, 2), 14),
        ((6, 4), 9),
    ],
)
def test_calculate_basin(position, expected):
    cave_floor, width, height = parse_input(test_input)
    basin = set()
    assert len(calculate_basin(cave_floor, position, basin)) == expected


@pytest.mark.parametrize(
    ["position", "expected"],
    [
        ((1, 0), 3),
        ((9, 0), 9),
        ((2, 2), 14),
        ((6, 4), 9),
    ],
)
def test_calculate_basin_async(position, expected):
    cave_floor, width, height = parse_input(test_input)
    result = asyncio.run(calculate_basin_async(cave_floor, position))
    assert len(result) == expected


@pytest.mark.parametrize(
    ["position", "expected"],
    [
        ((1, 0), 3),
        ((9, 0), 9),
        ((2, 2), 14),
        ((6, 4), 9),
    ],
)
def test_calculate_basin_mp(position, expected):
    cave_floor, width, height = parse_input(test_input)
    assert len(calculate_basin_mp(cave_floor, position)) == expected


def test_find_basin_size_product():
    assert find_basin_size_product(*parse_input(test_input)) == 1134


def test_find_basin_size_product_async():
    result = asyncio.run(find_basin_size_product_async(*parse_input(test_input)))
    assert result == 1134


def test_find_basin_size_product_mp():
    assert find_basin_size_product_mp(*parse_input(test_input)) == 1134


def test_part_one():
    assert part_one(test_input) == 15


def test_part_two():
    assert part_two(test_input) == 1134
