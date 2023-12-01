import re
from collections.abc import Callable

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

pattern = re.compile(r"(\d{1,3},\d{1,3}) through (\d{1,3},\d{1,3})")

ActionType = Callable[[bool], bool]

TURN_ON: ActionType = lambda x: True  # noqa: E731, ARG005
TURN_OFF: ActionType = lambda x: False  # noqa: E731, ARG005
TOGGLE: ActionType = lambda x: not x  # noqa: E731


def read_instruction(
    line: str,
) -> tuple[Callable[[bool], bool], tuple[int, ...], tuple[int, ...]]:
    match = pattern.findall(line)

    if len(match) > 0:
        start = tuple(map(int, match[0][0].split(",")))
        end = tuple(map(int, match[0][1].split(",")))

        if line.startswith("turn on"):
            return TURN_ON, start, end
        if line.startswith("turn off"):
            return TURN_OFF, start, end
        if line.startswith("toggle"):
            return TOGGLE, start, end

    raise ValueError("could not read instructions")


def read_instruction_part_two(
    line: str,
) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    match = pattern.findall(line)

    if len(match) > 0:
        start = tuple(map(int, match[0][0].split(",")))
        end = tuple(map(int, match[0][1].split(",")))

        if line.startswith("turn on"):
            return 1, start, end
        if line.startswith("turn off"):
            return -1, start, end
        if line.startswith("toggle"):
            return 2, start, end

    raise ValueError("could not read instructions")


def run_instructions(input_data: list[str]) -> int:
    lights = {}

    for line in input_data:
        action, start, end = read_instruction(line)
        start_x, start_y = start
        end_x, end_y = end

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                light = (x, y)
                if light not in lights:
                    lights[light] = False

                lights[light] = action(lights[light])

    return count_lights(lights)


def run_instructions_part_two(input_data: list[str]) -> int:
    lights = {}

    for line in input_data:
        action, start, end = read_instruction_part_two(line)
        start_x, start_y = start
        end_x, end_y = end

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                light = (x, y)
                if light not in lights:
                    lights[light] = 0

                lights[light] += action

                if lights[light] < 0:
                    lights[light] = 0

    return count_brightness(lights)


def count_lights(lights: dict[tuple[int, int], bool]) -> int:
    return len({light: status for light, status in lights.items() if status})


def count_brightness(lights: dict[tuple[int, int], int]) -> int:
    return sum(lights.values())


@register_solution(2015, 6, 1)
def part_one(input_data: list[str]):
    answer = run_instructions(input_data)

    if not answer:
        raise SolutionNotFoundError(2015, 6, 1)

    return answer


@register_solution(2015, 6, 2)
def part_two(input_data: list[str]):
    answer = run_instructions_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2015, 6, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 6)
    part_one(data)
    part_two(data)
