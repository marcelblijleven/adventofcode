import pytest
from adventofcode.year_2015.day_05 import is_nice, is_nice_part_two


@pytest.mark.parametrize(['line', 'expected'], [
    ('ugknbfddgicrmopn', True),
    ('aaa', True),
    ('jchzalrnumimnmhp', False),
    ('haegwjzuvuyypxyu', False),
    ('dvszwmarrgswjxmb', False),
])
def test_is_nice(line, expected):
    assert expected == is_nice(line)
