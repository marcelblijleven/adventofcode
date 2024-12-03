import pytest

from adventofcode.year_2020.day_05_2020 import part_one

test_input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def test_part_one():
    assert 820 == part_one(test_input)


@pytest.mark.skip()
def test_part_two(): ...
