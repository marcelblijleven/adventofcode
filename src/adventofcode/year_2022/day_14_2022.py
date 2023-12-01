from collections import defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]
Cave = dict[Position, str]


class AbyssError(Exception):
    """Raised when a unit of sand falls into the abyss"""


class SandStoppedError(Exception):
    """Raised when the pouring of sand has stopped"""


def read_paths(line: str) -> list[Position]:
    """Convert an input line to a list of Position"""
    segments = line.split(" -> ")
    paths: list[Position] = []

    for segment in segments:
        x, y = segment.split(",")
        paths.append((int(x), int(y)))

    return paths


def fill_paths_in_cave(paths: list[Position], cave: Cave) -> None:
    """Draw rock paths in cave"""
    index = 0

    while index < len(paths) - 1:
        start_x, start_y = paths[index]
        end_x, end_y = paths[index + 1]

        if end_x < start_x:
            start_x, end_x = end_x, start_x
        if end_y < start_y:
            start_y, end_y = end_y, start_y

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                cave[x, y] = "#"

        index += 1


def scan_cave(input_data: list[str]) -> Cave:
    """Scan rocks in cave"""
    cave: Cave = defaultdict(str)

    for line in input_data:
        fill_paths_in_cave(read_paths(line), cave)

    return cave


def get_abyss(cave: Cave) -> int:
    """Get the y coordinate of the lowest (the highest value) rock formation"""
    return max([y for x, y in cave.keys()])


def get_floor(cave: Cave) -> int:
    """Get the y coordiante of the floor (the highest y value + 2)"""
    return max([y for x, y in cave.keys()]) + 2


def simulate_sand(cave: Cave) -> int:
    """
    Simulate dropping of sand in cave

    Sand always falls from 500, 0 and falls down first
    If it cannot fall down, it falls diagonally to the left
    If it cannot fall left, it falls diagonally to the right
    If it cannot fall vertical or diagonal, it stops

    If the unit of sand falls into the abyss, a AbyssException is raised
    """
    pouring_start = 500, 0
    units_of_sand = 0
    abyss = get_abyss(cave)

    try:
        while True:  # pour new unit of sand
            units_of_sand += 1
            position = pouring_start

            while True:  # falling of unit of sand
                x, y = position

                if y > abyss:
                    raise AbyssError()

                # Try vertical drop
                if (next_position := (x, y + 1)) not in cave:
                    position = next_position
                    continue
                # Try diagonally left
                elif (next_position := (x - 1, y + 1)) not in cave:
                    position = next_position
                    continue
                # Try diagonally right
                elif (next_position := (x + 1, y + 1)) not in cave:
                    position = next_position
                    continue
                else:
                    # Sand cannot drop any further and rests here
                    cave[position] = "o"
                    break
    except AbyssError:
        # Return units of sand minus one because we need the unit BEFORE they start
        # to fall into the abyss
        return units_of_sand - 1


def simulate_sand_with_floor(cave: Cave) -> int:
    """
    Simulate dropping of sand in cave

    Sand always falls from 500, 0 and falls down first
    If it cannot fall down, it falls diagonally to the left
    If it cannot fall left, it falls diagonally to the right
    If it cannot fall vertical or diagonal, it stops

    If the unit of sand falls into the abyss, a AbyssException is raised
    """
    pouring_start = 500, 0
    units_of_sand = 0
    cave_floor = get_floor(cave)

    try:
        while True:  # pour new unit of sand
            if pouring_start in cave:
                raise SandStoppedError()

            units_of_sand += 1
            position = pouring_start

            while True:  # falling of unit of sand
                x, y = position

                next_y = y + 1

                if next_y == cave_floor:
                    cave[position] = "o"
                    break

                # Try vertical drop
                if (next_position := (x, next_y)) not in cave:
                    position = next_position
                    continue
                # Try diagonally left
                elif (next_position := (x - 1, next_y)) not in cave:
                    position = next_position
                    continue
                # Try diagonally right
                elif (next_position := (x + 1, next_y)) not in cave:
                    position = next_position
                    continue
                else:
                    # Sand cannot drop any further and rests here
                    cave[position] = "o"
                    break

    except SandStoppedError:
        return units_of_sand


def count_units_of_sand(input_data: list[str]) -> int:
    """Count units of sand before sand starts falling into the abyss"""
    cave = scan_cave(input_data)
    return simulate_sand(cave)


def count_units_of_sand_until_stopped(input_data: list[str]) -> int:
    """Count units of sand until the pouring stops"""
    cave = scan_cave(input_data)
    return simulate_sand_with_floor(cave)


@register_solution(2022, 14, 1)
def part_one(input_data: list[str]):
    answer = count_units_of_sand(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 14, 1)

    return answer


@register_solution(2022, 14, 2)
def part_two(input_data: list[str]):
    answer = count_units_of_sand_until_stopped(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 14, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 14)
    part_one(data)
    part_two(data)
