from collections import defaultdict

import pytest

from adventofcode.year_2022.day_09_2022 import (
    determine_move,
    get_instructions,
    move_snake,
    parse_instruction,
    part_one,
    part_two,
    simulate_rope,
    simulate_rope_snake,
)

test_input = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2",
]

test_input_larger = [
    "R 5",
    "U 8",
    "L 8",
    "D 3",
    "R 17",
    "D 10",
    "L 25",
    "U 20",
]


@pytest.mark.parametrize(
    ["instruction", "expected"],
    [
        ("R 4", ("R", 4)),
        ("U 4", ("U", 4)),
        ("L 3", ("L", 3)),
        ("D 1", ("D", 1)),
        ("R 4", ("R", 4)),
        ("D 1", ("D", 1)),
        ("L 5", ("L", 5)),
        ("R 2", ("R", 2)),
    ],
)
def test_parse_instruction(instruction, expected):
    assert parse_instruction(instruction) == expected


def test_get_instructions():
    assert len(list(get_instructions(test_input))) == len(test_input)


def test_simulate_rope():
    assert simulate_rope(test_input) == 13


def test_simulate_rope_snake():
    assert simulate_rope_snake(test_input) == 1
    assert simulate_rope_snake(test_input_larger) == 36


def test_determine_move():
    # horizontal moves
    assert determine_move((0, 0), (2, 0)) == (1, 0)
    assert determine_move((1, 0), (3, 0)) == (2, 0)
    assert determine_move((1, 0), (4, 0)) == (3, 0)

    assert determine_move((0, 0), (-2, 0)) == (-1, 0)
    assert determine_move((-1, 0), (-3, 0)) == (-2, 0)
    assert determine_move((-1, 0), (-4, 0)) == (-3, 0)

    # vertical moves
    assert determine_move((0, 0), (0, 2)) == (0, 1)
    assert determine_move((0, 1), (0, 3)) == (0, 2)
    assert determine_move((0, 1), (0, 4)) == (0, 3)

    assert determine_move((0, 0), (0, -2)) == (0, -1)
    assert determine_move((0, -1), (0, -3)) == (0, -2)
    assert determine_move((0, -1), (0, -4)) == (0, -3)

    # diagonal moves
    assert determine_move((0, 0), (2, -1)) == (1, -1)
    assert determine_move((3, -1), (4, -3)) == (4, -2)


def test_move_snake():
    positions = {k: (0, 0) for k in range(0, 10)}
    tail_locations = defaultdict(int)

    move_snake(("R", 4), positions, tail_locations)
    assert positions[0] == (4, 0)
    assert positions[1] == (3, 0)
    assert positions[2] == (2, 0)
    assert positions[3] == (1, 0)
    assert (
        positions[4]
        == positions[5]
        == positions[6]
        == positions[7]
        == positions[8]
        == positions[9]
        == (0, 0)
    )

    move_snake(("U", 4), positions, tail_locations)
    assert positions[0] == (4, -4)
    assert positions[1] == (4, -3)
    assert positions[2] == (4, -2)
    assert positions[3] == (3, -2)


def test_part_one():
    assert part_one(test_input) == 13


def test_part_two():
    assert part_two(test_input) == 1
