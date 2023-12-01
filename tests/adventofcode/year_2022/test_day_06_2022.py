import pytest

from adventofcode.year_2022.day_06_2022 import (
    find_marker,
    find_message_marker,
    part_one,
    part_two,
)

test_input = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]


@pytest.mark.parametrize(
    ["input_str", "expected"],
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_find_marker(input_str: str, expected: int):
    assert find_marker(input_str) == expected


@pytest.mark.parametrize(
    ["input_str", "expected"],
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_find_message_marker(input_str: str, expected: int):
    assert find_message_marker(input_str) == expected


def test_part_one():
    assert part_one(test_input) == 7


def test_part_two():
    assert part_two(test_input) == 19
