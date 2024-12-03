from collections import defaultdict

import pytest

from adventofcode.year_2021.day_20_2021 import (
    get_algorithm_position_for_pixel,
    get_algorithm_position_for_pixel_simplified,
    get_infinity_grid,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##"  # noqa
    + "#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###"
    + ".######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#."
    + ".#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#....."
    + ".#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.."
    + "...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#....."
    + "..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#",
    "",
    "#..#.",
    "#....",
    "##..#",
    "..#..",
    "..###",
]

test_input_image = defaultdict(int)
test_input_image.update(
    {
        (0, 0): 1,
        (0, 1): 1,
        (0, 2): 1,
        (0, 3): 0,
        (0, 4): 0,
        (1, 0): 0,
        (1, 1): 0,
        (1, 2): 1,
        (1, 3): 0,
        (1, 4): 0,
        (2, 0): 0,
        (2, 1): 0,
        (2, 2): 0,
        (2, 3): 1,
        (2, 4): 1,
        (3, 0): 1,
        (3, 1): 0,
        (3, 2): 0,
        (3, 3): 0,
        (3, 4): 1,
        (4, 0): 0,
        (4, 1): 0,
        (4, 2): 1,
        (4, 3): 0,
        (4, 4): 1,
    }
)


def test_parse_input():
    image = parse_input(test_input)
    assert image.algorithm == [0 if x == "." else 1 for x in test_input[0]]
    assert len(image.algorithm) == 512
    assert dict(image.grid) == {k: v for k, v in test_input_image.items() if v != 0}


def test_enhance():
    image = parse_input(test_input)
    assert image.enhance(2) == 35


def test_get_algorithm_position_for_pixel():
    image = parse_input(test_input)
    infinity_grid_test: defaultdict[tuple[int, int], int] = defaultdict(int, image.grid)
    assert get_algorithm_position_for_pixel((2, 2), infinity_grid_test) == int(
        "000100010", 2
    )


def test_get_algorithm_position_for_pixel_simplified():
    image = parse_input(test_input)
    infinity_grid_test: defaultdict[tuple[int, int], int] = defaultdict(int, image.grid)
    assert get_algorithm_position_for_pixel_simplified(
        (2, 2), infinity_grid_test
    ) == int("000100010", 2)


@pytest.mark.parametrize(
    ["toggles", "default_value"],
    [
        (True, 1337),
        (False, 1337),
    ],
)
def test_get_infinity_grid(toggles, default_value):
    infinity_grid = get_infinity_grid(toggles, default_value)
    infinity_grid[(1, 1)] = 10
    assert infinity_grid[(1, 1)] == 10

    if toggles:
        assert infinity_grid[(10, 10)] == default_value
    else:
        assert infinity_grid[(10, 10)] == 0


def test_part_one():
    x = part_one(test_input)
    assert x == 35


def test_part_two():
    assert part_two(test_input) == 3351
