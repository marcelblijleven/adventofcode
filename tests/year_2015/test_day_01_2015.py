import pytest
from adventofcode.year_2015.day_01_2015 import part_one


@pytest.mark.parametrize(['sequence', 'expected'], [
    ('(())', 0),
    ('()()', 0),
    ('))(((((', 3)
])
def test_part_one(sequence, expected):
    assert expected == part_one([sequence])
