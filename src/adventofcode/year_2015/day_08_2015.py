import ast
import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

QUOTE_PATTERN = re.compile(r'(\\")')
HEX_PATTERN = re.compile(r"(\\x[a-f0-9]{2})")
SLASH_PATTERN = re.compile(r'(\\[^a-z"])')


def get_hex_character(hex_str: str) -> str:
    num = int(hex_str[-2:], 16)
    return chr(num)


def get_in_memory_count(line: str) -> int:
    return len(ast.literal_eval(line))


def parse_line(line: str) -> int:
    literal_count = len(line)
    in_memory_count = get_in_memory_count(line)
    value = literal_count - in_memory_count
    return value


def parse_line_part_two(line: str) -> int:
    translation_table = {
        '"': r"\"",
        "\\": r"\\",
    }

    old_length = len(line)
    new_line = line.translate(str.maketrans(translation_table))  # type: ignore
    new_length = len(new_line) + 2
    return new_length - old_length


def parse_lines(input_data: list[str]) -> int:
    count = 0

    for line in input_data:
        count += parse_line(line)

    return count


def parse_lines_part_two(input_data: list[str]) -> int:
    count = 0

    for line in input_data:
        count += parse_line_part_two(line)

    return count


@register_solution(2015, 8, 1)
def part_one(input_data: list[str]):
    answer = parse_lines(input_data)

    if not answer:
        raise SolutionNotFoundError(2015, 8, 1)

    return answer


@register_solution(2015, 8, 2)
def part_two(input_data: list[str]):
    answer = parse_lines_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2015, 8, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 8)
    part_one(data)
    part_two(data)
