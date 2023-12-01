import pytest
import pytest_mock

from adventofcode.year_2021.day_12_2021 import (
    CaveExplorer3000,
    get_paths,
    is_big_cave,
    is_small_cave,
    part_one,
    part_two,
)

test_input = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]

test_input_slightly_larger = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

test_input_even_larger = [
    "fs-end",
    "he-DX",
    "fs-he",
    "start-DX",
    "pj-DX",
    "end-zg",
    "zg-sl",
    "zg-pj",
    "pj-he",
    "RW-he",
    "fs-DX",
    "pj-RW",
    "zg-RW",
    "start-pj",
    "he-WI",
    "zg-he",
    "pj-fs",
    "start-RW",
]


@pytest.mark.parametrize(
    ["cave", "expected"],
    [
        ("A", True),
        ("AB", True),
        ("a", False),
        ("ab", False),
        ("Ab", False),
    ],
)
def test_is_big_cave(cave, expected):
    assert is_big_cave(cave) == expected


@pytest.mark.parametrize(
    ["cave", "expected"],
    [
        ("A", False),
        ("AB", False),
        ("a", True),
        ("ab", True),
        ("Ab", False),
    ],
)
def test_is_small_cave(cave, expected):
    assert is_small_cave(cave) == expected


def test_get_paths():
    input_data = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

    assert dict(get_paths(input_data)) == {
        "A": ["start", "c", "b", "end"],
        "b": ["start", "A", "d", "end"],
        "c": ["A"],
        "d": ["b"],
        "end": ["A", "b"],
        "start": ["A", "b"],
    }


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [(test_input, 10), (test_input_slightly_larger, 19), (test_input_even_larger, 226)],
)
def test_cave_explorer_traverse(input_data, expected):
    paths = get_paths(input_data)
    cave_explorer = CaveExplorer3000(paths)
    assert cave_explorer.traverse("start", set()) == expected


@pytest.mark.parametrize(
    ["input_data", "expected"],
    [
        (test_input, 36),
        (test_input_slightly_larger, 103),
        (test_input_even_larger, 3509),
    ],
)
def test_cave_explorer_traverse_part_two(input_data, expected):
    paths = get_paths(input_data)
    cave_explorer = CaveExplorer3000(paths, limit_small_caves=True)
    assert cave_explorer.traverse_part_two("start", set()) == expected


def test_cave_explorer_traverse_with_print(mocker: pytest_mock.MockerFixture):
    mock_console = mocker.patch("adventofcode.year_2021.day_12_2021.console")
    paths = get_paths(test_input)
    cave_explorer = CaveExplorer3000(paths)
    assert cave_explorer.traverse_with_print("start", set()) == 10
    mock_console.print.assert_called()


def test_part_one():
    assert part_one(test_input) == 10


def test_part_two():
    assert part_two(test_input) == 36
