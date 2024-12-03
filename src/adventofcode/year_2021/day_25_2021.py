import copy

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

EASTBOUND = ">"
SOUTHBOUND = "v"
EMPTY = "."

Position = tuple[int, int]
Grid = dict[Position, str]


def get_values(input_data: list[str]) -> Grid:
    grid: Grid = {}
    for y, line in enumerate(input_data):
        for x, value in enumerate(line):
            grid[x, y] = value

    return grid


def get_next_position(
    position: Position, direction: str, grid: Grid, max_x: int, max_y: int
) -> bool | Position:
    x, y = position

    if direction == EASTBOUND:
        x += 1

        if x > max_x:
            x = 0
    elif direction == SOUTHBOUND:
        y += 1

        if y > max_y:
            y = 0

    if grid[x, y] != EMPTY:
        return False

    return x, y


def get_next_southbound_position(
    position: Position,
    seen: set[Position],
    old_eastbound_positions: set[Position],
    grid: Grid,
    max_y: int,
) -> bool | Position:
    x, y = position
    y += 1

    if y > max_y:
        y = 0

    if grid[x, y] == EMPTY:
        return x, y
    elif grid[x, y] == SOUTHBOUND:
        return False
    else:
        if (x, y) in seen:
            return False

        if grid[x + 1 % 100, y] == EMPTY:
            grid[x + 1 % 100, y] = EASTBOUND
            old_eastbound_positions.add((x, y))
            return x, y

    return False


def do_step(grid: Grid, max_x: int, max_y: int) -> bool:
    has_moved = False
    new_grid = copy.deepcopy(grid)

    for position, value in grid.items():
        if value != EASTBOUND:
            continue

        if next_position := get_next_position(position, value, grid, max_x, max_y):
            new_grid[next_position] = value  # type: ignore
            new_grid[position] = EMPTY
            has_moved = True

    grid.update(new_grid)

    for position, value in grid.items():
        if value != SOUTHBOUND:
            continue

        if next_position := get_next_position(position, value, grid, max_x, max_y):
            new_grid[next_position] = value  # type: ignore
            new_grid[position] = EMPTY
            has_moved = True

    grid.update(new_grid)

    return has_moved


def do_steps(input_data: list[str]) -> int:
    grid = get_values(input_data)
    max_x = max(pos[0] for pos in grid.keys())
    max_y = max(pos[1] for pos in grid.keys())
    counter = 0

    while True:
        counter += 1
        has_moved = do_step(grid, max_x, max_y)
        if not has_moved:
            break

    return counter


@register_solution(2021, 25, 1)
def part_one(input_data: list[str]):
    answer = do_steps(input_data)

    if not answer:
        raise SolutionNotFoundError(2021, 25, 1)

    return answer


# @register_solution(2021, 5, 2)
# def part_two(input_data: list[str]):
#     answer = ...
#
#     if not answer:
#         raise SolutionNotFoundError(2021, 25, 2)
#
#     return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 25)
    part_one(data)
    # part_two(data)
