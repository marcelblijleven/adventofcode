import pytest

from adventofcode.year_2015.day_02_2015 import get_surface, get_ribbon


@pytest.mark.parametrize(['line', 'expected'], [
    ('2x3x4', 58),
    ('1x1x10', 43)
])
def test_get_surface(line, expected):
    assert expected == get_surface(line)


@pytest.mark.parametrize(['line', 'expected'], [
    ('2x3x4', 34),
    ('1x1x10', 14)
])
def test_get_ribbon(line, expected):
    assert expected == get_ribbon(line)
