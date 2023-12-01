import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

REPLACEMENT_PATTERN = re.compile(r"(\w+) => (\w+)")


def get_replacements(input_data: list[str]) -> list[tuple[str, str]]:
    replacements: list[tuple[str, str]] = []

    # skip last two rows because it doesn't contain replacements
    for line in input_data[:-2]:
        found = REPLACEMENT_PATTERN.findall(line)
        if len(found) > 0:
            replacements.append(found[0])

    return replacements


def find_unique_replacements(replacements: list[tuple[str, str]], medicine: str) -> int:
    unique_replacements = set()

    for key, value in replacements:
        for i, _ in enumerate(medicine):
            if medicine[i : i + len(key)] == key:
                replacement = medicine[:i] + value + medicine[i + len(key) :]
                unique_replacements.add(replacement)

    return len(unique_replacements)


def count_time(replacements: list[tuple[str, str]], medicine: str) -> int:
    count = 0

    while medicine != "e":
        for key, value in replacements:
            if value in medicine:
                medicine = medicine.replace(value, key, 1)
                count += 1
    return count


@register_solution(2015, 19, 1)
def part_one(input_data: list[str]):
    replacements = get_replacements(input_data)
    answer = find_unique_replacements(replacements, input_data[-1])

    if not answer:
        raise SolutionNotFoundError(2015, 19, 1)

    return answer


@register_solution(2015, 19, 2)
def part_two(input_data: list[str]):
    answer = count_time(get_replacements(input_data), input_data[-1])

    if not answer:
        raise SolutionNotFoundError(2015, 19, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 19)
    part_one(data)
    part_two(data)
