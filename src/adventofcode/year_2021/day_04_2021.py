import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

line_pattern = re.compile(r"(\d+)")


def transpose_rows(rows: list[list[int]]) -> list[list[int]]:
    columns: list[list[int]] = []

    for sublist in zip(*rows, strict=True):
        columns.append(list(sublist))

    return columns


def flatten(list_of_lists: list[list[int]]) -> list[int]:
    flat: list[int] = []

    for sublist in list_of_lists:
        for value in sublist:
            flat.append(value)

    return flat


class Board:
    columns: list[list[int]]
    rows: list[list[int]]
    drawn_numbers: list[int]
    has_bingo: bool

    def __init__(self, lines: list[str]):
        self.has_bingo = False
        self.rows = []
        self.columns = []
        self.drawn_numbers = []
        self._parse_lines(lines)

    def _parse_lines(self, lines: list[str]) -> None:
        for line in lines:
            self.rows.append(list(map(int, line_pattern.findall(line))))

        self.columns = transpose_rows(self.rows)

    @property
    def unmarked_numbers(self) -> int:
        return sum(flatten(self.columns))

    def draw_number(self, number: int) -> None:
        self.drawn_numbers.append(number)
        index = 0

        for row, column in zip(self.rows, self.columns, strict=True):
            new_row = [value for value in row if value != number]
            new_column = [value for value in column if value != number]
            self.rows[index] = new_row
            self.columns[index] = new_column

            if not len(new_row) or not len(new_column):
                self.has_bingo = True

            index += 1


def parse_input_data(input_data: list[str]) -> tuple[list[int], list[Board]]:
    numbers = list(map(int, input_data[0].split(",")))
    boards: list[Board] = []

    for chunk in "\n".join(input_data[2:]).split("\n\n"):
        lines = chunk.split("\n")
        boards.append(Board(lines))

    return numbers, boards


def play_bingo(input_data: list[str], first_board=True) -> int:
    numbers, boards = parse_input_data(input_data)
    winning_boards: list[Board] = []
    drawn_numbers: list[int] = []

    for number in numbers:
        drawn_numbers.append(number)

        for board in [board for board in boards if not board.has_bingo]:
            board.draw_number(number)

            if board.has_bingo:
                winning_boards.append(board)

                if first_board:
                    return board.unmarked_numbers * number

        if all([board.has_bingo for board in boards]):  # noqa
            break

    last_board = winning_boards[-1]
    last_number = drawn_numbers[-1]

    return last_board.unmarked_numbers * last_number


@register_solution(2021, 4, 1)
def part_one(input_data: list[str]):
    answer = play_bingo(input_data)

    if not answer:
        raise SolutionNotFoundError(2021, 4, 1)

    return answer


@register_solution(2021, 4, 2)
def part_two(input_data: list[str]):
    answer = play_bingo(input_data, first_board=False)

    if not answer:
        raise SolutionNotFoundError(2021, 4, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 4)
    part_one(data)
    part_two(data)
