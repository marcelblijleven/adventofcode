import pytest

from adventofcode.year_2023.day_01_2023 import (
    get_calibration_value,
    get_calibration_value_with_words,
    part_one,
    part_two,
)

test_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

test_input_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_get_calibration_value(line, expected):
    assert get_calibration_value(line) == expected


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_get_calibration_value_with_words(line, expected):
    assert get_calibration_value_with_words(line) == expected


def test_part_one():
    assert part_one(test_input) == 142


def test_part_two():
    assert part_two(test_input_2) == 281
