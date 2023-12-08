import re
from collections import deque

from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def parse_input(data: list[str]) -> tuple[deque, dict[str, tuple[str, str]]]:
    instructions = deque(data[0])
    paths: dict[str, tuple[str, str]] = {}
    pattern = re.compile("[A-Z]{3}")

    for line in data[2:]:
        key, left, right = pattern.findall(line)
        paths[key] = (left, right)

    return instructions, paths


def follow_instructions(data: list[str]) -> int:
    instructions, paths = parse_input(data)
    current_position = "AAA"
    steps = 0

    while True:
        direction = 0 if instructions[0] == "L" else 1
        current_position = paths[current_position][direction]
        steps += 1

        if current_position == "ZZZ":
            break

        instructions.rotate(-1)

    return steps


@register_solution(2023, 8, 1)
def part_one(input_data: list[str]):
    answer = follow_instructions(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 8, 1)

    return answer


@register_solution(2023, 8, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2023, 8, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 8)
    part_one(data)
    part_two(data)
