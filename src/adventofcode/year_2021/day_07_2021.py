from statistics import median
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.util.math_helpers import mean_floor, mean_ceil, gaussian_sum


def get_crabs(input_data: List[str]) -> List[int]:
    return list(map(int, input_data[0].split(',')))


def move_to_position(crabs: List[int], position: int) -> int:
    fuel = 0

    for crab in crabs:
        fuel += abs(crab - position)

    return fuel


def get_least_amount_of_fuel(crabs: List[int]) -> int:
    return move_to_position(crabs, int(median(crabs)))


def get_least_amount_of_fuel_part_two(crabs: List[int]) -> int:
    crabs.sort()
    mean_crabs_floor = mean_floor(crabs)
    mean_crabs_ceil = mean_ceil(crabs)

    return min(
        sum(gaussian_sum(abs(crab - mean_crabs_floor)) for crab in crabs),
        sum(gaussian_sum(abs(crab - mean_crabs_ceil)) for crab in crabs),
    )


def get_least_amount_of_fuel_part_two_slower(crabs: List[int]) -> int:
    crabs.sort()
    mid = crabs[len(crabs) // 2]

    fuel = sum(gaussian_sum(abs(crab - mid)) for crab in crabs)

    for position in range(min(crabs[mid:]), max(crabs) + 1):
        position_fuel = min(fuel, sum(gaussian_sum(abs(crab - position)) for crab in crabs))
        fuel = min(fuel, position_fuel)

    return fuel


def try_all_positions(crabs: List[int]) -> int:
    fuel = int(1e10)
    crabs.sort()

    for position in range(min(crabs), max(crabs) + 1):
        position_fuel = move_to_position(crabs, position)

        if position_fuel > fuel:
            return fuel

        fuel = min(fuel, position_fuel)

    return fuel


@register_solution(2021, 7, 1)
def part_one(input_data: List[str]):
    crabs = get_crabs(input_data)
    answer = get_least_amount_of_fuel(crabs)

    if not answer:
        raise SolutionNotFoundException(2021, 7, 1)

    return answer


@register_solution(2021, 7, 2)
def part_two(input_data: List[str]):
    crabs = get_crabs(input_data)
    answer = get_least_amount_of_fuel_part_two(crabs)

    if not answer:
        raise SolutionNotFoundException(2021, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 7)
    part_one(data)
    part_two(data)
    get_crabs(data)
