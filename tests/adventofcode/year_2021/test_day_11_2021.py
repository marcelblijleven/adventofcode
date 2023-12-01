import pytest

from adventofcode.year_2021.day_11_2021 import (
    Octopus,
    OctopusGrid,
    part_one,
    part_two,
    run_ticks,
    run_ticks_until_sync,
)

test_input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]


@pytest.mark.parametrize(
    ["position", "adjacent_octopuses"],
    [
        ((0, 0), [(1, 0), (1, 1), (0, 1)]),
        ((0, 9), [(0, 8), (1, 8), (1, 9)]),
        ((5, 5), [(4, 4), (4, 5), (4, 6), (5, 4), (5, 6), (6, 4), (6, 5), (6, 6)]),
        ((9, 0), [(8, 0), (8, 1), (9, 1)]),
        ((9, 9), [(8, 8), (8, 9), (9, 8)]),
    ],
)
def test_octopus_adjacent_octopuses(position, adjacent_octopuses):
    octopus = Octopus(1, position)
    assert sorted(octopus.adjacent_octopuses) == sorted(adjacent_octopuses)


def test_part_one():
    grid = OctopusGrid(test_input)
    run_ticks(grid, 100)
    assert part_one(test_input) == 1656


def test_part_two():
    grid = OctopusGrid(test_input)
    run_ticks_until_sync(grid)
    assert part_two(test_input) == 195
