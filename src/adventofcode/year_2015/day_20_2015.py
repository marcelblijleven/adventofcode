from collections import defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def most_presents_at_house(houses: dict[int, int]) -> int:
    presents = sorted(houses.values())

    if len(presents) == 0:
        return 0

    return presents[-1]


def visit_houses(elf_count: int, target: int):
    houses: dict[int, int] = defaultdict(int)

    for elf in range(1, target):
        for house in range(elf, elf_count, elf):
            houses[house] += elf * 10

        if houses[elf] >= target:
            return elf


def visit_houses_part_two(elf_count: int, target: int):
    houses: dict[int, int] = defaultdict(int)

    for elf in range(1, target):
        for house in range(elf, min([elf * 50 + 1, elf_count]), elf):
            houses[house] += elf * 11

        if houses[elf] >= target:
            return elf


@register_solution(2015, 20, 1)
def part_one(input_data: list[str]):
    target = int(input_data[0])
    answer = visit_houses(1000000, target)

    if not answer:
        raise SolutionNotFoundError(2015, 20, 1)

    return answer


@register_solution(2015, 20, 2)
def part_two(input_data: list[str]):
    target = int(input_data[0])
    answer = visit_houses_part_two(1000000, target)

    if not answer:
        raise SolutionNotFoundError(2015, 20, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 20)
    part_one(data)
    part_two(data)
