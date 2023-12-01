import pytest

from adventofcode.year_2015.day_16_2015 import (
    Aunt,
    all_properties_match,
    find_aunt_sue,
    find_aunt_sue_part_two,
    parse_lines,
)

test_input = [
    "Sue 1: children: 1, cars: 8, vizslas: 7",
    "Sue 2: akitas: 10, perfumes: 10, children: 5",
]


def test_parse_lines():
    aunts = parse_lines(test_input)

    assert aunts[0].name == "Sue 1"
    assert aunts[1].name == "Sue 2"
    assert aunts[0].kwargs == {"children": 1, "cars": 8, "vizslas": 7}
    assert aunts[1].kwargs == {"akitas": 10, "perfumes": 10, "children": 5}
    assert aunts[0].number == 1
    assert aunts[1].number == 2


@pytest.mark.parametrize(
    ["aunt", "expected"],
    [
        (Aunt("Sue 1", children=1, cats=7, samoyeds=2), False),
        (Aunt("Sue 2", children=3, cats=7, samoyeds=2), True),
        (Aunt("Sue 3", akitas=0, goldfish=5, trees=3), True),
    ],
)
def test_all_properties_match(aunt, expected):
    assert all_properties_match(aunt) == expected


def test_find_aunt_sue():
    aunts = [
        Aunt("Sue 1", children=1, cats=7, samoyeds=2),
        Aunt("Sue 2", children=3, cats=7, samoyeds=2),
        Aunt("Sue 3", akitas=0, goldfish=5, trees=4),
    ]

    assert find_aunt_sue(aunts).name == "Sue 2"


def test_find_aunt_sue_part_two():
    aunts = [
        Aunt("Sue 1", children=1, cats=7, samoyeds=2),
        Aunt("Sue 2", children=3, cats=7, samoyeds=2),
        Aunt("Sue 3", akitas=0, goldfish=10, trees=1),
        Aunt("Sue 4", akitas=0, goldfish=2, trees=10),
    ]

    assert find_aunt_sue_part_two(aunts).name == "Sue 4"
