from pathlib import Path

import pytest

from adventofcode.year_2022.day_07_2022 import (
    find_directory_to_delete,
    find_sum_of_dirs_below_threshold,
    get_dir_sizes,
    get_dirs,
    get_file_path,
    get_filename_size,
    get_sum_of_dirs_below_threshold,
    is_command,
    part_one,
    part_two,
)

test_input = [
    "cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("$ cd d", True),
        ("$ cd ..", True),
        ("$ ls", True),
        ("4060174 j", False),
    ],
)
def test_is_command(line, expected):
    assert is_command(line) == expected


def test_get_file_path():
    current_path = Path("/abc/")
    filename = "def.txt"
    assert str(get_file_path(current_path, filename)) == "/abc/def.txt"


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("4060174 j", ("j", 4060174)),
        ("5626152 d.ext", ("d.ext", 5626152)),
    ],
)
def test_get_filename_size(line, expected):
    assert get_filename_size(line) == expected


def test_get_dir_sizes():
    files = {
        Path("/a.txt"): 1,
        Path("/b/b.txt"): 2,
        Path("/b/c/c.txt"): 3,
        Path("/b/c/d/d.txt"): 4,
    }

    dir_sizes = get_dir_sizes(files)
    assert dir_sizes == {
        Path("/"): 10,
        Path("/b"): 9,
        Path("/b/c"): 7,
        Path("/b/c/d"): 4,
    }


def test_get_sum_of_dirs_below_threshold():
    dirs = {Path("/"): 10, Path("/b"): 9, Path("/b/c"): 7, Path("/b/c/d"): 4}

    assert get_sum_of_dirs_below_threshold(dirs, 9) == 11


def test_get_dirs():
    assert get_dirs(test_input) == {
        Path("/"): 48381165,
        Path("/a"): 94853,
        Path("/a/e"): 584,
        Path("/d"): 24933642,
    }


def test_find_sum_of_dirs_below_threshold():
    assert find_sum_of_dirs_below_threshold(test_input) == 95437


def test_find_directory_to_delete():
    assert find_directory_to_delete(test_input) == 24933642


def test_part_one():
    assert part_one(test_input) == 95437


def test_part_two():
    assert part_two(test_input) == 24933642
