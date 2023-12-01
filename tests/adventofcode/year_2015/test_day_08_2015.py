import pytest

from adventofcode.year_2015.day_08_2015 import (
    get_hex_character,
    parse_line,
    parse_line_part_two,
)


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (r'""', 2),
        (r'"abc"', 2),
        (r'"aaa\"aaa"', 3),
        (r'"\x27"', 5),
    ],
)
def test_parse_line(line, expected):
    assert expected == parse_line(line)


def test_get_hex_character():
    assert "'" == get_hex_character(r"\x27")


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        (r'""', 6 - 2),
        (r'"abc"', 9 - 5),
        (r'"aaa\"aaa"', 16 - 10),
        (r'"\x27"', 11 - 6),
    ],
)
def test_part_two(line, expected):
    assert expected == parse_line_part_two(line)
