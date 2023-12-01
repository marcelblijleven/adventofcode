from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"
FORWARD = "F"
LEFT = "L"
RIGHT = "R"

Position = tuple[int, int]


def move(direction: str, steps: int, current_position: Position) -> Position:
    x, y = current_position

    if direction == "N":
        y += steps
    elif direction == "E":
        x += steps
    elif direction == "S":
        y -= steps
    elif direction == "W":
        x -= steps
    else:
        raise ValueError(f"unknown direction {direction}")

    return x, y


def turn(turn_direction: str, degrees: int, current_direction: str) -> str:
    compass = {NORTH: 0, EAST: 90, SOUTH: 180, WEST: 270}
    compass_invert = {0: NORTH, 90: EAST, 180: SOUTH, 270: WEST}
    current_degrees = compass[current_direction]

    if turn_direction == RIGHT:
        current_degrees += degrees
    elif turn_direction == LEFT:
        current_degrees -= degrees
    else:
        raise ValueError(f"unknown turn direction: {turn_direction}")

    current_degrees %= 360

    return compass_invert[current_degrees]


def _turn_waypoint_left(waypoint: tuple[int, int], degrees: int) -> tuple[int, int]:
    original_x, original_y = waypoint

    if degrees == 90:
        x = original_y * -1
        y = original_x
    elif degrees == 180:
        x = original_x * -1
        y = original_y * -1
    elif degrees == 270:
        x = original_y
        y = original_x * -1
    else:
        raise ValueError(f"cannot process degrees: {degrees}")

    return x, y


def _turn_waypoint_right(waypoint: tuple[int, int], degrees: int) -> tuple[int, int]:
    original_x, original_y = waypoint

    if degrees == 90:
        x = original_y
        y = original_x * -1
    elif degrees == 180:
        x = original_x * -1
        y = original_y * -1
    elif degrees == 270:
        x = original_y * -1
        y = original_x
    else:
        raise ValueError(f"cannot process degrees: {degrees}")

    return x, y


def turn_waypoint(
    waypoint: tuple[int, int], direction: str, degrees: int
) -> tuple[int, int]:
    if direction == LEFT:
        return _turn_waypoint_left(waypoint, degrees)
    elif direction == RIGHT:
        return _turn_waypoint_right(waypoint, degrees)
    else:
        raise ValueError(f"cannot process unknown direction: {direction}")


def move_waypoint(
    waypoint: tuple[int, int], action: str, number: int
) -> tuple[int, int]:
    x, y = waypoint

    if action == NORTH:
        y += number
    elif action == EAST:
        x += number
    elif action == SOUTH:
        y -= number
    elif action == WEST:
        x -= number
    else:
        raise ValueError(f"unknown action received: {action}")

    return x, y


def parse_instructions(instructions: list[str]) -> int:
    position = (0, 0)
    direction = EAST

    for instruction in instructions:
        action = instruction[0]
        number = int(instruction[1:])

        if action in [NORTH, EAST, SOUTH, WEST]:
            position = move(action, number, position)
        elif action in [LEFT, RIGHT]:
            direction = turn(action, number, direction)
        elif action == FORWARD:
            position = move(direction, number, position)
        else:
            raise ValueError(f"unknown action {action}")

    return abs(position[0]) + abs(position[1])


def parse_instructions_part_two(instructions: list[str]) -> int:
    position = (0, 0)
    waypoint = (10, 1)

    for instruction in instructions:
        action = instruction[0]
        number = int(instruction[1:])

        if action in [NORTH, EAST, SOUTH, WEST]:
            waypoint = move_waypoint(waypoint, action, number)
        elif action in [LEFT, RIGHT]:
            waypoint = turn_waypoint(waypoint, action, number)
        elif action == FORWARD:
            x, y = position
            x += number * waypoint[0]
            y += number * waypoint[1]
            position = (x, y)
        else:
            raise ValueError(f"unknown action {action}")

    return abs(position[0]) + abs(position[1])


@register_solution(2020, 12, 1)
def part_one(input_data: list[str]):
    answer = parse_instructions(input_data)

    if not answer:
        raise SolutionNotFoundError(2020, 12, 1)

    return answer


@register_solution(2020, 12, 2)
def part_two(input_data: list[str]):
    answer = parse_instructions_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2020, 12, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2020, 12)
    part_one(data)
    part_two(data)
