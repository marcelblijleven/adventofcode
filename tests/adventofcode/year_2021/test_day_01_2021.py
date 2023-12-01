from adventofcode.year_2021.day_01_2021 import (
    count_increasing_windows,
    sonar_sweep,
    sonar_sweep_sliding_window,
    sonar_sweep_sliding_window_reuse,
)

test_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def test_sonar_sweep():
    assert sonar_sweep(test_input) == 7


def test_sonar_sweep_sliding_window():
    assert sonar_sweep_sliding_window(test_input) == 5


def test_sonar_sweep_sliding_window_reuse():
    assert sonar_sweep_sliding_window_reuse(test_input) == 5


def test_count_increasing_windows():
    windows = [[1, 2, 3], [2, 3, 6], [3, 6, 2], [6, 2, 2]]

    assert count_increasing_windows(windows) == 1
