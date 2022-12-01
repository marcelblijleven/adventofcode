import pytest

from adventofcode.year_2015.day_06_2015 import (
    count_lights,
    count_brightness,
    run_instructions_part_two,
    run_instructions,
)


@pytest.mark.parametrize(
    ["grid", "expected"],
    [
        ({(0, 1): True, (1, 1): True, (0, 2): True}, 3),
        ({(0, 1): False, (1, 1): True, (0, 2): False}, 1),
    ],
)
def test_count_lights(grid, expected):
    assert expected == count_lights(grid)


@pytest.mark.parametrize(
    ["grid", "expected"],
    [
        ({(0, 1): 1, (1, 1): 2, (0, 2): 3}, 6),
        ({(0, 1): 0, (1, 1): 0, (0, 2): 0}, 0),
    ],
)
def test_count_brightness(grid, expected):
    assert expected == count_brightness(grid)


@pytest.mark.parametrize(
    ["line", "expected"],
    [("turn on 499,499 through 500,500", 4), ("toggle 0,0 through 999,0", 1000)],
)
def test_run_instructions(line, expected):
    assert expected == run_instructions([line])


@pytest.mark.parametrize(
    ["line", "expected"],
    [("turn on 0,0 through 0,0", 1), ("toggle 0,0 through 999,999", 2000000)],
)
def test_run_instructions_part_two(line, expected):
    assert expected == run_instructions_part_two([line])
