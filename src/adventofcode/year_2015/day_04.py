import hashlib
from typing import List, Dict


from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def find_number(secret: str, target: str, range_size: int) -> int:
    for i in range(range_size):
        h = hashlib.md5((secret + str(i)).encode('utf-8')).hexdigest()
        if h[:len(target)] == target:
            return i


@solution_timer(2015, 4, 1)
def part_one(input_data: List[str]) -> int:
    secret = input_data[0]
    number = find_number(secret, '00000', 1000000)

    if not number:
        raise SolutionNotFoundException(2015, 4, 1)

    return number


@solution_timer(2015, 4, 2)
def part_two(input_data: List[str]) -> int:
    secret = input_data[0]
    number = find_number(secret, '000000', 10000000)

    if not number:
        raise SolutionNotFoundException(2015, 4, 1)

    return number


if __name__ == '__main__':
    data = get_input_for_day(2015, 4)
    part_one(data)
    part_two(data)
