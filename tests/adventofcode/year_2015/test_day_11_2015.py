import pytest

from adventofcode.year_2015.day_11_2015 import is_valid


@pytest.mark.parametrize(
    ["password", "expected"],
    [
        ("hijklmmn", False),
        ("abbceffg", False),
        ("abbcegjk", False),
    ],
)
def test_iterate(password, expected):
    assert expected == is_valid(password)
