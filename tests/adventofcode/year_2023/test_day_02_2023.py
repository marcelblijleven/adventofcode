import pytest

from adventofcode.year_2023.day_02_2023 import parse_game, part_one, part_two

test_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


@pytest.mark.parametrize(
    ["game", "expected"],
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            [{"blue": 3, "red": 4}, {"blue": 6, "green": 2, "red": 1}, {"green": 2}],
        ),
        (
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            [
                {"blue": 1, "green": 2},
                {"blue": 4, "green": 3, "red": 1},
                {"blue": 1, "green": 1},
            ],
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            [
                {"blue": 6, "green": 8, "red": 20},
                {"blue": 5, "green": 13, "red": 4},
                {"green": 5, "red": 1},
            ],
        ),
        (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            [
                {"blue": 6, "green": 1, "red": 3},
                {"green": 3, "red": 6},
                {"blue": 15, "green": 3, "red": 14},
            ],
        ),
        (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            [{"blue": 1, "green": 3, "red": 6}, {"blue": 2, "green": 2, "red": 1}],
        ),
    ],
)
def test_parse_game(game, expected):
    assert parse_game(game) == expected


def test_part_one():
    assert part_one(test_input) == 8


def test_part_two():
    assert part_two(test_input) == 2286
