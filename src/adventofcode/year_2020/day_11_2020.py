from operator import itemgetter

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

FREE_SEAT = "L"
FLOOR = "."
TAKEN_SEAT = "#"

LayoutType = dict[tuple[int, int], str]


def get_layout(lines):
    y = 0
    layout = {}

    for line in lines:
        x = 0
        for item in line:
            layout[x, y] = item
            x += 1
        y += 1

    return layout


def get_x_y_range(layout: LayoutType) -> tuple[int, int]:
    max_x = max(layout.keys(), key=itemgetter(0))[0]
    max_y = max(layout.keys(), key=itemgetter(1))[1]
    return max_x, max_y


def get_adjacent_coordinates(
    layout: LayoutType, current_x: int, current_y: int
) -> LayoutType:
    adjacent_coordinates = {}

    for x, y in [
        (current_x + i, current_y + j) for i in [-1, 0, 1] for j in [-1, 0, 1]
    ]:
        if (x, y) in layout:
            adjacent_coordinates[x, y] = layout[x, y]

    return adjacent_coordinates


def seating_iteration(layout: LayoutType):
    new_layout = layout.copy()
    max_x, max_y = get_x_y_range(layout)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if layout[x, y] == FLOOR:
                continue

            adjacent_coordinates = get_adjacent_coordinates(layout, x, y)

            if layout[x, y] == FREE_SEAT:
                if [v for k, v in adjacent_coordinates.items() if k != (x, y)].count(
                    TAKEN_SEAT
                ) == 0:
                    new_layout[x, y] = TAKEN_SEAT
            elif layout[x, y] == TAKEN_SEAT:
                if [v for k, v in adjacent_coordinates.items() if k != (x, y)].count(
                    TAKEN_SEAT
                ) >= 4:
                    new_layout[x, y] = FREE_SEAT

    return new_layout


def print_layout(layout: LayoutType):
    max_x, max_y = get_x_y_range(layout)
    lines = []

    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            line += layout[x, y]

        lines.append(line)

    print("\n".join(lines), "\n")  # noqa


def start_iterating(layout: LayoutType, iteration_func=seating_iteration):  # type: ignore
    previous_layout = layout
    iteration = 1

    while True:
        new_layout = iteration_func(previous_layout)
        if new_layout == previous_layout:
            return len([value for value in new_layout.values() if value == TAKEN_SEAT])

        previous_layout = new_layout
        iteration += 1


@register_solution(2020, 11, 1)
def part_one(_input):
    layout = get_layout(_input)
    taken_seats = start_iterating(layout)
    return taken_seats


def seats_in_line_of_sight(
    layout: LayoutType, current_x: int, current_y: int
) -> LayoutType:
    directions = {
        "left": (-1, 0),
        "right": (1, 0),
        "up": (0, -1),
        "down": (0, 1),
        "left_up": (-1, -1),
        "right_up": (1, -1),
        "left_down": (-1, 1),
        "right_down": (1, 1),
    }

    coords = {}

    for direction in directions.values():
        x = current_x
        y = current_y

        while True:
            x = x + direction[0]
            y = y + direction[1]

            if (x, y) not in layout.keys():
                break

            if layout[x, y] != FLOOR:
                coords[x, y] = layout[x, y]
                break

    return coords


def los_seating_iteration(layout: LayoutType, tolerance=5) -> LayoutType:
    new_layout = layout.copy()
    max_x, max_y = get_x_y_range(layout)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if layout[x, y] == FLOOR:
                continue

            seats = seats_in_line_of_sight(layout, x, y)

            if layout[x, y] == FREE_SEAT:
                if [v for k, v in seats.items() if k != (x, y)].count(TAKEN_SEAT) == 0:
                    new_layout[x, y] = TAKEN_SEAT
            elif layout[x, y] == TAKEN_SEAT:
                if [v for k, v in seats.items() if k != (x, y)].count(
                    TAKEN_SEAT
                ) >= tolerance:
                    new_layout[x, y] = FREE_SEAT

    return new_layout


@register_solution(2020, 11, 2)
def part_two(_input):
    layout = get_layout(_input)
    taken_seats = start_iterating(layout, los_seating_iteration)
    return taken_seats


if __name__ == "__main__":
    data = get_input_for_day(2020, 11)
    part_one(data)
    part_two(data)
