import pytest

from adventofcode.year_2021.day_06_2021 import (
    Fish,
    count_fish_after_days,
    count_fish_faster,
    get_starting_fish,
    iterate_day,
    part_one,
    part_two,
)

test_input = [
    "3,4,3,1,2",
]


def test_get_starting_fish():
    fish = [Fish(3), Fish(4), Fish(3), Fish(1), Fish(2)]
    assert list(get_starting_fish(test_input)) == fish


@pytest.mark.parametrize(
    ["days", "expected"],
    [
        (18, 26),
        (80, 5934),
    ],
)
def test_iterate_day(days, expected):
    fish = [Fish(3), Fish(4), Fish(3), Fish(1), Fish(2)]

    for _ in range(days):
        fish = iterate_day(fish)

    assert len(fish) == expected


@pytest.mark.parametrize(
    ["days", "expected"],
    [
        (18, 26),
        (80, 5934),
    ],
)
def test_count_fish_after_days(days, expected):
    assert count_fish_after_days(test_input, days) == expected


@pytest.mark.parametrize(
    ["days", "expected"],
    [
        (18, 26),
        (80, 5934),
    ],
)
def test_count_fish_faster(days, expected):
    assert count_fish_faster(test_input, days) == expected


def test_part_one():
    answer = part_one(test_input)
    assert answer == 5934


def test_part_two():
    answer = part_two(test_input)
    assert answer == 26984457539
