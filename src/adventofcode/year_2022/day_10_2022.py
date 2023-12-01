from collections.abc import Generator

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def parse_instruction(line: str) -> int | None:
    if line == "noop":
        return None

    instruction, _, value = line.partition(" ")
    return int(value)


def start_cycles(input_data: list[str]) -> Generator[int, int, int]:
    x = 1
    cycle = 0

    for line in input_data:
        if (value := parse_instruction(line)) is None:
            cycle += 1
            yield x
        else:
            # instruction is addx, takes two cycles
            cycle += 1
            yield x  # first cycle, nothing changes
            cycle += 1
            yield x  # second cycle, x increases
            x += value

    return x


def get_signal_strength(input_data: list[str]) -> int:
    signal_strength = 0
    for cycle, x_value in enumerate(start_cycles(input_data), start=1):
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength += cycle * x_value

    return signal_strength


def draw_crt(input_data: list[str]) -> str:
    crt_rows: list[str] = []
    crt_row = [" "] * 40
    cycle_modifier = 0

    for cycle, x_value in enumerate(start_cycles(input_data), start=1):
        sprite = x_value
        crt_position = cycle - 1 - cycle_modifier

        for sprite_position in [sprite - 1, sprite, sprite + 1]:
            if crt_position == sprite_position:
                crt_row[crt_position] = "█"

        if not cycle % 40:
            cycle_modifier += 40
            crt_rows.append("".join(crt_row))
            crt_row = [" "] * 40

    value = "\n".join(crt_rows)
    print(value)  # noqa
    return value


@register_solution(2022, 10, 1)
def part_one(input_data: list[str]):
    answer = get_signal_strength(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 10, 1)

    return answer


@register_solution(2022, 10, 2)
def part_two(input_data: list[str]):
    answer = draw_crt(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 10, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 10)
    part_one(data)
    part_two(data)
