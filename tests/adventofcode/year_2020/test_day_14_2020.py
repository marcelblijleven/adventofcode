import pytest

from adventofcode.year_2020.day_14_2020 import (
    apply_mask_to_address,
    apply_mask_to_value,
    parse_program,
    part_one,
    part_two,
)

test_input = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0",
]

test_input_part_two = [
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1",
]


def test_parse_program():
    expected_memory = {7: 101, 8: 64}
    assert parse_program(test_input) == expected_memory


@pytest.mark.parametrize(
    ["value", "mask", "expected"],
    [
        (
            "000000000000000000000000000000001011",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            int("000000000000000000000000000001001001", 2),
        ),
        (
            "000000000000000000000000000001100101",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            int("000000000000000000000000000001100101", 2),
        ),
        (
            "000000000000000000000000000000000000",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            int("000000000000000000000000000001000000", 2),
        ),
    ],
)
def test_apply_mask_to_value(value, mask, expected):
    assert apply_mask_to_value(value, mask) == expected


def test_apply_mask_to_address():
    address = "000000000000000000000000000000101010"
    mask = "000000000000000000000000000000X1001X"
    expected = [
        int("000000000000000000000000000000011010", 2),
        int("000000000000000000000000000000011011", 2),
        int("000000000000000000000000000000111010", 2),
        int("000000000000000000000000000000111011", 2),
    ]
    assert sorted(apply_mask_to_address(address, mask)) == sorted(expected)

    address = "000000000000000000000000000000011010"
    mask = "00000000000000000000000000000000X0XX"
    expected = [
        int("000000000000000000000000000000010000", 2),
        int("000000000000000000000000000000010001", 2),
        int("000000000000000000000000000000010010", 2),
        int("000000000000000000000000000000010011", 2),
        int("000000000000000000000000000000011000", 2),
        int("000000000000000000000000000000011001", 2),
        int("000000000000000000000000000000011010", 2),
        int("000000000000000000000000000000011011", 2),
    ]
    assert sorted(apply_mask_to_address(address, mask)) == sorted(expected)


def test_part_one():
    answer = part_one(test_input)
    assert answer == 165


def test_part_two():
    answer = part_two(test_input_part_two)
    assert answer == 208
