import pytest

from adventofcode.year_2021.day_07_2021 import (
    get_crabs,
    get_least_amount_of_fuel,
    get_least_amount_of_fuel_part_two,
    get_least_amount_of_fuel_part_two_slower,
    move_to_position,
    part_one,
    part_two,
    try_all_positions,
)

test_input = [
    "16,1,2,0,4,2,7,1,2,14",
]


def test_get_crabs():
    assert get_crabs(test_input) == [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


@pytest.mark.parametrize(
    ["position", "expected"], [(1, 41), (2, 37), (3, 39), (10, 71)]
)
def test_move_to_position(position, expected):
    crabs = get_crabs(test_input)
    assert move_to_position(crabs, position=position) == expected


def test_try_all_positions():
    crabs = get_crabs(test_input)
    assert try_all_positions(crabs) == 37


def test_get_least_amount_of_fuel():
    crabs = get_crabs(test_input)
    assert get_least_amount_of_fuel(crabs) == 37


def test_get_least_amount_of_fuel_part_two():
    crabs = get_crabs(test_input)
    assert get_least_amount_of_fuel_part_two(crabs) == 168


def test_get_least_amount_of_fuel_part_two_slower():
    crabs = get_crabs(test_input)
    assert get_least_amount_of_fuel_part_two_slower(crabs) == 168


def test_compare_part_two_solutions():
    crabs = get_crabs(test_input)
    assert get_least_amount_of_fuel_part_two_slower(
        crabs
    ) == get_least_amount_of_fuel_part_two(crabs)


def test_part_one():
    answer = part_one(test_input)
    assert answer == 37


def test_part_two():
    answer = part_two(test_input)
    assert answer == 168
