import string

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def split_rucksack(rucksack: str) -> tuple[str, str]:
    mid = int(len(rucksack) / 2)
    return rucksack[:mid], rucksack[mid:]


def compare_compartments(a: str, b: str) -> str | None:
    if not (found := (set(a) & set(b))):
        return None

    return found.pop()


def get_letter_value(letter: str) -> int:
    return string.ascii_letters.index(letter) + 1


def rucksacks_part_one(input_data: list[str]) -> int:
    score: int = 0

    for rucksack in input_data:
        if (
            matched_letter := compare_compartments(*split_rucksack(rucksack))
        ) is not None:
            score += get_letter_value(matched_letter)

    return score


def get_groups_of_three(input_data: list[str]):
    for idx in range(0, len(input_data), 3):
        yield input_data[idx : idx + 3]


def compare_rucksacks(a: str, b: str, c: str) -> str | None:
    if not (found := (set(a) & set(b) & set(c))):
        return None

    return found.pop()


def rucksacks_part_two(input_data: list[str]) -> int:
    score: int = 0

    for group in get_groups_of_three(input_data):
        if matched_letter := compare_rucksacks(*group):
            score += get_letter_value(matched_letter)

    return score


@register_solution(2022, 3, 1)
def part_one(input_data: list[str]):
    answer = rucksacks_part_one(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 3, 1)

    return answer


@register_solution(2022, 3, 2)
def part_two(input_data: list[str]):
    answer = rucksacks_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 3, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 3)
    part_one(data)
    part_two(data)
