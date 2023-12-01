import pytest

from adventofcode.year_2020.day_11_2020 import (
    get_adjacent_coordinates,
    get_layout,
    get_x_y_range,
    los_seating_iteration,
    start_iterating,
)

test_input = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL",
]


@pytest.mark.parametrize(
    ["coords", "expected"],
    [
        ((0, 0), "1"),
        ((1, 0), "2"),
        ((2, 0), "3"),
        ((0, 1), "4"),
        ((1, 1), "5"),
        ((2, 1), "6"),
    ],
)
def test_get_layout(coords, expected):
    lines = ["123", "456"]
    layout = get_layout(lines)
    x, y = coords
    assert expected == layout[x, y]


def test_get_x_y_range():
    layout = {
        (0, 1): "test",
        (1, 1): "test",
        (2, 2): "test",
        (3, 2): "test",
    }

    max_x, max_y = get_x_y_range(layout)
    assert 3 == max_x
    assert 2 == max_y


def test_get_adjacent_coordinates():
    lines = [
        "123",
        "456",
        "789",
    ]

    layout = get_layout(lines)

    x, y = 0, 0
    coords = get_adjacent_coordinates(layout, x, y)

    assert (0, 1) in coords.keys()
    assert (1, 0) in coords.keys()
    assert (1, 1) in coords.keys()

    x, y = 1, 1

    coords = get_adjacent_coordinates(layout, x, y)

    assert (0, 1) in coords.keys()
    assert (0, 1) in coords.keys()
    assert (0, 2) in coords.keys()
    assert (1, 1) in coords.keys()
    assert (1, 2) in coords.keys()
    assert (2, 1) in coords.keys()
    assert (2, 1) in coords.keys()
    assert (2, 2) in coords.keys()


def test_start_iterating():
    layout = get_layout(test_input)
    assert 37 == start_iterating(layout)


def test_start_iterating_part_two():
    layout = get_layout(test_input)
    assert 26 == start_iterating(layout, los_seating_iteration)
