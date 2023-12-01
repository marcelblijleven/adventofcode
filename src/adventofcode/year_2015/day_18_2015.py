import math

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

LightType = tuple[int, int]
GridType = dict[LightType, str]
ON = "#"
OFF = "."


def read_grid(input_data: list[str]) -> GridType:
    grid: GridType = {}

    for y, line in enumerate(input_data):
        for x, light in enumerate(line):
            grid[(x, y)] = light

    return grid


def get_neighbours(light: LightType):
    """
    Gets all the neighbours
    123
    4#5
    678
    """
    x, y = light
    neighbours: list[LightType] = []

    for y_diff in range(-1, 2):
        for x_diff in range(-1, 2):
            neighbour = (x + x_diff, y + y_diff)
            if neighbour != light:
                neighbours.append(neighbour)

    return neighbours


def get_next_state(light: LightType, grid: GridType) -> str:
    own_state = grid[light]
    neighbours = get_neighbours(light)
    neighbour_states: list[str] = []

    for neighbour in neighbours:
        if neighbour not in grid.keys():
            neighbour_states.append(OFF)
        else:
            neighbour_states.append(grid[neighbour])

    neighbours_on = neighbour_states.count(ON)
    # neighbours_off = neighbour_states.count(OFF)

    if own_state == ON:
        if neighbours_on in (2, 3):
            return ON

        return OFF
    elif own_state == OFF:
        if neighbours_on == 3:
            return ON

        return OFF
    else:
        raise ValueError(f"unknown light state: {own_state}")


def animate(grid: GridType) -> GridType:
    new_grid = grid.copy()

    for light in grid.keys():
        new_grid[light] = get_next_state(light, grid)

    return new_grid


def animate_stuck_corners(grid: GridType) -> GridType:
    new_grid = grid.copy()
    corners = get_corners(grid)

    for light in grid.keys():
        if light in corners:
            new_grid[light] = ON
        else:
            new_grid[light] = get_next_state(light, grid)

    return new_grid


def get_corners(grid: GridType) -> list[LightType]:
    max_x = max([keys[0] for keys in grid.keys()])
    max_y = max([keys[1] for keys in grid.keys()])
    return [(0, 0), (0, max_y), (max_x, max_y), (max_x, 0)]


def grid_to_list_str(grid: GridType) -> list[str]:
    # will only work on square grids
    size = int(math.sqrt(len(grid.keys())))
    lines = []

    for y in range(size):
        line = ""
        for x in range(size):
            line += grid[(x, y)]

        lines.append(line)

    return lines


@register_solution(2015, 18, 1)
def part_one(input_data: list[str]):
    grid = read_grid(input_data)

    for _ in range(100):
        grid = animate(grid)

    answer = "".join(grid_to_list_str(grid)).count(ON)

    if not answer:
        raise SolutionNotFoundError(2015, 18, 1)

    return answer


@register_solution(2015, 18, 2)
def part_two(input_data: list[str]):
    grid = read_grid(input_data)

    for corner in get_corners(grid):
        grid[corner] = ON

    for _ in range(100):
        grid = animate_stuck_corners(grid)

    answer = "".join(grid_to_list_str(grid)).count(ON)

    if not answer:
        raise SolutionNotFoundError(2015, 18, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 18)
    part_one(data)
    part_two(data)
