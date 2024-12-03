import math
import re
from itertools import permutations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

pair_pattern = re.compile(r"(\[\d+,\d+])")
single_number_pattern = re.compile(r"(\d+)")


def get_pair_level(pair_start: int, snailfish_number: str) -> int:
    sub_string = snailfish_number[:pair_start]
    opening_brackets = sub_string.count("[")
    closing_brackets = sub_string.count("]")
    return opening_brackets - closing_brackets


def get_pair_numbers(pair: str) -> tuple[int, int]:
    if not pair.startswith("[") or not pair.endswith("]"):
        raise ValueError(f"invalid pair: {pair}")

    pair = pair.lstrip("[").rstrip("]")
    left, right = pair.split(",")
    return int(left), int(right)


def apply_explode_update_left(number: int, sub_string: str) -> str:
    matches = list(single_number_pattern.finditer(sub_string))

    if not matches:
        return sub_string

    last_match = matches[-1]
    value = last_match.group()
    span = last_match.span()
    return f"{sub_string[:span[0]]}{int(value) + number}{sub_string[span[1]:]}"


def apply_explode_update_right(number: int, sub_string: str) -> str:
    matches = list(single_number_pattern.finditer(sub_string))

    if not matches:
        return sub_string

    first_match = matches[0]
    value = first_match.group()
    span = first_match.span()
    return f"{sub_string[:span[0]]}{int(value) + number}{sub_string[span[1]:]}"


def explode(snailfish_number: str) -> tuple[str, bool]:
    for match in pair_pattern.finditer(snailfish_number):
        if get_pair_level(match.start(), snailfish_number) == 4:
            left, right = get_pair_numbers(match.group())
            span = match.span()
            left_of_pair = snailfish_number[: span[0]]
            right_of_pair = snailfish_number[span[1] :]
            left_sub_string = apply_explode_update_left(left, left_of_pair)
            right_sub_string = apply_explode_update_right(right, right_of_pair)
            new_number = f"{left_sub_string}0{right_sub_string}"
            return new_number, True

    return snailfish_number, False


def split_number(number: int) -> tuple[int, int]:
    half = number / 2
    return math.floor(half), math.ceil(half)


def split(snailfish_number: str) -> tuple[str, bool]:
    for match in single_number_pattern.finditer(snailfish_number):
        if (number := int(match.group())) > 9:
            left, right = split_number(number)
            span = match.span()
            left_of_pair = snailfish_number[: span[0]]
            right_of_pair = snailfish_number[span[1] :]
            return f"{left_of_pair}[{left},{right}]{right_of_pair}", True

    return snailfish_number, False


def addition(snailfish_number: str, to_add: str) -> str:
    return f"[{snailfish_number},{to_add}]"


def reduce_snailfish_number(snailfish_number: str) -> str:
    while True:
        snailfish_number, exploded = explode(snailfish_number)

        if exploded:
            continue

        snailfish_number, was_split = split(snailfish_number)

        if not exploded and not was_split:
            return snailfish_number


def parse_snailfish_number(snailfish_number: str, next_value: str) -> str:
    snailfish_number = addition(snailfish_number, next_value)
    return reduce_snailfish_number(snailfish_number)


def parse_snailfish_numbers(snailfish_numbers: list[str] | tuple[str, ...]) -> str:
    result = snailfish_numbers[0]

    for number in snailfish_numbers[1:]:
        result = parse_snailfish_number(result, number)

    return result


def calculate_magnitude(snailfish_number: str) -> int:
    pairs = list(pair_pattern.finditer(snailfish_number))

    if not pairs:
        return int(snailfish_number)

    for pair in pairs[::-1]:
        left, right = get_pair_numbers(pair.group())
        pair_value = left * 3 + right * 2
        span = pair.span()
        snailfish_number = (
            f"{snailfish_number[:span[0]]}{pair_value}{snailfish_number[span[1]:]}"
        )
        return calculate_magnitude(snailfish_number)

    raise ValueError(f"cannot parse snailfish number: {snailfish_number}")


def solve_homework(input_data: list[str]) -> int:
    result = parse_snailfish_numbers(input_data)
    return calculate_magnitude(result)


def solve_homework_part_two(input_data: list[str]) -> int:
    max_magnitude = 0

    for perm in permutations(input_data, 2):
        result = parse_snailfish_numbers(perm)
        magnitude = calculate_magnitude(result)
        max_magnitude = max(magnitude, max_magnitude)

    return max_magnitude


@register_solution(2021, 18, 1)
def part_one(input_data: list[str]):
    answer = solve_homework(input_data)

    if not answer:
        raise SolutionNotFoundError(2021, 18, 1)

    return answer


@register_solution(2021, 18, 2)
def part_two(input_data: list[str]):
    answer = solve_homework_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2021, 18, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 18)
    part_one(data)
    part_two(data)
