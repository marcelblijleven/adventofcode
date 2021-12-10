from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

POINTS_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

POINTS_MAP_AUTOCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

PAIRS_REVERSED = {v: k for k, v in PAIRS.items()}


def _is_open(character: str) -> bool:
    return character in '([{<'


def _is_close(character: str) -> bool:
    return character in ')]}>'


def reduce_line(line: str) -> str:
    first_to_close: List[str] = []

    for character in line:
        if _is_open(character):
            first_to_close.append(character)
        elif _is_close(character):
            if first_to_close[-1] == PAIRS_REVERSED[character]:
                first_to_close.pop(-1)
            else:
                return character
        else:
            raise ValueError(f'unknown character received: {character}')

    return ''


def find_corrupted_characters(lines: List[str]) -> List[str]:
    corrupted_characters: List[str] = []

    for line in lines:
        if len(character := reduce_line(line)) == 0:
            continue

        corrupted_characters.append(character)

    return corrupted_characters


def count_points_corrupted_characters(corrupted_characters: List[str]) -> int:
    total = 0

    for key, value in POINTS_MAP.items():
        total += corrupted_characters.count(key) * value

    return total


def filter_lines(lines: List[str]) -> List[str]:
    return list(filter(lambda line: len(reduce_line(line)) == 0, lines))


def find_closing_characters(lines: List[str]) -> List[str]:
    lines = filter_lines(lines)
    closing_characters: List[str] = []

    for line in lines:
        first_to_close: List[str] = []
        for character in line:
            if _is_open(character):
                first_to_close.append(character)
            elif _is_close(character):
                first_to_close.reverse()
                for idx, to_close in enumerate(first_to_close):
                    if PAIRS_REVERSED[character] == to_close:
                        first_to_close.pop(idx)
                        break

                first_to_close.reverse()

        first_to_close.reverse()
        if len(first_to_close) > 0:
            characters = ''.join(first_to_close).translate(str.maketrans(PAIRS))  # type: ignore
            closing_characters.append(characters)

    return closing_characters


def count_points_autocomplete(closing_characters: List[str]) -> int:
    total: List[int] = []

    for line in closing_characters:
        subtotal = 0
        for character in line:
            subtotal *= 5
            subtotal += POINTS_MAP_AUTOCOMPLETE[character]

        total.append(subtotal)

    total.sort()
    mid = int((len(total)) / 2)
    return total[mid]


@solution_timer(2021, 10, 1)
def part_one(input_data: List[str]):
    corrupted_characters = find_corrupted_characters(input_data)
    answer = count_points_corrupted_characters(corrupted_characters)

    if not answer:
        raise SolutionNotFoundException(2021, 10, 1)

    return answer


@solution_timer(2021, 10, 2)
def part_two(input_data: List[str]):
    closing_characters = find_closing_characters(input_data)
    answer = count_points_autocomplete(closing_characters)

    if not answer:
        raise SolutionNotFoundException(2021, 10, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 10)
    part_one(data)
    part_two(data)
