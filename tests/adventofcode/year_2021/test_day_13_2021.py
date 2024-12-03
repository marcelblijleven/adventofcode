import os

import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_13_2021 import (
    fold_paper,
    fold_position_along_x,
    fold_position_along_y,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5",
]


@pytest.mark.parametrize(
    ["position", "fold_y", "expected"],
    [
        ((2, 9), 5, (2, 1)),
        ((2, 8), 5, (2, 2)),
        ((2, 7), 5, (2, 3)),
        ((2, 6), 5, (2, 4)),
        ((2, 9), 4, (2, -1)),
        ((2, 8), 4, (2, 0)),
        ((2, 7), 4, (2, 1)),
        ((2, 6), 4, (2, 2)),
    ],
)
def test_fold_along_y(position, fold_y, expected):
    assert fold_position_along_y(position, fold_y) == expected


@pytest.mark.parametrize(
    ["position", "fold_x", "expected"],
    [
        ((9, 2), 5, (1, 2)),
        ((8, 2), 5, (2, 2)),
        ((7, 2), 5, (3, 2)),
        ((6, 2), 5, (4, 2)),
        ((9, 2), 4, (-1, 2)),
        ((8, 2), 4, (0, 2)),
        ((7, 2), 4, (1, 2)),
        ((6, 2), 4, (2, 2)),
    ],
)
def test_fold_along_x(position, fold_x, expected):
    assert fold_position_along_x(position, fold_x) == expected


def test_fold_paper_invalid_instructions():
    with pytest.raises(ValueError) as wrapped_e:
        fold_paper({}, ("z", 4))

    assert str(wrapped_e.value) == "invalid instruction received: ('z', 4)"


def test_parse_input():
    paper, instructions = parse_input(test_input)
    assert paper == {
        (0, 3): 1,
        (0, 13): 1,
        (0, 14): 1,
        (1, 10): 1,
        (2, 14): 1,
        (3, 0): 1,
        (3, 4): 1,
        (4, 1): 1,
        (4, 11): 1,
        (6, 0): 1,
        (6, 10): 1,
        (6, 12): 1,
        (8, 4): 1,
        (8, 10): 1,
        (9, 0): 1,
        (9, 10): 1,
        (10, 4): 1,
        (10, 12): 1,
    }

    assert instructions == [("y", 7), ("x", 5)]


def test_part_one():
    assert part_one(test_input) == 17


# flake8: noqa
@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_two():
    assert (
        part_two(get_input_for_day(2021, 13))
        == """
███   ██  ████ █    ███  █  █ ████ ███ 
█  █ █  █    █ █    █  █ █  █ █    █  █
█  █ █      █  █    ███  ████ ███  █  █
███  █ ██  █   █    █  █ █  █ █    ███ 
█ █  █  █ █    █    █  █ █  █ █    █   
█  █  ███ ████ ████ ███  █  █ █    █   """
    )  # noqa
