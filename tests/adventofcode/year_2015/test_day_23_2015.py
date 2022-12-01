import pytest
from adventofcode.year_2015.day_23_2015 import (
    parse_instruction,
    run_program,
    get_input_for_day,
)


def test_part_one():
    assert run_program(get_input_for_day(2015, 23), {"a": 0, "b": 0}) == 255


def test_part_two():
    assert run_program(get_input_for_day(2015, 23), {"a": 1, "b": 0}) == 334


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("inc a", ("inc", "a")),
        ("tpl a", ("tpl", "a")),
        ("jmp +19", ("jmp", "+19")),
        ("jmp -7", ("jmp", "-7")),
    ],
)
def test_parse_instruction(line, expected):
    assert parse_instruction(line) == expected
