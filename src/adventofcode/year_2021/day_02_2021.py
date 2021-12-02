from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


Instruction = tuple[str, int]
Position = tuple[int, int]

FORWARD = 'forward'
DOWN = 'down'
UP = 'up'


def parse_instruction(instruction: str) -> Instruction:
    direction, steps = instruction.split(' ')
    return direction, int(steps)


def parse_instructions(input_data: List[str]) -> List[Instruction]:
    instructions: List[Instruction] = []

    for instruction in input_data:
        instructions.append(parse_instruction(instruction))

    return instructions


def _get_new_position(position: Position, instruction: Instruction) -> Position:
    x, y = position
    direction, steps = instruction

    if direction == FORWARD:
        x += steps
    elif direction == UP:
        y -= steps
    elif direction == DOWN:
        y += steps
    else:
        raise ValueError(f'unknown direction received: {direction}')

    return x, y


def _get_new_position_with_aim(position: Position, aim: int, instruction: Instruction) ->tuple[Position, int]:
    x, y = position
    direction, steps = instruction

    if direction == FORWARD:
        x += steps
        y += aim * steps
    elif direction == UP:
        aim -= steps
    elif direction == DOWN:
        aim += steps
    else:
        raise ValueError(f'unknown direction received: {direction}')

    return (x, y), aim


def get_new_position(position: Position, aim: int, instruction: Instruction, include_aim: bool) -> tuple[Position, int]:
    if not include_aim:
        return _get_new_position(position, instruction), 0

    return _get_new_position_with_aim(position, aim, instruction)


def move_submarine(input_data: List[str], include_aim: bool) -> Position:
    position = (0, 0)
    aim = 0
    instructions = parse_instructions(input_data)

    for instruction in instructions:
        position, aim = get_new_position(position, aim, instruction, include_aim)

    return position


@solution_timer(2021, 2, 1)
def part_one(input_data: List[str]):
    x, y = move_submarine(input_data, False)
    answer = x * y

    if not answer:
        raise SolutionNotFoundException(2021, 2, 1)

    return answer


@solution_timer(2021, 2, 2)
def part_two(input_data: List[str]):
    x, y = move_submarine(input_data, True)
    answer = x * y

    if not answer:
        raise SolutionNotFoundException(2021, 2, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 2)
    part_one(data)
    part_two(data)
