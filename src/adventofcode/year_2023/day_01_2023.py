from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_value(line: str) -> int:
    left: str | None = None
    right: str | None = None

    for char in line:
        if char.isdigit():
            right = char
            if left is None:
                left = char

    return int(left + right)


def get_calibration_values(lines: list[str]) -> int:
    total: int = 0

    for line in lines:
        total += get_calibration_value(line)

    return total


@register_solution(2023, 1, 1)
def part_one(input_data: list[str]):
    answer = get_calibration_values(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 1, 1)

    return answer


@register_solution(2023, 1, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2023, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)
