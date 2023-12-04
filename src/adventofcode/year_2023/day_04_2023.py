import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def parse_card(line: str) -> int:
    pattern = re.compile("\\d{1,2}")
    _, numbers = line.split(": ")
    split_card = numbers.split(" | ")
    winning_numbers = set(map(int, pattern.findall(split_card[0])))
    my_numbers = set(map(int, pattern.findall(split_card[1])))
    my_winning_numbers = winning_numbers & my_numbers

    if not my_winning_numbers:
        return 0

    return 1 * 2 ** (len(my_winning_numbers) - 1)


@register_solution(2023, 4, 1)
def part_one(input_data: list[str]):
    answer = sum(map(parse_card, input_data))

    if not answer:
        raise SolutionNotFoundError(2023, 4, 1)

    return answer


@register_solution(2023, 4, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2023, 4, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 4)
    part_one(data)
    part_two(data)
