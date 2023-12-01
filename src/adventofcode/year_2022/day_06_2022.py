from collections import deque

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def is_marker(checker: deque[str], expected_len: int = 4) -> bool:
    """Checks if the checker consists of all unique letters"""
    return len(set(checker)) == expected_len


def find_marker(input_str: str) -> int:
    """Finds the first start-of-packet marker"""
    checker: deque[str] = deque(maxlen=4)

    for idx, letter in enumerate(input_str):
        checker.append(letter)

        if idx > 3 and is_marker(checker):
            return idx + 1

    raise ValueError("invalid message")


def find_message_marker(input_str: str) -> int:
    """Finds the first start-of-message marker"""
    checker: deque[str] = deque(maxlen=14)

    for idx, letter in enumerate(input_str):
        checker.append(letter)

        if idx > 3 and is_marker(checker, expected_len=14):
            return idx + 1
    err = "invalid_message"
    raise ValueError(err)


@register_solution(2022, 6, 1)
def part_one(input_data: list[str]):
    answer = find_marker(input_data[0])

    if not answer:
        raise SolutionNotFoundError(2022, 6, 1)

    return answer


@register_solution(2022, 6, 2)
def part_two(input_data: list[str]):
    answer = find_message_marker(input_data[0])

    if not answer:
        raise SolutionNotFoundError(2022, 6, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 6)
    part_one(data)
    part_two(data)
