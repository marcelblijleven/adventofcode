import pytest

from adventofcode.year_2023.day_01_2023 import (part_two, part_one, get_calibration_value,
                                                )

test_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]


@pytest.mark.parametrize(["line", "expected"], [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77),
])
def test_get_calibration_value(line, expected):
    assert get_calibration_value(line) == expected


def test_part_one():
    assert part_one(test_input) == 142


def test_part_two():
    assert part_two(test_input) == 'x'
