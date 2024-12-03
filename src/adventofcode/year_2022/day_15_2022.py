import re
from functools import partial
from multiprocessing import Pool

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.helpers import manhattan_distance
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]
Grid = dict[Position, str]


def parse_input(input_data: list[str]) -> list[tuple[Position, Position]]:
    pattern = re.compile(r"(-?\d+)")
    pairs: list[tuple[Position, Position]] = []

    for line in input_data:
        s_x, s_y, b_x, b_y = pattern.findall(line)
        sensor = int(s_x), int(s_y)
        beacon = int(b_x), int(b_y)
        pairs.append((sensor, beacon))

    return pairs


def find_locations_at_y(input_data: list[str], y_value: int) -> int:
    """
    Find any sensor where the range of y - manhattan distance and y + manhattan distance
    intersects with the y value that is to be checked

    Then use the difference between the manhattan distance between the sensor and beacon
    and the sensor y value and the y value that needs to be checked to determine
    how far the x value can go left and right of the sensor's x value
    """
    grid: Grid = {}
    pairs = parse_input(input_data)

    for sensor, beacon in pairs:
        grid[sensor] = "S"
        grid[beacon] = "B"
        distance = manhattan_distance(sensor, beacon)
        sensor_x, sensor_y = sensor

        if y_value in range(sensor_y - distance, sensor_y + distance + 1):
            distance_y = abs(sensor_y - y_value)
            distance_remainder = distance - distance_y

            for x in range(
                sensor_x - distance_remainder, sensor_x + distance_remainder + 1
            ):
                if (position := (x, y_value)) not in grid:
                    grid[position] = "#"

    return sum([1 for key, value in grid.items() if key[1] == y_value and value == "#"])


def rotate_positions(position: Position) -> Position:
    """Rotate the position to be able to make squares out of the diamond ranges"""
    x, y = position
    return x + y, x - y


def undo_rotate_positions(position: Position) -> Position:
    """Reset position to original state"""
    u, v = position
    return (u + v) // 2, (u - v) // 2


def find_positions_at_y(
    pairs: list[tuple[Position, Position]], y_value: int
) -> Position | None:
    ranges: list[Position] = []

    for sensor, beacon in pairs:
        sensor_x, sensor_y = sensor
        distance = manhattan_distance(sensor, beacon)
        y_distance = abs(y_value - sensor_y)

        if y_distance > distance:
            continue

        x_distance = distance - y_distance
        ranges.append((sensor_x - x_distance, sensor_x + x_distance))

    ranges.sort()
    last_x2 = ranges[0][1]
    for x1, x2 in ranges[1:]:
        if x1 > last_x2:
            return last_x2 + 1, y_value
        last_x2 = max(x2, last_x2)

    return None


def find_beacon_position(input_data: list[str], range_value: int = 4000000) -> int:
    pairs = parse_input(input_data)

    with Pool() as p:
        results = p.map(partial(find_positions_at_y, pairs), range(range_value))
        x, y = next(filter(bool, results))  # type: ignore
        return x * range_value + y


@register_solution(2022, 15, 1)
def part_one(input_data: list[str]):
    answer = find_locations_at_y(input_data, 2000000)

    if not answer:
        raise SolutionNotFoundError(2022, 15, 1)

    return answer


@register_solution(2022, 15, 2)
def part_two(input_data: list[str]):
    answer = find_beacon_position(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 15, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 15)
    part_one(data)
    part_two(data)
