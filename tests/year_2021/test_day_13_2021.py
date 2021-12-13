import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2021.day_13_2021 import part_two, part_one, fold_position_along_y, fold_position_along_x, \
    parse_input, fold_paper

test_input = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
]


@pytest.mark.parametrize(['position', 'fold_y', 'expected'], [
    ((2, 9), 5, (2, 1)),
    ((2, 8), 5, (2, 2)),
    ((2, 7), 5, (2, 3)),
    ((2, 6), 5, (2, 4)),
    ((2, 9), 4, (2, -1)),
    ((2, 8), 4, (2, 0)),
    ((2, 7), 4, (2, 1)),
    ((2, 6), 4, (2, 2)),
])
def test_fold_along_y(position, fold_y, expected):
    assert fold_position_along_y(position, fold_y) == expected


@pytest.mark.parametrize(['position', 'fold_x', 'expected'], [
    ((9, 2), 5, (1, 2)),
    ((8, 2), 5, (2, 2)),
    ((7, 2), 5, (3, 2)),
    ((6, 2), 5, (4, 2)),
    ((9, 2), 4, (-1, 2)),
    ((8, 2), 4, (0, 2)),
    ((7, 2), 4, (1, 2)),
    ((6, 2), 4, (2, 2)),
])
def test_fold_along_x(position, fold_x, expected):
    assert fold_position_along_x(position, fold_x) == expected


def test_fold_paper_invalid_instructions():
    with pytest.raises(ValueError) as wrapped_e:
        fold_paper({}, ('z', 4))

    assert str(wrapped_e.value) == 'invalid instruction received: (\'z\', 4)'


def test_parse_input():
    paper, instructions = parse_input(test_input)
    assert paper == {
        (0, 3): '#',
        (0, 13): '#',
        (0, 14): '#',
        (1, 10): '#',
        (2, 14): '#',
        (3, 0): '#',
        (3, 4): '#',
        (4, 1): '#',
        (4, 11): '#',
        (6, 0): '#',
        (6, 10): '#',
        (6, 12): '#',
        (8, 4): '#',
        (8, 10): '#',
        (9, 0): '#',
        (9, 10): '#',
        (10, 4): '#',
        (10, 12): '#'
    }

    assert instructions == [('y', 7), ('x', 5)]


def test_part_one():
    assert part_one(test_input) == 17


def test_part_two():
    assert part_two(get_input_for_day(2021, 13)) == """
███   ██  ████ █    ███  █  █ ████ ███ 
█  █ █  █    █ █    █  █ █  █ █    █  █
█  █ █      █  █    ███  ████ ███  █  █
███  █ ██  █   █    █  █ █  █ █    ███ 
█ █  █  █ █    █    █  █ █  █ █    █   
█  █  ███ ████ ████ ███  █  █ █    █   """  # noqa
