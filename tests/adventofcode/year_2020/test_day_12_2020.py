import pytest

from adventofcode.year_2020.day_12_2020 import (
    EAST,
    LEFT,
    NORTH,
    RIGHT,
    SOUTH,
    WEST,
    part_one,
    part_two,
    turn,
    turn_waypoint,
)

test_input = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
]


@pytest.mark.parametrize(
    ["turn_direction", "degrees", "current_direction", "expected"],
    [
        (LEFT, 90, NORTH, WEST),
        (LEFT, 180, NORTH, SOUTH),
        (LEFT, 270, NORTH, EAST),
        (RIGHT, 90, NORTH, EAST),
        (RIGHT, 180, NORTH, SOUTH),
        (RIGHT, 270, NORTH, WEST),
        (LEFT, 90, EAST, NORTH),
        (LEFT, 180, EAST, WEST),
        (LEFT, 270, EAST, SOUTH),
        (RIGHT, 90, EAST, SOUTH),
        (RIGHT, 180, EAST, WEST),
        (RIGHT, 270, EAST, NORTH),
        (LEFT, 90, SOUTH, EAST),
        (LEFT, 180, SOUTH, NORTH),
        (LEFT, 270, SOUTH, WEST),
        (RIGHT, 90, SOUTH, WEST),
        (RIGHT, 180, SOUTH, NORTH),
        (RIGHT, 270, SOUTH, EAST),
        (LEFT, 90, WEST, SOUTH),
        (LEFT, 180, WEST, EAST),
        (LEFT, 270, WEST, NORTH),
        (RIGHT, 90, WEST, NORTH),
        (RIGHT, 180, WEST, EAST),
        (RIGHT, 270, WEST, SOUTH),
    ],
)
def test_turn(turn_direction, degrees, current_direction, expected):
    assert turn(turn_direction, degrees, current_direction) == expected


@pytest.mark.parametrize(
    ["waypoint", "direction", "degrees", "expected"],
    [
        ((10, 4), LEFT, 90, (-4, 10)),
        ((10, 4), LEFT, 180, (-10, -4)),
        ((10, 4), LEFT, 270, (4, -10)),
        ((10, 4), RIGHT, 90, (4, -10)),
        ((10, 4), RIGHT, 180, (-10, -4)),
        ((10, 4), RIGHT, 270, (-4, 10)),
    ],
)
def test_turn_waypoint(waypoint, direction, degrees, expected):
    assert turn_waypoint(waypoint, direction, degrees) == expected


def test_turn_waypoint_raises():
    with pytest.raises(ValueError) as wrapped_e:
        turn_waypoint((0, 0), "X", 90)

    assert str(wrapped_e.value) == "cannot process unknown direction: X"

    with pytest.raises(ValueError) as wrapped_e:
        turn_waypoint((0, 0), "R", 89)

    assert str(wrapped_e.value) == "cannot process degrees: 89"


def test_part_one():
    answer = part_one(test_input)
    assert answer == 25


def test_part_two():
    answer = part_two(test_input)
    assert answer == 286
