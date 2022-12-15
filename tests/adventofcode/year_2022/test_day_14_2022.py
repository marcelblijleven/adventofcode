from adventofcode.year_2022.day_14_2022 import (
    count_units_of_sand,
    get_abyss,
    get_floor,
    part_one,
    part_two,
    scan_cave,
)

test_input = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9",
]


def test_scan_cave():
    cave = scan_cave(test_input)
    assert len(cave.keys()) == 20


def test_get_abyss():
    assert get_abyss({(1, 1): "a", (2, 2): "b"}) == 2


def test_get_floor():
    assert get_floor({(1, 1): "a", (2, 2): "b"}) == 4


def test_count_units_of_sand():
    assert count_units_of_sand(test_input) == 24


def test_part_one():
    assert part_one(test_input) == 24


def test_part_two():
    assert part_two(test_input) == 93
