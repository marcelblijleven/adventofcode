from collections import deque

from adventofcode.year_2023.day_08_2023 import (
    follow_instructions,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

test_input_2 = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]

test_input_3 = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]


def test_parse_input():
    assert parse_input(test_input_2) == (
        deque("LLR"),
        {
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "ZZZ"),
            "ZZZ": ("ZZZ", "ZZZ"),
        },
    )


def test_follow_instructions():
    assert follow_instructions(test_input) == 2
    assert follow_instructions(test_input_2) == 6


def test_part_one():
    assert part_one(test_input_2) == 6


def test_part_two():
    assert part_two(test_input_3) == 6
