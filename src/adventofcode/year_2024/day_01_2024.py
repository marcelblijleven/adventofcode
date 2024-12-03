from collections import Counter

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def parse_input(input_data: list[str]) -> tuple[list, list]:
    left_list: list[int] = []
    right_list: list[int] = []

    for row in input_data:
        left, right = row.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    return sorted(left_list), sorted(right_list)


def calculate_distances(data: tuple[list[int], list[int]]) -> int:
    total = 0
    for left, right in zip(*data, strict=True):
        total += abs(left - right)

    return total


def calculate_similarity(data: tuple[list[int], list[int]]) -> int:
    total = 0
    left_list, right_list = data
    right_counter = Counter(right_list)

    for num in left_list:
        total += right_counter[num] * num

    return total


@register_solution(2024, 1, 1)
def part_one(input_data: list[str]):
    parsed_input = parse_input(input_data)
    answer = calculate_distances(parsed_input)

    if not answer:
        raise SolutionNotFoundError(2024, 1, 1)

    return answer


@register_solution(2024, 1, 2)
def part_two(input_data: list[str]):
    parsed_input = parse_input(input_data)
    answer = calculate_similarity(parsed_input)

    if not answer:
        raise SolutionNotFoundError(2024, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2024, 1)
    part_one(data)
    part_two(data)
