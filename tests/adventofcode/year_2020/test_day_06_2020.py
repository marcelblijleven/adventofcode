from adventofcode.year_2020.day_06_2020 import part_one, part_two

test_input = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
]


def test_part_one():
    assert 11 == part_one(test_input)


def test_part_two():
    assert 6 == part_two(test_input)
