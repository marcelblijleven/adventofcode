from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def _check_vowels(line: str) -> bool:
    a = line.count('a')
    e = line.count('e')
    i = line.count('i')
    o = line.count('o')
    u = line.count('u')

    return a + e + i + o + u >= 3


def _check_forbidden_characters(line: str) -> bool:
    for chars in ['ab', 'cd', 'pq', 'xy']:
        if chars in line:
            return False

    return True


def _check_double_characters(line: str) -> bool:
    for i, char in enumerate(line):
        try:
            if char == line[i + 1]:
                return True
        except IndexError:
            pass

    return False


def is_nice(line: str) -> bool:
    return _check_double_characters(line) and _check_forbidden_characters(line) and _check_vowels(line)


@solution_timer(2015, 5, 1)
def part_one(input_data: List[str]):
    answer = len([line for line in input_data if is_nice(line)])

    if not answer:
        raise SolutionNotFoundException(2015, 5, 1)

    return answer


@solution_timer(2015, 5, 2)
def part_two(input_data: List[str]):
    return None


if __name__ == '__main__':
    data = get_input_for_day(2015, 5)
    part_one(data)
    part_two(data)
