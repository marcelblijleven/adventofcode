import heapq

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.helpers import manhattan_distance
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]
Grid = dict[Position, int]


def parse_input(input_list: list[str]) -> Grid:
    grid: Grid = {}

    for y, line in enumerate(input_list):
        for x, value in enumerate(line):
            grid[(x, y)] = int(value)

    return grid


def get_possible_routes_for_position(position: Position, grid: Grid) -> list[Position]:
    x, y = position
    possible_routes: list[Position] = []
    routes = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for route in routes:
        possible_route = x + route[0], y + route[1]

        if possible_route in grid:
            possible_routes.append(possible_route)

    return possible_routes


def find_route(grid: Grid):
    start = (0, 0)
    end = max(grid.keys())
    heap: list[tuple[int, Position]] = []
    heapq.heappush(heap, (0, start))
    visited: dict[Position, int] = {start: 0}

    while len(heap) > 0:
        # https://docs.python.org/3/library/heapq.html#module-heapq
        # retrieve the smallest item from the heap
        # use [0] to retrieve it without popping
        #
        # Could also use PriorityQueue, which is thread safe and heapq is not,
        # but for this solution it doesn't matter
        position = heapq.heappop(heap)[1]

        if position == end:
            break

        for route in get_possible_routes_for_position(position, grid):
            risk = visited[position] + grid[route]

            if route not in visited or risk < visited[route]:
                visited[route] = risk
                cost = manhattan_distance(route, end) + risk
                heapq.heappush(heap, (cost, route))

    return visited[end]


def increment_value(value: int) -> int:
    new_value = value + 1

    if new_value > 9:
        new_value = new_value % 9

    return new_value


def enlarge_grid(grid: Grid, factor: int = 5) -> Grid:
    max_x, max_y = max(grid.keys())
    new_grid: Grid = {}

    # Horizontal first
    for y in range(max_y + 1):
        for x in range((max_x + 1) * factor):
            position = x, y
            if position in grid:
                new_grid[position] = grid[position]
            else:
                target_x = x - (max_x + 1)
                new_grid[position] = increment_value(new_grid[(target_x, y)])

    # Calculate vertical last
    for y in range(max_y + 1, (max_y + 1) * factor):
        for x in range((max_x + 1) * factor):
            position = x, y
            target_y = y - (max_y + 1)
            new_grid[position] = increment_value(new_grid[(x, target_y)])

    return new_grid


@register_solution(2021, 15, 1)
def part_one(input_data: list[str]):
    answer = find_route(parse_input(input_data))

    if not answer:
        raise SolutionNotFoundError(2021, 15, 1)

    return answer


@register_solution(2021, 15, 2)
def part_two(input_data: list[str]):
    grid = parse_input(input_data)
    answer = find_route(enlarge_grid(grid))

    if not answer:
        raise SolutionNotFoundError(2021, 15, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 15)
    part_one(data)
    part_two(data)
