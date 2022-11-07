import pytest

from adventofcode.year_2015.day_12_2015 import count_all_numbers, traverser


@pytest.mark.parametrize(
    ["value", "expected"],
    [
        ("[1, 2, 3]", 6),
        ("[1, {'c': 'red', 'b': 2}, 3]", 6),
        ("{'d': 'red', 'e': [1, 2, 3, 4], 'f': 5}", 15),
        ("[1, 'red', 5]", 6),
    ],
)
def test_count_all_numbers(value, expected):
    assert expected == count_all_numbers(value)


@pytest.mark.parametrize(
    ["value", "expected"],
    [
        ([1, 2, 3], 6),
        ([1, {"c": "red", "b": 2}, 3], 4),
        ({"d": "red", "e": [1, 2, 3, 4], "f": 5}, 0),
        ([1, "red", 5], 6),
    ],
)
def test_traverser(value, expected):
    assert expected == traverser(value)
