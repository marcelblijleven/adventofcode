from collections import Counter
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def input_to_list_of_list(input_data: List[str]) -> List[List[str]]:
    lists: List[List[str]] = []

    for line in input_data:
        lists.append([num for num in line])

    return lists


def merge_lists(lists: List[List[str]]) -> list[tuple[str]]:
    merged = zip(*lists)
    return list(merged)  # type: ignore


def get_power_consumption(values: list[tuple[str]]) -> int:
    gamma_rate = ''
    epsilon_rate = ''

    for value in values:
        counter = Counter(value)
        gamma_rate += str(counter.most_common()[0][0])
        epsilon_rate += str(counter.most_common()[1][0])

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_life_support_rating(values: list[tuple[str]]):
    ...


@solution_timer(2021, 3, 1)
def part_one(input_data: List[str]):
    lists = input_to_list_of_list(input_data)
    merged = list(merge_lists(lists))
    get_power_consumption(merged)
    answer = get_power_consumption(merged)

    if not answer:
        raise SolutionNotFoundException(2021, 3, 1)

    return answer


@solution_timer(2021, 3, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 3)
    part_one(data)
    part_two(data)
