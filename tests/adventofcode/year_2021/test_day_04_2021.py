from adventofcode.year_2021.day_04_2021 import (
    flatten,
    part_one,
    part_two,
    play_bingo,
    transpose_rows,
)

test_input = [
    "7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1",
    "",
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    "6 10  3 18  5",
    "1 12 20 15 19",
    "",
    "3 15  0  2 22",
    "9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    "2  0 12  3  7",
]

test_board_input = [
    "22 13 17 11  0",
    "8  2 23  4 24",
    "21  9 14 16  7",
    "6 10  3 18  5",
    "1 12 20 15 19",
]


def test_play_bingo():
    assert play_bingo(test_input) == 4512


def test_play_bingo_to_lose():
    assert play_bingo(test_input, False) == 1924


def test_transpose_rows():
    rows = [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert transpose_rows(rows) == [[1, 5], [2, 6], [3, 7], [4, 8]]


def test_flatten():
    rows = [[1, 2, 3, 4], [5, 6, 7, 8]]
    assert flatten(rows) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_part_one():
    answer = part_one(test_input)
    assert answer == 4512


def test_part_two():
    answer = part_two(test_input)
    assert answer == 1924
