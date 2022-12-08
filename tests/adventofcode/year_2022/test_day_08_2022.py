from adventofcode.year_2022.day_08_2022 import (
    get_grid,
    get_grid_size,
    get_scenic_scores,
    get_visible_trees,
    part_one,
    part_two,
)

test_input = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]


def test_get_grid_size():
    assert get_grid_size(test_input) == (5, 5)


def test_get_grid():
    assert get_grid(test_input) == {
        (0, 0): 3,
        (0, 1): 2,
        (0, 2): 6,
        (0, 3): 3,
        (0, 4): 3,
        (1, 0): 0,
        (1, 1): 5,
        (1, 2): 5,
        (1, 3): 3,
        (1, 4): 5,
        (2, 0): 3,
        (2, 1): 5,
        (2, 2): 3,
        (2, 3): 5,
        (2, 4): 3,
        (3, 0): 7,
        (3, 1): 1,
        (3, 2): 3,
        (3, 3): 4,
        (3, 4): 9,
        (4, 0): 3,
        (4, 1): 2,
        (4, 2): 2,
        (4, 3): 9,
        (4, 4): 0,
    }


def test_get_visible_trees():
    assert get_visible_trees(test_input) == 21


def test_get_scenic_scores():
    assert get_scenic_scores(test_input) == 8


def test_part_one():
    assert part_one(test_input) == 21


def test_part_two():
    assert part_two(test_input) == 8
