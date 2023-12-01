from adventofcode.year_2022.day_01_2022 import find_most_calories, part_one, part_two

test_input = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


def test_find_elf_with_most_calories():
    assert find_most_calories(test_input) == 24000


def test_part_one():
    assert part_one(test_input) == 24000


def test_part_two():
    assert part_two(test_input) == 45000
