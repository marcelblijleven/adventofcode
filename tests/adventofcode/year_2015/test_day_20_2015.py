import pytest

from adventofcode.year_2015.day_20_2015 import (
    most_presents_at_house,
    part_one,
    visit_houses,
    visit_houses_part_two,
)


@pytest.mark.parametrize(
    ["houses", "expected"],
    [
        ({1: 10, 2: 15, 3: 5}, 15),
        ({1: 10, 2: 10, 3: 3}, 10),
    ],
)
def test_most_presents_at_house(houses, expected):
    assert most_presents_at_house(houses) == expected


def test_visit_houses():
    assert visit_houses(10, 150) == 8
    assert visit_houses(1000, 15000) == 480


def test_visit_houses_part_two():
    assert visit_houses_part_two(10, 150) == 8
    assert visit_houses_part_two(1000, 15000) == 480


def test_part_one():
    assert part_one(["2500"]) == 96


def test_part_two():
    assert part_one(["2500"]) == 96
