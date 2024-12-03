import re
from collections.abc import Iterable

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def find_symbol_coords(lines: list[str]) -> set[tuple[int, int]]:
    """
    Loop through all lines to find the x,y coordinates of all symbols
    """
    coords = set[tuple[int, int]]()

    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            if not value.isdigit() and value != ".":
                coords.add((x, y))

    return coords


def find_gear_coords(lines: list[str]) -> dict[tuple[int, int], list[int]]:
    """
    Loop through all lines to find x,y coordinates of all gears (*)
    """
    coords: dict[tuple[int, int], list[int]] = {}

    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            if value == "*":
                coords[(x, y)] = []

    return coords


def neighbour_has_adjacent_symbol(
    current_position: tuple[int, int], symbols: set[tuple[int, int]]
) -> bool:
    x, y = current_position
    for y_mod in [-1, 0, 1]:
        for x_mod in [-1, 0, 1]:
            _x = x + x_mod
            _y = y + y_mod

            if (x + x_mod, y + y_mod) in symbols:
                return True

    return False


def neighbouring_gear_coords(
    current_position: tuple[int, int], gears: Iterable[tuple[int, int]]
) -> tuple[int, int] | None:
    x, y = current_position
    for y_mod in [-1, 0, 1]:
        for x_mod in [-1, 0, 1]:
            gear_pos = x + x_mod, y + y_mod

            if gear_pos in gears:
                return gear_pos

    return None


def find_numbers(lines: list[str]) -> int:
    symbols = find_symbol_coords(lines)
    pattern = re.compile("\\d+")
    total: int = 0

    for y, line in enumerate(lines):
        for match in pattern.finditer(line):
            for x in range(match.start(), match.end()):
                if neighbour_has_adjacent_symbol((x, y), symbols):
                    total += int(match.group())
                    break

    return total


def find_gear_ratios(lines: list[str]) -> int:
    gears = find_gear_coords(lines)
    pattern = re.compile("\\d+")
    total: int = 0

    for y, line in enumerate(lines):
        for match in pattern.finditer(line):
            for x in range(match.start(), match.end()):
                if (gear_pos := neighbouring_gear_coords((x, y), gears)) is not None:
                    if gear_pos not in gears:
                        gears[gear_pos] = []
                    gears[gear_pos].append(int(match.group()))

                    if len(gears[gear_pos]) == 2:
                        total += gears[gear_pos][0] * gears[gear_pos][1]
                    break

    return total


@register_solution(2023, 3, 1)
def part_one(input_data: list[str]):
    answer = find_numbers(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 3, 1)

    return answer


@register_solution(2023, 3, 2)
def part_two(input_data: list[str]):
    answer = find_gear_ratios(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 3, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 3)
    part_one(data)
    part_two(data)
