from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def decipher_xmas(preamble: int, numbers: List[int]) -> int:
    idx = preamble

    while preamble < len(numbers):
        preamble_check = numbers[idx - preamble:idx]
        need = numbers[idx]
        seen = []
        is_valid = False
        for num in preamble_check:
            seen.append(num)
            if need - num in seen:
                is_valid = True
                break

        if not is_valid:
            return numbers[idx]

        idx += 1

    raise ValueError('xmas could not by deciphered')


@solution_timer(2020, 9, 1)
def part_one(input_data: List[str]):
    preamble = 25
    int_data = list(map(int, input_data))
    answer = decipher_xmas(preamble, int_data)

    if not answer:
        raise SolutionNotFoundException(2020, 9, 1)

    return answer


def find_group_sum(numbers: List[int], target: int) -> List[int]:
    for left_edge in range(len(numbers)):
        for right_edge in range(len(numbers)):
            window = numbers[left_edge:right_edge]
            if sum(window) == target:
                return window

    raise ValueError('group sum not found')


@solution_timer(2020, 9, 2)
def part_two(input_data: List[str]):
    preamble = 25
    int_data = list(map(int, input_data))
    wrong_number = decipher_xmas(preamble, int_data)
    group = find_group_sum(int_data, wrong_number)

    if not group:
        raise SolutionNotFoundException(2020, 9, 2)

    return min(group) + max(group)


if __name__ == '__main__':
    data = get_input_for_day(2020, 9)
    part_one(data)
    part_two(data)
