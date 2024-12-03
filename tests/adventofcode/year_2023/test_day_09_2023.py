import pytest

from adventofcode.year_2023.day_09_2023 import (
    find_next_in_sequence,
    parse_input,
    parse_sequence,
    part_one,
    part_two,
)

test_input = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


@pytest.mark.parametrize(
    ["sequence", "expected"],
    [
        ("0 3 6 9 12 15", [0, 3, 6, 9, 12, 15]),
        ("1 3 6 10 15 21", [1, 3, 6, 10, 15, 21]),
        ("10 13 16 21 30 45", [10, 13, 16, 21, 30, 45]),
        ("-1 -20 -300 400", [-1, -20, -300, 400]),
        (
            "5 1 -3 -7 -11 -15 -19 -23 -27 -31 -35 -39 -43 -47 -51 -55 -59 -63 -67 -71 -75",
            [
                5,
                1,
                -3,
                -7,
                -11,
                -15,
                -19,
                -23,
                -27,
                -31,
                -35,
                -39,
                -43,
                -47,
                -51,
                -55,
                -59,
                -63,
                -67,
                -71,
                -75,
            ],
        ),
    ],
)
def test_parse_sequence(sequence, expected):
    assert list(parse_sequence(sequence)) == expected


def test_parse_input():
    assert len(list(parse_input(test_input))) == 3


@pytest.mark.parametrize(
    ["sequence", "expected"],
    [
        (
            [
                13,
                23,
                46,
                97,
                206,
                436,
                919,
                1924,
                3971,
                8016,
                15765,
                30243,
                56875,
                105604,
                195153,
                361805,
                677725,
                1289089,
                2494076,
                4898137,
                9713336,
            ],
            19316320,
        ),
        (
            [
                -7,
                6,
                44,
                130,
                309,
                672,
                1404,
                2864,
                5712,
                11113,
                21082,
                39112,
                71386,
                129156,
                233312,
                422773,
                769075,
                1400300,
                2538072,
                4551386,
                8029995,
            ],
            13877188,
        ),
        (
            [
                5,
                1,
                -3,
                -7,
                -11,
                -15,
                -19,
                -23,
                -27,
                -31,
                -35,
                -39,
                -43,
                -47,
                -51,
                -55,
                -59,
                -63,
                -67,
                -71,
                -75,
            ],
            -79,
        ),
    ],
)
def test_find_next_in_sequence(sequence, expected):
    assert find_next_in_sequence(sequence, []) == expected


def test_part_one():
    assert part_one(test_input) == 114


def test_part_two():
    assert part_two(test_input) == 2
