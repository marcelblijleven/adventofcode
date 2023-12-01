from collections.abc import Callable

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

instructions_funcs: dict[str, Callable[[int], int]] = {
    "hlf r": lambda r: int(r / 2),
    "tpl r": lambda r: int(r * 3),
    "inc r": lambda r: r + 1,
}


def run_program(input_data: list[str], registers: dict[str, int]) -> int:
    position = 0

    while position < len(input_data):
        instruction, content = parse_instruction(input_data[position])

        if instruction == "hlf":
            registers[content] = int(registers[content] / 2)
            position += 1
        elif instruction == "tpl":
            registers[content] = registers[content] * 3
            position += 1
        elif instruction == "inc":
            registers[content] += 1
            position += 1
        elif instruction == "jmp":
            position += int(content)
        elif instruction == "jie":
            register, jump_size = content.split(", ")
            if registers[register] % 2 == 0:
                position += int(jump_size)
            else:
                position += 1
        elif instruction == "jio":
            register, jump_size = content.split(", ")
            if registers[register] == 1:
                position += int(jump_size)
            else:
                position += 1
        else:
            raise ValueError(f"invalid instruction received: {instruction}")

    return registers["b"]


def parse_instruction(line: str) -> tuple[str, str]:
    instruction_key, instruction = line.split(" ", 1)
    return instruction_key, instruction


@register_solution(2015, 23, 1)
def part_one(input_data: list[str]):
    registers = {"a": 0, "b": 0}
    answer = run_program(input_data, registers)

    if not answer:
        raise SolutionNotFoundError(2015, 23, 1)

    return answer


@register_solution(2015, 23, 2)
def part_two(input_data: list[str]):
    registers = {"a": 1, "b": 0}
    answer = run_program(input_data, registers)

    if not answer:
        raise SolutionNotFoundError(2015, 23, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 23)
    part_one(data)
    part_two(data)
