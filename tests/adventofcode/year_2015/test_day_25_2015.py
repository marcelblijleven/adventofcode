import os

import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2015.day_25_2015 import part_one, part_two


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_one():
    assert part_one(get_input_for_day(2015, 25)) == 2650453


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_two():
    assert part_two(get_input_for_day(2015, 25)) == "hooray"
