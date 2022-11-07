import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_02_2021 import (
    part_two,
    part_one,
    move_submarine,
    get_new_position,
)


test_input = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2",
]


def test_move_submarine():
    assert move_submarine(test_input, False) == (15, 10)
    assert move_submarine(test_input, True) == (15, 60)


def test_get_new_position():
    with pytest.raises(ValueError) as wrapped_e:
        get_new_position((0, 0), 0, ("coffee", 2), False)

    assert str(wrapped_e.value) == "unknown direction received: coffee"

    with pytest.raises(ValueError) as wrapped_e:
        get_new_position((0, 0), 0, ("coffee", 2), True)

    assert str(wrapped_e.value) == "unknown direction received: coffee"


def test_part_one():
    answer = part_one(get_input_for_day(2021, 2))
    assert answer == 2036120


def test_part_two():
    answer = part_two(get_input_for_day(2021, 2))
    assert answer == 2015547716
