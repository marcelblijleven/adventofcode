from adventofcode.year_2020.day_13_2020 import (
    get_answer_part_one,
    get_departure_times,
    get_sequential_departure_times,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "939",
    "7,13,x,x,59,x,31,19",
]


def test_parse_input():
    assert parse_input(test_input) == (939, [7, 13, 59, 31, 19])


def test_get_departure_times():
    expected = {7: [945, 952, 959], 13: [949], 19: [950], 31: [961], 59: [944]}

    assert get_departure_times(939, [7, 13, 59, 31, 19]) == expected


def test_get_answer_part_one():
    times = {7: [945, 952, 959], 13: [949], 19: [950], 31: [961], 59: [944]}
    assert get_answer_part_one(939, times) == 295


def test_get_sequential_departure_times():
    assert get_sequential_departure_times(test_input[1]) == 1068781


def test_part_one():
    answer = part_one(test_input)
    assert answer == 295


def test_part_two():
    answer = part_two(test_input)
    assert answer == 1068781
