from adventofcode.year_2024.day_01_2024 import part_one, part_two

test_input = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]


def test_part_one():
    assert part_one(test_input) == 11


def test_part_two():
    assert part_two(test_input) == 31
