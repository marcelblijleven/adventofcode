from typing import Set, Generator

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def groups(input_data: list[str]) -> Generator[list[str], None, None]:
    group = ""
    for line in input_data:
        if line:
            group += line
        else:
            yield sorted(list(set(list(group))))
            group = ""

    yield sorted(list(set(list(group))))


def groups_as_lists(input_data: list[str]) -> Generator[list[str], None, None]:
    group = []
    for line in input_data:
        if line:
            group.append(line)
        else:
            yield group
            group = []

    yield group


def get_all_answered(value: list[str]) -> Set[str]:
    s = set(value[0])

    for i in range(1, len(value)):
        s = s & set(value[i])

    return s


@register_solution(2020, 6, 1)
def part_one(input_data):
    total = 0

    for group in groups(input_data):
        total += len(group)

    if not total:
        raise SolutionNotFoundException(2020, 6, 1)

    return total


@register_solution(2020, 6, 2)
def part_two(input_data):
    total = 0

    for group in groups_as_lists(input_data):
        total += len(get_all_answered(group))

    if not total:
        raise SolutionNotFoundException(2020, 6, 2)

    return total


if __name__ == "__main__":
    data = get_input_for_day(2020, 6)
    part_one(data)
    part_two(data)
