from adventofcode.year_2021.day_25_2021 import do_step, get_values, part_one

test_input = [
    "v...>>.vv>",
    ".vv>>.vv..",
    ">>.>v>...v",
    ">>v>>.>.v.",
    "v>v.vv.v..",
    ">.>>..v...",
    ".vv..>.>v.",
    "v.v..>>v.v",
    "....v..v.>",
]

step_1 = [
    "....>.>v.>",
    "v.v>.>v.v.",
    ">v>>..>v..",
    ">>v>v>.>.v",
    ".>v.v...v.",
    "v>>.>vvv..",
    "..v...>>..",
    "vv...>>vv.",
    ">.v.v..v.v",
]


def test_do_step():
    grid = get_values(test_input)
    max_x = max(pos[0] for pos in grid.keys())
    max_y = max(pos[1] for pos in grid.keys())
    do_step(grid, max_x, max_y)
    assert grid == get_values(step_1)


def test_part_one():
    assert part_one(test_input) == 58


# def test_part_two():
#     assert part_two(test_input) == 'x'
