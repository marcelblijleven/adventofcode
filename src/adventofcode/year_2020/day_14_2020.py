import re
from collections.abc import Generator
from itertools import combinations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

MEMORY_PATTERN = re.compile(r"(\d+).+ = (\d+)$")


def get_mask(line: str) -> str:
    return line.split("mask = ")[1]


def value_to_36_bit_string(value: str) -> str:
    int_value = int(value)
    return format(int_value, "036b")


def apply_mask_to_value(value: str, mask: str) -> int:
    masked = "".join(
        [
            value if mask_value == "X" else mask_value
            for value, mask_value in zip(value, mask, strict=True)
        ]
    )
    return int(masked, 2)


def apply_mask_to_address(address: str, mask: str) -> Generator[int, None, None]:
    addresses: list[str] = []
    floating_bits = mask.count("X")
    bits = ["0", "1"] * floating_bits

    masked_address = "".join(
        [
            character if mask_value == "0" else mask_value
            for character, mask_value in zip(address, mask, strict=True)
        ]
    )

    for combination in set(combinations(bits, floating_bits)):
        new_address = masked_address
        for bit in combination:
            new_address = new_address.replace("X", bit, 1)

        addresses.append(new_address)

    for address in addresses:
        yield int(address, 2)


def parse_program(input_data: list[str]) -> dict[int, int]:
    current_mask = ""
    memory: dict[int, int] = {}

    for line in input_data:
        if line.startswith("mask"):
            current_mask = get_mask(line)
        else:
            address, value = MEMORY_PATTERN.findall(line)[0]
            value = value_to_36_bit_string(value)
            memory[int(address)] = apply_mask_to_value(value, current_mask)

    return memory


def parse_program_version_2(input_data: list[str]) -> dict[int, int]:
    current_mask = ""
    memory: dict[int, int] = {}

    for line in input_data:
        if line.startswith("mask"):
            current_mask = get_mask(line)
        else:
            address, value = MEMORY_PATTERN.findall(line)[0]
            address = value_to_36_bit_string(address)
            int_value = int(value)

            for a in apply_mask_to_address(address, current_mask):
                memory[a] = int_value

    return memory


def count_memory(memory: dict[int, int]) -> int:
    return sum(memory.values())


@register_solution(2020, 14, 1)
def part_one(input_data: list[str]):
    memory = parse_program(input_data)
    answer = count_memory(memory)

    if not answer:
        raise SolutionNotFoundError(2020, 14, 1)

    return answer


@register_solution(2020, 14, 2)
def part_two(input_data: list[str]):
    memory = parse_program_version_2(input_data)
    answer = count_memory(memory)

    if not answer:
        raise SolutionNotFoundError(2020, 14, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2020, 14)
    part_one(data)
    part_two(data)
