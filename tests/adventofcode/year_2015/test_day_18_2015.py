import pytest

from adventofcode.year_2015.day_18_2015 import (
    OFF,
    ON,
    animate,
    animate_stuck_corners,
    get_neighbours,
    get_next_state,
    grid_to_list_str,
    read_grid,
)

test_input = [
    ".#.#.#",
    "...##.",
    "#....#",
    "..#...",
    "#.#..#",
    "####..",
]

test_input_step_1 = [
    "..##..",
    "..##.#",
    "...##.",
    "......",
    "#.....",
    "#.##..",
]

test_input_step_2 = [
    "..###.",
    "......",
    "..###.",
    "......",
    ".#....",
    ".#....",
]

test_input_step_3 = [
    "...#..",
    "......",
    "...#..",
    "..##..",
    "......",
    "......",
]

test_input_step_4 = [
    "......",
    "......",
    "..##..",
    "..##..",
    "......",
    "......",
]

test_input_part_two = [
    "##.#.#",
    "...##.",
    "#....#",
    "..#...",
    "#.#..#",
    "####.#",
]

test_input_part_two_step_1 = [
    "#.##.#",
    "####.#",
    "...##.",
    "......",
    "#...#.",
    "#.####",
]

test_input_part_two_step_2 = [
    "#..#.#",
    "#....#",
    ".#.##.",
    "...##.",
    ".#..##",
    "##.###",
]

test_input_part_two_step_3 = [
    "#...##",
    "####.#",
    "..##.#",
    "......",
    "##....",
    "####.#",
]

test_input_part_two_step_4 = [
    "#.####",
    "#....#",
    "...#..",
    ".##...",
    "#.....",
    "#.#..#",
]

test_input_part_two_step_5 = [
    "##.###",
    ".##..#",
    ".##...",
    ".##...",
    "#.#...",
    "##...#",
]


def test_read_grid():
    assert read_grid(test_input) == {
        (0, 0): OFF,
        (0, 1): OFF,
        (0, 2): ON,
        (0, 3): OFF,
        (0, 4): ON,
        (0, 5): ON,
        (1, 0): ON,
        (1, 1): OFF,
        (1, 2): OFF,
        (1, 3): OFF,
        (1, 4): OFF,
        (1, 5): ON,
        (2, 0): OFF,
        (2, 1): OFF,
        (2, 2): OFF,
        (2, 3): ON,
        (2, 4): ON,
        (2, 5): ON,
        (3, 0): ON,
        (3, 1): ON,
        (3, 2): OFF,
        (3, 3): OFF,
        (3, 4): OFF,
        (3, 5): ON,
        (4, 0): OFF,
        (4, 1): ON,
        (4, 2): OFF,
        (4, 3): OFF,
        (4, 4): OFF,
        (4, 5): OFF,
        (5, 0): ON,
        (5, 1): OFF,
        (5, 2): ON,
        (5, 3): OFF,
        (5, 4): ON,
        (5, 5): OFF,
    }


def test_get_neighbours():
    light = (10, 10)
    x, y = light

    neighbours = get_neighbours(light)
    assert len(neighbours) == 8
    assert (x - 1, y - 1) in neighbours
    assert (x, y - 1) in neighbours
    assert (x + 1, y - 1) in neighbours
    assert (x - 1, y) in neighbours
    assert (x + 1, y) in neighbours
    assert (x - 1, y + 1) in neighbours
    assert (x, y + 1) in neighbours
    assert (x + 1, y + 1) in neighbours


@pytest.mark.parametrize(
    ["own_value", "neighbours_on", "expected"],
    [
        (ON, 1, OFF),
        (ON, 2, ON),
        (ON, 3, ON),
        (ON, 4, OFF),
        (OFF, 2, OFF),
        (OFF, 3, ON),
        (OFF, 4, OFF),
    ],
)
def test_get_next_state(own_value, neighbours_on, expected):
    light = (10, 10)
    grid = {light: own_value}

    # Setup neighbours
    on_values = [ON] * neighbours_on
    off_values = [OFF] * (8 - neighbours_on)
    values = on_values + off_values
    neighbours = get_neighbours(light)

    for neighbours in neighbours:  # noqa
        grid[neighbours] = values.pop(0)

    assert get_next_state(light, grid) == expected


def test_get_next_state_raises():
    light = (10, 10)
    grid = {light: "!"}

    # Setup neighbours
    on_values = [ON] * 4
    off_values = [OFF] * 4
    values = on_values + off_values
    neighbours = get_neighbours(light)

    for neighbours in neighbours:  # noqa
        grid[neighbours] = values.pop(0)

    with pytest.raises(ValueError) as wrapped_e:
        _ = get_next_state(light, grid)

    assert str(wrapped_e.value) == "unknown light state: !"


@pytest.mark.parametrize(
    ["steps", "expected"],
    [
        (1, test_input_step_1),
        (2, test_input_step_2),
        (3, test_input_step_3),
        (4, test_input_step_4),
    ],
)
def test_animate(steps, expected):
    grid = read_grid(test_input)

    for step in range(steps):  # noqa
        grid = animate(grid)

    assert grid_to_list_str(grid) == expected


@pytest.mark.parametrize(
    ["steps", "expected"],
    [
        (1, test_input_part_two_step_1),
        (2, test_input_part_two_step_2),
        (3, test_input_part_two_step_3),
        (4, test_input_part_two_step_4),
        (5, test_input_part_two_step_5),
    ],
)
def test_animate_stuck_corners(steps, expected):
    grid = read_grid(test_input_part_two)

    for step in range(steps):  # noqa
        grid = animate_stuck_corners(grid)

    assert grid_to_list_str(grid) == expected


def test_grid_to_list_str():
    grid = read_grid(test_input)
    assert grid_to_list_str(grid) == test_input
