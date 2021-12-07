import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_07_2021 import part_two, part_one, get_crabs, move_to_position, try_all_positions

test_input = [
    '16,1,2,0,4,2,7,1,2,14',
]


def test_get_crabs():
    assert get_crabs(test_input) == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.mark.parametrize(['position', 'expected'], [
    (1, 41),
    (2, 37),
    (3, 39),
    (10, 71)
])
def test_move_to_position(position, expected):
    crabs = get_crabs(test_input)
    assert move_to_position(crabs, position=position) == expected


def test_try_all_positions():
    crabs = get_crabs(test_input)
    assert try_all_positions(crabs) == 37



def test_part_one():
    answer = part_one(get_input_for_day(2021, 7))
    assert False


def test_part_two():
    answer = part_two(get_input_for_day(2021, 7))
    assert False
