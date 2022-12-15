import pytest

from adventofcode.year_2022.day_13_2022 import compare_pairs, part_one, part_two

test_input = [
    "[1,1,3,1,1]",
    "[1,1,5,1,1]",
    "",
    "[[1],[2,3,4]]",
    "[[1],4]",
    "",
    "[9]",
    "[[8,7,6]]",
    "",
    "[[4,4],4,4]",
    "[[4,4],4,4,4]",
    "",
    "[7,7,7,7]",
    "[7,7,7]",
    "",
    "[]",
    "[3]",
    "",
    "[[[]]]",
    "[[]]",
    "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]",
    "[1,[2,[3,[4,[5,6,0]]]],8,9]",
]


@pytest.mark.parametrize(
    ["left", "right", "expected"],
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], True),
        ([[1], [2, 3, 4]], [[1], 4], True),
        ([9], [[8, 7, 6]], False),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], True),
        ([7, 7, 7, 7], [7, 7, 7], False),
        ([], [3], True),
        ([[[]]], [[]], False),
        (
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            False,
        ),
    ],
)
def test_compare_pairs(left, right, expected):
    assert compare_pairs(left, right) == expected


def test_part_one():
    assert part_one(test_input) == 13


def test_part_two():
    assert part_two(test_input) == 140
