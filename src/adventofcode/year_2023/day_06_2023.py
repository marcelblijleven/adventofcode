import math
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


def parse_input_part_two(data: list[str]) -> tuple[int, int]:
    """
    Parse input to a single pair of duration and distance
    """
    pattern = re.compile("\\d+")
    duration = int("".join(pattern.findall(data[0])))
    distance = int("".join(pattern.findall(data[1])))
    return duration, distance


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
    possibilities = zip(range(duration), [duration] * duration, strict=True)
    distances = starmap(calculate_distance, possibilities)
    winning_distances = filter(lambda x: x > farthest_distance, distances)
    return len(list(winning_distances))


def calculate_ways_to_win_part_two(duration: int, farthest_distance: int) -> int:
    """
    Calculate ways to beat the current farthest distance
    """
    possibilities = zip(range(duration), [duration] * duration, strict=True)
    winning_distances: int = 0
    for possibility in possibilities:
        if calculate_distance(*possibility) > farthest_distance:
            winning_distances += 1

    return winning_distances


def calculate_margin_of_error(data: list[str]) -> int:
    """
    Calculate the margin of error
    """
    parsed_input = parse_input(data)
    return prod(starmap(calculate_ways_to_win, parsed_input))


def calculate_margin_of_error_part_two(data: list[str]) -> int:
    """
    Calculate the margin of error
    """
    parsed_input = parse_input_part_two(data)
    return calculate_ways_to_win(*parsed_input)


def calculate_margin_of_error_quadratic(data: list[str]) -> int:
    """
    I suspected that the outcome of calculate_distance for x was a parabola,
    when running calculate distance for x in range(12) with max time of 12 the values were:
    0, 11, 20, 27, 32, 35, 32, 27, 20, 11, 0.

    We can use a quadratic equation to solve the problem.
    By first calculating the discriminant and then the upper and lower bound.

    After calculating the bounds, we can add/subtract from that value until the
    distance is no longer a winning distance, each time it is, add 1 to total
    """
    duration, distance = parse_input_part_two(data)
    discriminant = duration * duration - 4 * distance
    lower_bound = math.ceil((-duration + math.sqrt(discriminant)) / -2)
    upper_bound = math.floor((-duration - math.sqrt(discriminant)) / -2)

    total = 0

    while calculate_distance(lower_bound - 1, duration) > distance:
        lower_bound = lower_bound - 1
        total += 1

    while calculate_distance(upper_bound + 1, duration) > distance:
        upper_bound = upper_bound + 1
        total += 1

    return upper_bound - lower_bound + 1


@register_solution(2023, 6, 1)
def part_one(input_data: list[str]):
    answer = calculate_margin_of_error(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 6, 1)

    return answer


@register_solution(2023, 6, 2)
def part_two(input_data: list[str]):
    answer = calculate_margin_of_error_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 6, 2)

    return answer


@register_solution(2023, 6, 2, version="quadratic")
def part_two_quadratic(input_data: list[str]):
    answer = calculate_margin_of_error_quadratic(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 6, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 6)
    part_one(data)
    part_two(data)
    part_two_quadratic(data)
