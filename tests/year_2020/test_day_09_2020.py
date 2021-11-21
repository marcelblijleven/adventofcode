from adventofcode.year_2020.day_09_2020 import decipher_xmas, find_group_sum

test_input = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_part_one():
    assert 127 == decipher_xmas(5, test_input)


def test_part_two():
    num = decipher_xmas(5, test_input)
    group = find_group_sum(test_input, num)
    assert 62 == min(group) + max(group)
