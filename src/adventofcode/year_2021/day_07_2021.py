from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def get_crabs(input_data: List[str]) -> List[int]:
    return list(map(int, input_data[0].split(',')))


def move_to_position(crabs: List[int], position: int) -> int:
    fuel = 0

    for crab in crabs:
        fuel += abs(crab - position)

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


@solution_timer(2021, 7, 1)
def part_one(input_data: List[str]):
    crabs = get_crabs(input_data)
    answer = try_all_positions(crabs)

    if not answer:
        raise SolutionNotFoundException(2021, 7, 1)

    return answer


@solution_timer(2021, 7, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 7, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 7)
    part_one(data)
    part_two(data)
    get_crabs(data)
