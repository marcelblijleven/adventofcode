from adventofcode.year_2022.day_04_2022 import (
    part_two,
    part_one,
    find_containing,
    does_contain,
    get_pairs,
    does_overlap,
    find_overlapping,
)

test_input = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def test_does_contain():
    assert does_contain((6, 6), (4, 6))
    assert does_contain((2, 8), (3, 7))
    assert not does_contain((2, 4), (6, 8))


def test_does_overlap():
    assert not does_overlap((2, 4), (6, 8))
    assert not does_overlap((2, 3), (4, 5))
    assert does_overlap((5, 7), (7, 9))
    assert does_overlap((2, 8), (3, 7))


def test_find_containing():
    assert find_containing(test_input) == 2


def test_find_overlapping():
    assert find_overlapping(test_input) == 4


def test_part_one():
    assert part_one(test_input) == 2


def test_part_two():
    assert part_two(test_input) == 4
