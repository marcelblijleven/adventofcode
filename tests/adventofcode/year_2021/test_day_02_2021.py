import os

import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_02_2021 import (
    get_new_position,
    move_submarine,
    part_one,
    part_two,
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


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_one():
    answer = part_one(get_input_for_day(2021, 2))
    assert answer == 2036120


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_two():
    answer = part_two(get_input_for_day(2021, 2))
    assert answer == 2015547716
