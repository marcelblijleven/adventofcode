import pytest

from adventofcode.year_2023.day_07_2023 import part_two, part_one, parse_input, parse_hand, hands

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


@pytest.mark.parametrize(["hand", "expected"], [
    ("32T3K", hands["High card"]),
    ("T55J5", hands["Three of a kind"]),
    ("KK677", hands["Two pair"]),
    ("KTJJT", hands["Two pair"]),
    ("QQQJA", hands["Three of a kind"]),
    ("AAAAA", hands["Five of a kind"]),
    ("AAAAK", hands["Four of a kind"]),
    ("AAAKK", hands["Full house"]),
])
def test_parse_hand(hand, expected):
    assert parse_hand(hand) == expected


def test_part_one():
    assert part_one(test_input) == 6440


def test_part_two():
    assert part_two(test_input) == 5905
