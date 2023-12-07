import re
from itertools import starmap
from math import prod

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def parse_input(data: list[str]) -> list[tuple[int, int]]:
    """
    Zip the time and distance values into a list of tuples of int
    """
    pattern = re.compile("\\d+")
    times = map(int, pattern.findall(data[0]))
    distances = map(int, pattern.findall(data[1]))
    return list(zip(times, distances, strict=True))


def calculate_distance(hold: int, max_time: int) -> int:
    """
    Calculate the distance you can travel within the max limit
    for the given hold duration
    """
    if hold in (0, max_time):
        return 0

    return (max_time - hold) * hold


def calculate_ways_to_win(duration: int, farthest_distance: int) -> int:
    """
    Calculate ways to beat the current farthest distance
    """
    possibilities = zip(range(duration + 1), [duration] * duration, strict=True)
    distances = starmap(calculate_distance, possibilities)
    winning_distances = filter(lambda x: x > farthest_distance, distances)
    return len(list(winning_distances))


def calculate_margin_of_error(data: list[str]) -> int:
    """
    Calculate the margin of error
    """
    parsed_input = parse_input(data)
    return prod(starmap(calculate_ways_to_win, parsed_input))


@register_solution(2023, 6, 1)
def part_one(input_data: list[str]):
    answer = calculate_margin_of_error(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 6, 1)

    return answer


@register_solution(2023, 6, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2023, 6, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 6)
    part_one(data)
    part_two(data)
