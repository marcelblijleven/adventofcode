import os

import pytest

from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.year_2015.day_24_2015 import (
    get_quantum_entanglement,
    move_packages_into_groups,
    part_one,
    part_two,
)

test_input = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]


@pytest.mark.parametrize(
    ["packages", "expected"],
    [
        ([11, 9], 99),
        ([10, 9, 1], 90),
        ([10, 8, 2], 160),
        ([10, 7, 3], 210),
        ([10, 5, 4, 1], 200),
        ([10, 5, 3, 2], 300),
        ([10, 4, 3, 2, 1], 240),
        ([9, 8, 3], 216),
        ([9, 7, 4], 252),
    ],
)
def test_get_quantum_entanglement(packages, expected):
    assert get_quantum_entanglement(packages) == expected


def test_move_packages_into_groups():
    assert move_packages_into_groups(test_input, 3) == 99
    assert move_packages_into_groups(test_input, 4) == 44


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_one():
    assert part_one(get_input_for_day(2015, 24)) == 10723906903


@pytest.mark.skipif(
    os.environ.get("CI", "false") == "true", reason="inputs not available in CI"
)
def test_part_two():
    assert part_two(get_input_for_day(2015, 24)) == 74850409
