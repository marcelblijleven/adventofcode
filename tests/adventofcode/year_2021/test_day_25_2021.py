from adventofcode.util.helpers import grid_to_string
from adventofcode.year_2021.day_25_2021 import part_one, get_values, do_step

test_input = [
    'v...>>.vv>',
    '.vv>>.vv..',
    '>>.>v>...v',
    '>>v>>.>.v.',
    'v>v.vv.v..',
    '>.>>..v...',
    '.vv..>.>v.',
    'v.v..>>v.v',
    '....v..v.>',
]

step_1 = [
    '....>.>v.>',
    'v.v>.>v.v.',
    '>v>>..>v..',
    '>>v>v>.>.v',
    '.>v.v...v.',
    'v>>.>vvv..',
    '..v...>>..',
    'vv...>>vv.',
    '>.v.v..v.v',
]


def test_do_step():
    grid = get_values(test_input)
    do_step(grid)
    print()
    print(grid_to_string(grid))
    print()
    print(grid_to_string(get_values(step_1)))
    assert grid == get_values(step_1)


def test_part_one():
    assert part_one(test_input) == 58


# def test_part_two():
#     assert part_two(test_input) == 'x'
