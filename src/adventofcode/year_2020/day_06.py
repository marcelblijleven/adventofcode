from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def groups(input_data: List[str]) -> List[str]:
    group = ''
    for line in input_data:
        if line:
            group += line
        else:
            yield sorted(list(set(list(group))))
            group = ''

    yield sorted(list(set(list(group))))


def groups_as_lists(input_data: List[str]) -> List[List[str]]:
    group = []
    for line in input_data:
        if line:
            group.append(line)
        else:
            yield group
            group = []

    yield group


def get_all_answered(value: List[str]) -> List[str]:
    s = set(value[0])

    for i in range(1, len(value)):
        s = s & set(value[i])

    return s


@solution_timer(2020, 6, 1)
def part_one(input_data):
    total = 0

    for group in groups(input_data):
        total += len(group)

    return total


@solution_timer(2020, 6, 2)
def part_two(input_data):
    total = 0

    for group in groups_as_lists(input_data):
        total += len(get_all_answered(group))

    return total


if __name__ == '__main__':
    data = get_input_for_day(2020, 6)
    part_one(data)
    part_two(data)
