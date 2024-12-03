import os

import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2015.day_10_2015 import (
    iterate,
    part_one,
    part_two,
    part_two_method_2,
)


@pytest.mark.parametrize(
    ["value", "expected"],
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
        ("3113322113", "132123222113"),
        ("132123222113", "111312111213322113"),
    ],
)
def test_iterate(value, expected):
    assert expected == iterate(value)


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_one():
    assert part_one(get_input_for_day(2015, 10)) == 329356


@pytest.mark.skip(reason="extremely slow in CI with Python 3.11")
def test_part_two():
    assert part_two(get_input_for_day(2015, 10)) == 4666278


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_two_method_2():
    assert part_two_method_2(get_input_for_day(2015, 10)) == 4666278
