import os

import pytest

from adventofcode.year_2015.day_02_2015 import (
    get_input_for_day,
    get_ribbon,
    get_surface,
    parse_line,
    part_one,
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


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_one():
    assert part_one(get_input_for_day(2015, 2)) == 1606483


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_two():
    assert part_two(get_input_for_day(2015, 2)) == 3842356
