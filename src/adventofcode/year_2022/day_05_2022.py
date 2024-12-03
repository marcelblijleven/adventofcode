import re
import string
from collections import defaultdict
from collections.abc import Callable, Generator

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

INSTRUCTIONS_PATTERN = re.compile(r"(\d+)")


def get_number_of_crates(len_of_line: int) -> int:
    """
    Get number of crates.
    The length of the provided line will be divided by 4 (each crate consists of 3
    characters + a space) and rounded up to get the number of crates
    """
    return round(len_of_line / 4)


def parse_crates(lines: list[str]) -> defaultdict[int, list[str]]:
    """
    Parse crate part of input, crate letters are at positions:
    1, 5, 9, 13, 17, 21, 25, 29, 33
    (1, 5, 9 for test input)

    There are max 9 stacks of crates
    """
    stacks: defaultdict[int, list[str]] = defaultdict(list)
    number_of_crates = max(int(x) for x in INSTRUCTIONS_PATTERN.findall(lines[-1]))

    indices = [1 + (idx * 4) for idx in range(0, number_of_crates)]

    for row in lines:
        for stack_no, idx in enumerate(indices):
            if idx > len(row):
                break
            try:
                string.ascii_uppercase.index(value := row[idx])
                stacks[stack_no + 1].insert(0, value)
            except (ValueError, IndexError):
                pass

    return stacks


def parse_crates_option_two(lines: list[str]) -> defaultdict[int, list[str]]:
    """
    Parse crate part of input, crate letters are at positions:
    1, 5, 9, 13, 17, 21, 25, 29, 33
    (1, 5, 9 for test input)

    There are max 9 stacks of crates

    Different approach to filling the stacks, 0 to 2ms faster
    """
    stacks: defaultdict[int, list[str]] = defaultdict(list)
    number_of_crates = max(int(x) for x in INSTRUCTIONS_PATTERN.findall(lines[-1]))

    indices = {1 + (idx * 4): idx + 1 for idx in range(number_of_crates)}

    for row in lines:
        for idx, value in enumerate(row):
            if value.isalpha():
                stacks[indices[idx]].insert(0, value)

    return stacks


def parse_instructions(lines: list[str]) -> Generator[tuple[int, ...], None, None]:
    """Parse a line of instructions to a tuple of int"""
    for line in lines:
        if line:
            yield tuple([int(x) for x in INSTRUCTIONS_PATTERN.findall(line)])


def parse_input(input_data: list[str]) -> tuple[list[str], list[str]]:
    """Splits the input in a section for crates and a section for instructions"""
    crates: list[str] = []
    instructions_start: int = 0

    # read crates first
    for idx, row in enumerate(input_data):
        if not row:
            instructions_start = idx
            break

        crates.append(row)

    return crates, input_data[instructions_start:]


def execute_instruction(crates: defaultdict[int, list[str]], instructions) -> None:
    """Executes instructions for the CrateMover 9000"""
    amount, source, destination = instructions

    for _ in range(amount):
        try:
            crates[destination].append(crates[source].pop())
        except IndexError as exc:
            raise ValueError(
                f"tried to move a crate from an empty stack with instruction {instructions}"
            ) from exc


def execute_instruction_9001(crates: defaultdict[int, list[str]], instructions) -> None:
    """Executes instructions for the CrateMover 9001"""
    amount, source, destination = instructions

    crates[destination] += crates[source][-1 * amount :]
    crates[source] = crates[source][: -1 * amount]


def move_crates(
    input_data: list[str],
    executor_func: Callable[[defaultdict[int, list[str]], tuple[int, ...]], None],
) -> str:
    crates_input, instructions_input = parse_input(input_data)
    # crates = parse_crates(crates_input)
    crates = parse_crates_option_two(crates_input)

    for instruction in parse_instructions(instructions_input):
        executor_func(crates, instruction)

    output = ""
    for _, value in sorted(crates.items()):
        output += value[-1]

    return output


@register_solution(2022, 5, 1)
def part_one(input_data: list[str]):
    answer = move_crates(input_data, execute_instruction)

    if not answer:
        raise SolutionNotFoundError(2022, 5, 1)

    return answer


@register_solution(2022, 5, 2)
def part_two(input_data: list[str]):
    answer = move_crates(input_data, execute_instruction_9001)

    if not answer:
        raise SolutionNotFoundError(2022, 5, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 5)
    part_one(data)
    part_two(data)
