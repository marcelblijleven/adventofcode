import math
import re
from collections import deque
from functools import reduce

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def parse_input(data: list[str]) -> tuple[deque, dict[str, tuple[str, str]]]:
    instructions = deque(data[0])
    paths: dict[str, tuple[str, str]] = {}
    pattern = re.compile("[A-Z0-9]{3}")

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


def highest_common_multiple(num_a: int, num_b: int) -> int:
    return num_a * num_b // math.gcd(num_a, num_b)


def find_end_as_ghost(
    starting_position: str, instructions: deque[str], paths: dict[str, tuple[str, str]]
) -> int:
    """
    Count how many staps it will take to arrive at a location that ends with Z
    """
    steps = 0
    current_location = starting_position

    while not current_location.endswith("Z"):
        direction = 0 if instructions[0] == "L" else 1
        current_location = paths[current_location][direction]
        steps += 1
        instructions.rotate(-1)

    return steps


def follow_instructions_as_a_ghost(data: list[str]) -> int:
    """
    The solution for part one will not work here, it will take too much time.
    Find the steps to the end for all starting position and then use the highest common multiple
    """
    instructions, paths = parse_input(data)
    starting_positions = list(filter(lambda k: k.endswith("A"), paths.keys()))
    steps_required: list[int] = []

    for position in starting_positions:
        steps_required.append(find_end_as_ghost(position, instructions, paths))

    return reduce(highest_common_multiple, steps_required)


@register_solution(2023, 8, 1)
def part_one(input_data: list[str]):
    answer = follow_instructions(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 8, 1)

    return answer


@register_solution(2023, 8, 2)
def part_two(input_data: list[str]):
    answer = follow_instructions_as_a_ghost(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 8, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 8)
    part_one(data)
    part_two(data)
