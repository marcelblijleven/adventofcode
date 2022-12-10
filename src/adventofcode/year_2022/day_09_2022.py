import copy
from collections import defaultdict
from typing import Generator

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import manhattan_distance
from adventofcode.util.input_helpers import get_input_for_day


def parse_instruction(line: str) -> tuple[str, int]:
    """Parses an instruction to direction and number of steps"""
    direction, _, steps = line.partition(" ")
    return direction, int(steps)


def get_instructions(input_data: list[str]) -> Generator[tuple[str, int], None, None]:
    """Get instructions from input data"""
    for line in input_data:
        yield parse_instruction(line)


def _move_in_direction(
    position: tuple[int, int], direction: str, steps: int
) -> tuple[int, int]:
    if not steps:
        return position

    x, y = position
    if direction == "U":
        y -= steps
    elif direction == "R":
        x += steps
    elif direction == "D":
        y += steps
    elif direction == "L":
        x -= steps
    else:
        raise ValueError(f'unknown direction "{direction}" received')
    return x, y


def move(
    instruction: tuple[str, int],
    position_head: tuple[int, int],
    position_tail: tuple[int, int],
    tail_locations: dict[tuple[int, int], int],
) -> tuple[int, int, int, int]:
    """Apply the move instruction and update the head and tail positions"""
    direction, steps = instruction
    head_x, head_y = position_head
    tail_x, tail_y = position_tail
    new_head_x, new_head_y = head_x, head_y

    for _ in range(steps):
        new_head_x, new_head_y = _move_in_direction((head_x, head_y), direction, 1)

        # Diagonally is two steps, but shouldn't invoke a move from tail
        allowed_distance = 1 if new_head_x == tail_x or new_head_y == tail_y else 2

        if (
            manhattan_distance((new_head_x, new_head_y), (tail_x, tail_y))
            > allowed_distance
        ):
            tail_x, tail_y = determine_move((tail_x, tail_y), (new_head_x, new_head_y))
            tail_locations[tail_x, tail_y] += 1

        head_x, head_y = (new_head_x, new_head_y)

    return new_head_x, new_head_y, tail_x, tail_y


def determine_move(
    position: tuple[int, int], target: tuple[int, int]
) -> tuple[int, int]:
    """
    Determine the next position based on the target

    If x or y is the same, move along they or x respectively.
    Else, move diagonally
    """
    pos_x, pos_y = position
    target_x, target_y = target

    if pos_x == target_x:
        # move vertically
        pos_y += target_y - pos_y - (1 if target_y > pos_y else -1)
    elif pos_y == target_y:
        # move horizontally
        pos_x += target_x - pos_x - (1 if target_x > pos_x else -1)
    else:
        # move diagonally
        pos_y += 1 if target_y > pos_y else -1
        pos_x += 1 if target_x > pos_x else -1

    return pos_x, pos_y


def move_snake(
    instruction: tuple[str, int],
    positions: dict[int, tuple[int, int]],
    tail_locations: dict[tuple[int, int], int],
) -> None:
    """
    Apply the move instruction and update the head, knot and tail positions
    """
    direction, steps = instruction

    for _ in range(steps):
        for key, position in positions.items():
            if key == 0:  # Head
                positions[key] = _move_in_direction(position, direction, 1)
            else:
                x, y = position
                x_prev, y_prev = positions[key - 1]
                allowed_distance = 1 if x_prev == x or y_prev == y else 2

                if manhattan_distance(position, positions[key - 1]) > allowed_distance:
                    positions[key] = determine_move(position, positions[key - 1])

                    if key == 9:  # Tail
                        tail_locations[positions[key]] += 1


def simulate_rope(input_data: list[str]) -> int:
    """
    Simulate rope movements and return the number of positions
    the tail has visited at least once
    """
    tail_locations: defaultdict[tuple[int, int], int] = defaultdict(int)
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0

    tail_locations[tail_x, tail_y] += 1

    for instruction in get_instructions(input_data):
        head_x, head_y, tail_x, tail_y = move(
            instruction, (head_x, head_y), (tail_x, tail_y), tail_locations
        )

    return len(tail_locations.keys())


def simulate_rope_snake(input_data: list[str]) -> int:
    """
    Simulate rope movements and return the number of positions
    the tail has visited at least once
    """
    tail_locations: defaultdict[tuple[int, int], int] = defaultdict(int)
    tail_locations[0, 0] += 1
    positions = {k: (0, 0) for k in range(0, 10)}

    for instruction in get_instructions(input_data):
        move_snake(instruction, positions, tail_locations)

    return len(tail_locations.keys())


@register_solution(2022, 9, 1)
def part_one(input_data: list[str]):
    answer = simulate_rope(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 9, 1)

    return answer


@register_solution(2022, 9, 2)
def part_two(input_data: list[str]):
    answer = simulate_rope_snake(input_data)

    if not answer:
        raise SolutionNotFoundException(2022, 9, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 9)
    part_one(data)
    part_two(data)
