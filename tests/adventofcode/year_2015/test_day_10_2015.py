import os
import sys

import pytest

from adventofcode.year_2015.day_10_2015 import (
    iterate,
    part_two,
    part_one,
    get_input_for_day,
)


def should_skip() -> bool:
    major, minor, micro, releaselevel, serial = sys.version_info
    if major == 3 and minor == 11 and os.getenv('CI', False):
        return True

    return False


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


def test_part_one():
    assert part_one(get_input_for_day(2015, 10)) == 329356


@pytest.mark.skipif(
    should_skip() == 'true',
    reason="For some reason, this test takes 23 minutes on 3.11 in Github Actions, but runs fine on earlier versions",
)
def test_part_two():
    assert part_two(get_input_for_day(2015, 10)) == 4666278
