from adventofcode.year_2022.day_02_2022 import (
    part_one,
    part_two,
    play_round_one,
    play_round_two,
)

test_input = [
    "A Y",
    "B X",
    "C Z",
]


def test_play_round_one():
    assert play_round_one(test_input) == 15


def test_play_round_two():
    assert play_round_two(test_input) == 12


def test_part_one():
    assert part_one(test_input) == 15


def test_part_two():
    assert part_two(test_input) == 12
