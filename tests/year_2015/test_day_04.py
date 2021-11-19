import pytest
from adventofcode.year_2015.day_04 import find_number


@pytest.mark.parametrize(['secret', 'target', 'range_size', 'expected'], [
    ('abcdef', '00000', 1000000, 609043),
    ('pqrstuv', '00000', 10000000, 1048970),
])
def test_find_number(secret, target, range_size, expected):
    assert expected == find_number(secret, target, range_size)
