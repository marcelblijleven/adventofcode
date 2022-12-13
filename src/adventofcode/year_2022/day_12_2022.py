from typing import Optional

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]
Grid = dict[Position, str]
Graph = dict[Position, set[Position]]


def parse_grid(input_data: list[str]) -> tuple[Grid, Position, Position]:
    grid: Grid = {}
    start: Optional[Position] = None
    end: Optional[Position] = None

    for y, row in enumerate(input_data):
        for x, letter in enumerate(row):
            grid[x, y] = letter
            if letter == "S":
                start = x, y
            elif letter == "E":
                end = x, y

    return grid, start, end


def get_directions_for_position(position: Position, grid: Grid) -> set[Position]:
    """Get all possible directions from the current position"""
    x, y = position

    directions: set[Position] = set()

    for diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        d_x, d_y = diff
        direction = x + d_x, y + d_y

        if direction in grid:
            directions.add(direction)

    return directions


def can_climb(current: str, next_position: str, must_go_up: bool = False) -> bool:
    """
    Check if you can climb to the next position

    Regular rules, can climb if:
    - current position is S or next position is E
    - current height is less than or equal to next height
    - current height is 1 lower than next height

    Must go up rules: only difference is that if current position is 'a'
    and the next position is also 'a', return False. This forces the elves up
    and helps eliminate starting positions
    """
    if must_go_up and current == "a" and next_position == "a":
        return False

    if current == "S":
        return True

    if next_position == "E":
        return current == "z"

    current_height = ord(current)
    next_height = ord(next_position)

    if current_height >= next_height or next_height == current_height + 1:
        return True

    return False


def get_possible_routes_for_position(
    position: Position, grid: Grid, must_go_up: bool = False
) -> list[Position]:
    """
    Get all possible routes (directions) from the current position
    """
    directions = get_directions_for_position(position, grid)
    routes: list[Position] = []

    for direction in directions:
        if can_climb(grid[position], grid[direction], must_go_up):
            routes.append(direction)

    return routes


def grid_to_graph(grid: Grid) -> dict[Position, set[Position]]:
    """Transform the x, y grid to a graph"""
    graph: Graph = {}

    max_x, max_y = max(grid)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            graph[x, y] = set(get_possible_routes_for_position((x, y), grid))

    return graph


def find_fastest_route(input_data: list) -> list[tuple[int, int]]:
    """Find the fastest route to 'E' from 'S'"""
    grid, start, end = parse_grid(input_data)
    graph: dict[Position, set[Position]] = grid_to_graph(grid)

    paths = [[start]]
    path_idx = 0
    visited = {start}

    while path_idx < len(paths):
        current = paths[path_idx]
        last_position = current[-1]
        next_positions = graph[last_position]

        if end in next_positions:
            current.append(end)
            return current

        for next_position in next_positions:
            if next_position not in visited:
                paths.append(current[:] + [next_position])
                visited.add(next_position)

        path_idx += 1

    return []


def find_scenic_route(input_data: list) -> list[tuple[int, int]]:
    """
    Find the shortest scenic route from 'a' to 'E'

    Finds any 'a' position with possible routes to start from
    This probably can go faster, maybe reverse search from End to any 'a'
    """
    grid, _, end = parse_grid(input_data)
    graph: dict[Position, set[Position]] = grid_to_graph(grid)

    positions = {k: v for k, v in graph.items() if grid[k] == "a" and len(v) > 0}
    possible_hikes = []

    for position in positions:
        paths = [[position]]
        path_idx = 0
        visited = {position}

        while path_idx < len(paths):
            current = paths[path_idx]
            last_position = current[-1]
            next_positions = graph[last_position]

            if end in next_positions:
                current.append(end)
                possible_hikes.append(current)
                break

            for next_position in next_positions:
                if next_position not in visited:
                    paths.append(current[:] + [next_position])
                    visited.add(next_position)

            path_idx += 1

    return min(possible_hikes, key=lambda hike: len(hike))


@register_solution(2022, 12, 1)
def part_one(input_data: list[str]):
    answer = len(find_fastest_route(input_data)) - 1

    if not answer:
        raise SolutionNotFoundException(2022, 12, 1)

    return answer


@register_solution(2022, 12, 2)
def part_two(input_data: list[str]):
    answer = len(find_scenic_route(input_data)) - 1

    if not answer:
        raise SolutionNotFoundException(2022, 12, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 12)
    part_one(data)
    part_two(data)
