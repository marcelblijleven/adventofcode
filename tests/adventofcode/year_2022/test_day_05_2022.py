from adventofcode.year_2022.day_05_2022 import (
    execute_instruction,
    execute_instruction_9001,
    get_number_of_crates,
    move_crates,
    parse_crates,
    parse_crates_option_two,
    parse_instructions,
    part_one,
    part_two,
)

test_input = [
    "    [D]",
    "[N] [C]",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_get_number_of_crates():
    assert get_number_of_crates(len("[N] [D] [M] [G] [Z] [F] [W] [S] [S]")) == 9
    assert get_number_of_crates(len("[Z] [M] [P]")) == 3


def test_parse_crates():
    crate_input = test_input[:4]
    crates = parse_crates(crate_input)
    assert list(crates[1]) == ["Z", "N"]
    assert list(crates[2]) == ["M", "C", "D"]
    assert list(crates[3]) == ["P"]


def test_parse_instructions():
    instructions_input = test_input[4:]

    for instruction in parse_instructions(instructions_input):
        print(type(instruction), instruction)  # noqa


def test_execute_instructions():
    crates = parse_crates(test_input[:4])
    instruction = (1, 2, 1)

    assert list(crates[1]) == ["Z", "N"]
    assert list(crates[2]) == ["M", "C", "D"]
    assert list(crates[3]) == ["P"]

    execute_instruction(crates, instruction)
    assert list(crates[1]) == ["Z", "N", "D"]
    assert list(crates[2]) == ["M", "C"]
    assert list(crates[3]) == ["P"]


def test_execute_instructions_9001():
    crates = parse_crates(test_input[:4])
    instruction = (1, 2, 1)

    assert list(crates[1]) == ["Z", "N"]
    assert list(crates[2]) == ["M", "C", "D"]
    assert list(crates[3]) == ["P"]

    execute_instruction_9001(crates, instruction)
    assert list(crates[1]) == ["Z", "N", "D"]
    assert list(crates[2]) == ["M", "C"]
    assert list(crates[3]) == ["P"]

    instruction = (3, 1, 3)
    execute_instruction_9001(crates, instruction)
    assert list(crates[1]) == []
    assert list(crates[2]) == ["M", "C"]
    assert list(crates[3]) == ["P", "Z", "N", "D"]


def test_parse_crates_option_two():
    crates = parse_crates(test_input[:4])
    crates_two = parse_crates_option_two(test_input[:4])

    for key, value in crates.items():
        assert crates_two[key] == value


def test_move_crates():
    assert "CMZ" == move_crates(test_input, execute_instruction)


def test_move_crates_part_two():
    assert "MCD" == move_crates(test_input, execute_instruction_9001)


def test_part_one():
    assert part_one(test_input) == "CMZ"


def test_part_two():
    assert part_two(test_input) == "MCD"
