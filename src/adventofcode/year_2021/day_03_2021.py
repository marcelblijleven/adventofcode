from collections import Counter
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def input_to_list_of_list(input_data: List[str]) -> List[List[str]]:
    lists: List[List[str]] = []

    for line in input_data:
        lists.append([num for num in line])

    return lists


def merge_lists(lists: List[List[str]]) -> list[tuple[str]]:
    merged = zip(*lists)
    return list(merged)  # type: ignore


def change_list(input_data: List[str]) -> List[tuple[str]]:
    return merge_lists(input_to_list_of_list(input_data))


def get_power_consumption(values: list[tuple[str]]) -> int:
    gamma_rate = ''
    epsilon_rate = ''

    for value in values:
        counter = Counter(value)
        gamma_rate += str(counter.most_common()[0][0])
        epsilon_rate += str(counter.most_common()[1][0])

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def filter_list(input_data: List[str], use_most_common: bool, idx: int = 0) -> int:
    if len(input_data) == 1:
        return int(input_data[0], 2)

    if idx > 12:
        raise IndexError('index is higher than 12')

    values = change_list(input_data)
    count_results = Counter(values[idx]).most_common()

    if len(count_results) > 1 and count_results[0][1] != count_results[1][1]:
        target = str(count_results[0][0] if use_most_common else count_results[1][0])
    else:
        target = str(int(use_most_common))

    filtered_input_data = [i for i in input_data if i[idx] == str(target)]

    return filter_list(filtered_input_data, use_most_common, idx + 1)


def get_life_support(input_data: List[str]) -> int:
    oxygen_generator = filter_list(input_data, use_most_common=True)
    co2_scrubber = filter_list(input_data, use_most_common=False)
    return oxygen_generator * co2_scrubber


@register_solution(2021, 3, 1)
def part_one(input_data: List[str]):
    merged = change_list(input_data)
    answer = get_power_consumption(merged)

    if not answer:
        raise SolutionNotFoundException(2021, 3, 1)

    return answer


@register_solution(2021, 3, 2)
def part_two(input_data: List[str]):
    answer = get_life_support(input_data)

    if not answer:
        raise SolutionNotFoundException(2021, 3, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 3)
    part_one(data)
    part_two(data)
