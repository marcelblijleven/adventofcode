from adventofcode.year_2020.day_02_2020 import part_one, part_two


def test_part_one():
    test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert 2 == part_one(test_data)


def test_part_two():
    test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    assert 1 == part_two(test_data)
