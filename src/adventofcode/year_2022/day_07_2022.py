import os.path
from collections import defaultdict
from pathlib import Path

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def is_command(line: str) -> bool:
    """Checks whether the provided line is a prompt"""
    return line.startswith("$")


def get_file_path(current_path: Path, filename: str) -> Path:
    """Get path for file"""
    return current_path / filename


def get_filename_size(file_line: str) -> tuple[str, int]:
    """Get file name and file size from file line"""
    size_str, _, name = file_line.partition(" ")
    return name, int(size_str)


def change_directory(current_path: Path, arg: str) -> Path:
    """Change directory"""
    next_path = current_path / arg
    return Path(os.path.abspath(next_path))


def get_dir_sizes(files: dict[Path, int]) -> dict[Path, int]:
    """Condense files into dirs with sizes"""
    dirs: defaultdict[Path, int] = defaultdict(int)

    for file, size in files.items():
        parent = file.parent
        dirs[parent] += size

        while parent.parent != parent:
            dirs[parent.parent] += size
            parent = parent.parent

    return dirs


def get_sum_of_dirs_below_threshold(
    dirs: dict[Path, int], threshold: int = 100000
) -> int:
    """Sum the size of all dirs with a size below threshold"""
    total: int = 0

    for size in dirs.values():
        if size < threshold:
            total += size
    return total


def get_dirs(input_data: list[str]) -> dict[Path, int]:
    """
    Run through all commands in the input to get all the dirs
    with sizes
    """
    current_path = Path("/")
    files: dict[Path, int] = {}

    for row in input_data[1:]:  # Skip first as it is cd into root
        if is_command(row) and "cd" in row:
            current_path = change_directory(current_path, row.rpartition(" ")[-1])
        elif is_command(row) and "ls" in row:
            continue  # NOTE: skip for now
        elif not is_command(row) and "dir" in row:
            continue  # NOTE: skip for now
        else:
            filename, size = get_filename_size(row)
            if (filepath := get_file_path(current_path, filename)) not in files:
                files[filepath] = size

    return get_dir_sizes(files)


def find_sum_of_dirs_below_threshold(input_data: list[str]) -> int:
    """Find the sum of all dir sizes below threshold"""
    dirs = get_dirs(input_data)
    total_size = get_sum_of_dirs_below_threshold(dirs)
    return total_size


def find_directory_to_delete(input_data: list[str]) -> int:
    """
    Find total size of the smallest directory to delete
    to free enough space for the update

    Total disk space is 70000000
    Required free space is 30000000
    """
    dirs = get_dirs(input_data)
    root_size = dirs[Path("/")]
    current_free_space = 70000000 - root_size
    minimum_space = 30000000 - current_free_space

    return min([value for value in dirs.values() if value >= minimum_space])


@register_solution(2022, 7, 1)
def part_one(input_data: list[str]):
    answer = find_sum_of_dirs_below_threshold(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 7, 1)

    return answer


@register_solution(2022, 7, 2)
def part_two(input_data: list[str]):
    answer = find_directory_to_delete(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 7, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 7)
    part_one(data)
    part_two(data)
