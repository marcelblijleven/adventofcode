import pytest

from adventofcode.year_2015.day_02_2015 import (
    get_surface,
    get_ribbon,
    parse_line,
    part_one,
    get_input_for_day,
    part_two,
)


@pytest.mark.parametrize(["line", "expected"], [("2x3x4", 58), ("1x1x10", 43)])
def test_get_surface(line, expected):
    assert expected == get_surface(line)


@pytest.mark.parametrize(["line", "expected"], [("2x3x4", 34), ("1x1x10", 14)])
def test_get_ribbon(line, expected):
    assert expected == get_ribbon(line)


def test_parse_line():
    with pytest.raises(ValueError) as wrapped_e:
        parse_line("incorrect line")

    assert str(wrapped_e.value) == "could not parse line"


def test_part_one():
    assert part_one(get_input_for_day(2015, 2)) == 1606483


def test_part_two():
    assert part_two(get_input_for_day(2015, 2)) == 3842356
