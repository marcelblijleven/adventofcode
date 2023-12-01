import pytest

from adventofcode.util.math_helpers import gaussian_sum, mean_ceil, mean_floor


@pytest.mark.parametrize("number", [*range(0, 10, 3)])
def test_gaussian_sum(number):
    assert gaussian_sum(number) == sum(range(1, number + 1))


@pytest.mark.parametrize(
    ["target_list", "expected"], [([1, 2, 3, 4, 5], 3), ([13, 34, 45, 68, 5], 33)]
)
def test_mean_floor(target_list, expected):
    assert mean_floor(target_list) == expected


@pytest.mark.parametrize(
    ["target_list", "expected"],
    [([123, 34546, 341, 45], 8764), ([13, 34, 45, 68, 5], 33)],
)
def test_mean_ceil(target_list, expected):
    assert mean_ceil(target_list) == expected
