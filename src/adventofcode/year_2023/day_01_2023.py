from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
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

    if left is None or right is None:
        raise ValueError("invalid state")

    return int(left + right)


def get_calibration_value_with_words(line: str) -> int:
    left: str | None = None
    left_idx: int | None = None
    right: str | None = None
    right_idx: int | None = None

    for idx, char in enumerate(line):
        if char.isdigit():
            right = char
            right_idx = idx
            if left is None:
                left = char
                left_idx = idx

    for word, value in DIGITS.items():
        if (lfind := line.find(word)) != -1 and (left_idx is None or lfind < left_idx):
            left = value
            left_idx = lfind
        if (rfind := line.rfind(word)) != -1 and (
            right_idx is None or rfind > right_idx
        ):
            right = value
            right_idx = rfind

    if left is None or right is None:
        raise ValueError("invalid state")

    return int(left + right)


def get_calibration_values(lines: list[str], *, with_words: bool) -> int:
    total: int = 0

    if with_words:
        func = get_calibration_value_with_words
    else:
        func = get_calibration_value

    for line in lines:
        total += func(line)

    return total


@register_solution(2023, 1, 1)
def part_one(input_data: list[str]):
    answer = get_calibration_values(input_data, with_words=False)

    if not answer:
        raise SolutionNotFoundError(2023, 1, 1)

    return answer


@register_solution(2023, 1, 2)
def part_two(input_data: list[str]):
    answer = get_calibration_values(input_data, with_words=True)

    if not answer:
        raise SolutionNotFoundError(2023, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 1)
    part_one(data)
    part_two(data)
