import pytest

from adventofcode.year_2023.day_07_2023 import (
    hands,
    parse_hand,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def test_parse_input():
    assert list(parse_input(test_input)) == [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]


@pytest.mark.parametrize(
    ["hand", "expected"],
    [
        ("32T3K", hands["One pair"]),
        ("T55J5", hands["Three of a kind"]),
        ("KK677", hands["Two pair"]),
        ("KTJJT", hands["Two pair"]),
        ("QQQJA", hands["Three of a kind"]),
        ("AAAAA", hands["Five of a kind"]),
        ("AAAAK", hands["Four of a kind"]),
        ("AAAKK", hands["Full house"]),
    ],
)
def test_parse_hand(hand, expected):
    assert parse_hand(hand, with_jokers=False) == expected


@pytest.mark.parametrize(
    ["hand", "expected"],
    [
        ("32T3K", hands["One pair"]),
        ("T55J5", hands["Four of a kind"]),
        ("KK677", hands["Two pair"]),
        ("KTJJT", hands["Four of a kind"]),
        ("QQQJA", hands["Four of a kind"]),
        ("AAAAA", hands["Five of a kind"]),
        ("AAAAK", hands["Four of a kind"]),
        ("AAAKK", hands["Full house"]),
    ],
)
def test_parse_hand_with_joker(hand, expected):
    assert parse_hand(hand, with_jokers=True) == expected


def test_part_one():
    assert part_one(test_input) == 6440


def test_part_two():
    assert part_two(test_input) == 5905
