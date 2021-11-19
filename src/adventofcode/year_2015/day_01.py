from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


@solution_timer(2015, 1, 1)
def part_one(input_data: List[str]) -> int:
    floor = 0

    for char in input_data[0]:
        if char == '(':
            floor += 1
        else:
            floor -= 1

    return floor


@solution_timer(2015, 1, 2)
def part_two(input_data: List[str]) -> int:
    floor = 0

    for i, char in enumerate(input_data[0]):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        print(floor)
        if floor == -1:
            return i + 1

    raise SolutionNotFoundException(2015, 1, 2)


if __name__ == '__main__':
    data = get_input_for_day(2015, 1)
    part_one(data)
    part_two(data)
