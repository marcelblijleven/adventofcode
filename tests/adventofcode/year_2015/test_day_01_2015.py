import pytest

from adventofcode.year_2015.day_01_2015 import part_one, part_two


@pytest.mark.parametrize(
    ["sequence", "expected"], [("(())", 0), ("()()", 0), ("))(((((", 3)]
)
def test_part_one(sequence, expected):
    assert part_one([sequence]) == expected


@pytest.mark.parametrize(
    ["sequence", "expected"],
    [
        (")", 1),
        ("()())", 5),
    ],
)
def test_part_two(sequence, expected):
    assert part_two([sequence]) == expected
