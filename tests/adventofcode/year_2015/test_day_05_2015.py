import pytest

from adventofcode.year_2015.day_05_2015 import (
    has_recurring_pairs,
    has_repeating_letter,
    is_nice,
)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_is_nice(line, expected):
    assert expected == is_nice(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("xyx", True),
        ("abcdefeghi", True),
        ("aaa", True),
    ],
)
def test_has_repeating_letter(line, expected):
    assert expected == has_repeating_letter(line)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("xyxy", True),
        ("aabcdefgaa", True),
        ("aaa", False),
    ],
)
def test_has_recurring_pairs(line, expected):
    assert expected == has_recurring_pairs(line)
