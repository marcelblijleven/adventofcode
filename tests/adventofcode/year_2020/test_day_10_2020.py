from adventofcode.year_2020.day_10_2020 import find_differences, part_one, part_two

test_input = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]


def test_part_one():
    assert 22 * 10 == part_one(test_input)


def test_part_two():
    assert 19208 == part_two(test_input)


def test_find_differences():
    data = [1, 2, 3, 6, 8, 9]
    assert [1, 1, 1, 3, 2, 1, 3] == find_differences(data)


def test_find_differences_with_test_input():
    differences = find_differences(test_input)
    ones = differences.count(1)
    threes = differences.count(3)
    assert 22 == ones
    assert 10 == threes
