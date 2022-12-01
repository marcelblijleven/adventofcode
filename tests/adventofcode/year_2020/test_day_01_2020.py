from adventofcode.year_2020.day_01_2020 import part_one, part_two


def test_part_one():
    test_data = ["1721", "979", "366", "299", "675", "1456"]
    assert 514579 == part_one(test_data)


def test_part_two():
    test_data = ["1721", "979", "366", "299", "675", "1456"]
    assert 241861950 == part_two(test_data)
