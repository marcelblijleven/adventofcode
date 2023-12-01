import ast
import os

from adventofcode.config import ROOT_DIR


def get_full_year_paths() -> list[str]:
    """
    Retrieves all directories in the ROOT_DIR that start with 'year_'
    """
    paths = [
        os.path.join(ROOT_DIR, val)
        for val in os.listdir(ROOT_DIR)
        if val.startswith("year_")
    ]
    return sorted(paths)


def get_full_day_paths(year_path: str) -> list[str]:
    """
    Retrieves all files in the ROOT_DIR/year_{year} directory that start with 'day_'
    """
    paths = [
        os.path.join(year_path, val)
        for val in os.listdir(year_path)
        if val.startswith("day_")
    ]
    return sorted(paths)


def get_functions_from_day_file(day: str):
    """
    Uses ast to retrieve all top level functions in the provided day file
    """
    with open(day) as f:
        parsed = ast.parse(f.read(), filename=day)

    return [func.name for func in parsed.body if isinstance(func, ast.FunctionDef)]


def clean_year(year_path: str) -> int:
    """
    Removes the 'year_' prefix from the year directory
    """
    year_segment = year_dir_from_path(year_path)
    return int(year_segment[len("year_") :])


def clean_day(day_file: str) -> int:
    """
    Removes the 'day_' prefix, _year suffix and .py extension from the day file
    """
    segments = day_file.split(os.sep)
    day_segment = segments[-1].replace(".py", "")

    return int(day_segment[4:-5])


def year_dir_from_path(year_dir: str) -> str:
    """
    Retrieves the module part from the year directory path
    Example: year_2020
    """
    segments = year_dir.split(os.sep)
    return segments[-1]


def get_full_module_from_day_file(day_file: str) -> str:
    """
    Returns the full module for the given day file
    Example: adventofcode.year_2020.day_01
    """
    segments = day_file.split(os.sep)
    segments = ["adventofcode"] + segments[-2:]
    module = ".".join(segments).replace(".py", "")
    return module
