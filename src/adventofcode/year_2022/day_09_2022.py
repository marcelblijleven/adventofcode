from collections import defaultdict
from collections.abc import Generator

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
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
        err = f'unknown direction "{direction}" received'
        raise ValueError(err)
    return x, y


def get_allowed_distance(pos_a: tuple[int, int], pos_b: tuple[int, int]) -> int:
    """Diagonally is two steps, but shouldn't invoke a move from tail"""
    return 1 if pos_a[0] == pos_b[0] or pos_a[1] == pos_b[1] else 2


def move(
    instruction: tuple[str, int],
    position_head: tuple[int, int],
    position_tail: tuple[int, int],
    tail_locations: dict[tuple[int, int], int],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Apply the move instruction and update the head and tail positions"""
    direction, steps = instruction

    for _ in range(steps):
        position_head = _move_in_direction(position_head, direction, 1)

        if manhattan_distance(position_head, position_tail) > get_allowed_distance(
            position_head, position_tail
        ):
            position_tail = determine_move(position_tail, position_head)
            tail_locations[position_tail] += 1

    return position_head, position_tail


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
    head_pos = 0
    tail_pos = 9
    for _ in range(steps):
        for key, position in positions.items():
            if key == head_pos:  # Head
                positions[key] = _move_in_direction(position, direction, 1)
            elif manhattan_distance(
                position, positions[key - 1]
            ) > get_allowed_distance(positions[key - 1], position):
                positions[key] = determine_move(position, positions[key - 1])

                if key == tail_pos:  # Tail
                    tail_locations[positions[key]] += 1


def simulate_rope(input_data: list[str]) -> int:
    """
    Simulate rope movements and return the number of positions
    the tail has visited at least once
    """
    tail_locations: defaultdict[tuple[int, int], int] = defaultdict(int)
    head = (0, 0)
    tail = (0, 0)

    tail_locations[tail] += 1

    for instruction in get_instructions(input_data):
        head, tail = move(instruction, head, tail, tail_locations)

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
        raise SolutionNotFoundError(2022, 9, 1)

    return answer


@register_solution(2022, 9, 2)
def part_two(input_data: list[str]):
    answer = simulate_rope_snake(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 9, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 9)
    part_one(data)
    part_two(data)
