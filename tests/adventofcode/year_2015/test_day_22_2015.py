from adventofcode.year_2015.day_22_2015 import fight


def test_part_one():
    assert fight(50, 500, 58, 9, False) == 1269


def test_part_two():
    assert fight(50, 500, 58, 9, True) == 1309
