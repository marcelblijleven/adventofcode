import pytest

from adventofcode.year_2020.day_08_2020 import (
    correcting_run,
    isolation_run,
    parse_instruction,
    part_one,
    part_two,
    verify_correction,
)

test_input = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]


def test_part_one():
    assert 5 == part_one(test_input)


def test_part_two():
    assert 8 == part_two(test_input)


@pytest.mark.parametrize(
    ["instruction", "expected"],
    [
        ("nop +0", ("nop", 0)),
        ("acc +1", ("acc", 1)),
        ("acc -1", ("acc", -1)),
        ("jmp +1", ("jmp", 1)),
        ("jmp -1", ("jmp", -1)),
        ("jmp -99", ("jmp", -99)),
    ],
)
def test_parse_instruction(instruction, expected):
    assert expected == parse_instruction(instruction)


def test_isolation_run():
    instructions = list(map(parse_instruction, test_input))
    accumulator, _ = isolation_run(instructions)
    assert 5 == accumulator


def test_verify_correction():
    instructions = [
        ("jmp", 1),
        ("jmp", -1),
    ]

    assert verify_correction(instructions)


def test_correcting_run():
    instructions = list(map(parse_instruction, test_input))
    accumulator = correcting_run(instructions)
    assert 8 == accumulator
