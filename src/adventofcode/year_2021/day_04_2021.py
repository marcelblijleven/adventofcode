import re
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

line_pattern = re.compile(r'(\d+)')


def transpose_rows(rows: List[List[int]]) -> List[List[int]]:
    columns: List[List[int]] = []

    for sublist in zip(*rows):
        columns.append(list(sublist))

    return columns


def flatten(list_of_lists: List[List[int]]) -> List[int]:
    flat: List[int] = []

    for sublist in list_of_lists:
        for value in sublist:
            flat.append(value)

    return flat


class Board:
    columns: List[List[int]]
    rows: List[List[int]]
    drawn_numbers: List[int]
    has_bingo: bool

    def __init__(self, lines: List[str]):
        self.has_bingo = False
        self.rows = []
        self.columns = []
        self.drawn_numbers = []
        self._parse_lines(lines)

    def _parse_lines(self, lines: List[str]) -> None:
        for line in lines:
            self.rows.append(list(map(int, line_pattern.findall(line))))

        self.columns = transpose_rows(self.rows)

    @property
    def unmarked_numbers(self) -> int:
        return sum(flatten(self.columns))

    def draw_number(self, number: int) -> None:
        self.drawn_numbers.append(number)
        index = 0

        for row, column in zip(self.rows, self.columns):
            new_row = [value for value in row if value != number]
            new_column = [value for value in column if value != number]
            self.rows[index] = new_row
            self.columns[index] = new_column

            if not len(new_row) or not len(new_column):
                self.has_bingo = True

            index += 1


def parse_input_data(input_data: List[str]) -> tuple[List[int], List[Board]]:
    numbers = list(map(int, input_data[0].split(',')))
    boards: List[Board] = []

    for chunk in '\n'.join(input_data[2:]).split('\n\n'):
        lines = chunk.split('\n')
        boards.append(Board(lines))

    return numbers, boards


def play_bingo(input_data: List[str], first_board=True) -> int:
    numbers, boards = parse_input_data(input_data)
    winning_boards: List[Board] = []
    drawn_numbers: List[int] = []

    for number in numbers:
        drawn_numbers.append(number)

        for board in [board for board in boards if not board.has_bingo]:
            board.draw_number(number)

            if board.has_bingo:
                winning_boards.append(board)

                if first_board:
                    return board.unmarked_numbers * number

        if all([board.has_bingo for board in boards]):
            break

    last_board = winning_boards[-1]
    last_number = drawn_numbers[-1]

    return last_board.unmarked_numbers * last_number


@solution_timer(2021, 4, 1)
def part_one(input_data: List[str]):
    answer = play_bingo(input_data)

    if not answer:
        raise SolutionNotFoundException(2021, 4, 1)

    return answer


@solution_timer(2021, 4, 2)
def part_two(input_data: List[str]):
    answer = play_bingo(input_data, first_board=False)

    if not answer:
        raise SolutionNotFoundException(2021, 4, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 4)
    part_one(data)
    part_two(data)
