from collections import defaultdict
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def find_differences(input_data: List[int]) -> List[int]:
    working_list = sorted([0] + input_data + [max(input_data) + 3])
    differences = [y - x for x, y in zip(working_list[:-1], working_list[1:])]
    return differences


@solution_timer(2020, 10, 1)
def part_one(input_data: List[str]):
    int_data = list(map(int, input_data))
    differences = find_differences(int_data)
    ones = differences.count(1)
    threes = differences.count(3)

    if not ones and not threes:
        raise SolutionNotFoundException(2020, 10, 1)

    return ones * threes


@solution_timer(2020, 10, 2)
def part_two(input_data: List[str]):
    int_data = list(map(int, input_data))
    jolts = sorted([0] + int_data + [max(int_data) + 3])
    cache = defaultdict(int, {0: 1})

    for a, b in zip(jolts[1:], jolts):
        cache[a] = cache[a - 3] + cache[a - 2] + cache[a - 1]

    answer = cache[jolts[-1]]

    if not answer:
        raise SolutionNotFoundException(2020, 10, 1)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2020, 10)
    part_one(data)
    part_two(data)
