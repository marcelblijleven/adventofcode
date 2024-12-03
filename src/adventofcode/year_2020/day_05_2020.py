import statistics

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def get_midpoint(min_row: int, max_row: int) -> int:
    return round(statistics.median(range(min_row, max_row + 1)))


def parse(sequence: list[str], min_row: int, max_row: int) -> int:
    next_step = sequence.pop(0)

    if next_step in ["F", "L"]:
        # Take lower half, subtract 1 because you take the lower part until the midpoint
        max_row = get_midpoint(min_row, max_row) - 1
        if not sequence:
            return min_row

    elif next_step in ["B", "R"]:
        # Take upper half
        min_row = get_midpoint(min_row, max_row)
        if not sequence:
            return max_row

    return parse(sequence, min_row, max_row)


@register_solution(2020, 5, 1)
def part_one(input_data: list[str]):
    ids = []

    for boarding_pass in input_data:
        row = parse([char for char in boarding_pass if char in ["F", "B"]], 0, 127)
        column = parse([char for char in boarding_pass if char in ["L", "R"]], 0, 7)
        ids.append(row * 8 + column)

    if not ids:
        raise SolutionNotFoundError(2020, 5, 1)

    return max(ids)


def _part_one_binary_version(input_data: list[str]) -> list[int]:
    ids = []

    for boarding_pass in input_data:
        # could also use a translation table
        # boarding_pass.translate(str.maketrans({'B': '1', 'F': '0', 'R': '1', 'L': '0'})
        _boarding_pass = (
            boarding_pass.replace("B", "1")
            .replace("F", "0")
            .replace("R", "1")
            .replace("L", "0")
        )
        ids.append(int(_boarding_pass, 2))

    if not ids:
        raise SolutionNotFoundError(2020, 5, 2)

    return ids


@register_solution(2020, 5, 2, "binary version")
def part_one_binary_version(input_data):
    return max(_part_one_binary_version(input_data))


@register_solution(2020, 5, 2)
def part_two(input_data: list[str]):
    ids = _part_one_binary_version(input_data)

    for i in range(0, max(ids)):
        if i not in ids and i - 1 in ids and i + 1 in ids:
            return i


if __name__ == "__main__":
    data = get_input_for_day(2020, 5)
    part_one(data)
    part_one_binary_version(data)
    part_two(data)
