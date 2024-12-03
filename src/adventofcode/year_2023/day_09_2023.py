import re
from collections.abc import Iterable
from functools import partial
from itertools import pairwise
from operator import itemgetter

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

pattern = re.compile("-?\\d+")


def parse_sequence(sequence: str) -> Iterable[int]:
    return map(int, pattern.findall(sequence))


def parse_sequence_backwards(sequence: str) -> Iterable[int]:
    return reversed(list(map(int, pattern.findall(sequence))))


def parse_input(data: list[str]) -> Iterable[Iterable[int]]:
    return map(parse_sequence, data)


def parse_input_reversed(data: list[str]) -> Iterable[Iterable[int]]:
    return map(parse_sequence_backwards, data)


def find_next_in_sequence(
    sequence: Iterable[int], lines: list[list[int]] | None
) -> int:
    numbers = list(sequence)
    lines = [numbers] if lines is None or len(lines) == 0 else lines
    differences = [y - x for (x, y) in pairwise(numbers)]
    lines.append(differences)

    if any(differences):
        return find_next_in_sequence(differences, lines)

    return sum(map(itemgetter(-1), lines))


def solve_part_one(data: list[str]) -> int:
    parsed_input = parse_input(data)
    find_next = partial(find_next_in_sequence, lines=None)
    return sum(map(find_next, parsed_input))


def solve_part_two(data: list[str]) -> int:
    parsed_input = parse_input_reversed(data)
    find_next = partial(find_next_in_sequence, lines=None)
    return sum(map(find_next, parsed_input))


@register_solution(2023, 9, 1)
def part_one(input_data: list[str]):
    answer = solve_part_one(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 9, 1)

    return answer


@register_solution(2023, 9, 2)
def part_two(input_data: list[str]):
    answer = solve_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 9, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 9)
    part_one(data)
    part_two(data)
