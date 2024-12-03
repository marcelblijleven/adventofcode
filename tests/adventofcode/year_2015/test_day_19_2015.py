import os

import pytest

from adventofcode.year_2015.day_19_2015 import get_input_for_day, part_one, part_two


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_one():
    assert part_one(get_input_for_day(2015, 19)) == 518


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_two():
    assert part_two(get_input_for_day(2015, 19)) == 200
