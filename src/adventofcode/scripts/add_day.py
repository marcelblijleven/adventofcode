import os
import sys
from argparse import ArgumentParser

from httpx import HTTPError

from adventofcode.config import ROOT_DIR
from adventofcode.scripts.get_inputs import get_input
from adventofcode.util.console import console
from adventofcode.util.input_helpers import get_input_for_day

UNKNOWN_EXCEPTION = "unknown exception occurred in verify_input_exists"


def add_day():
    """
    Creates a solution and test file for the provided year and day
    If the input for that day does not exist, it will be downloaded from
    the advent of code website
    """
    year, day = _parse_args(sys.argv[1:])
    console.print(f"Creating solution day file for year {year} day {day}")

    # Solution file
    module_path = os.path.join(ROOT_DIR, f"year_{year}")
    solution_file = os.path.join(module_path, f"day_{day:02}_{year}.py")
    create_module_dir(module_path)
    write_solution_template(solution_file, year, day)

    # Test file
    test_module_path = os.path.abspath(
        os.path.join(ROOT_DIR, "../../tests/adventofcode", f"year_{year}")
    )
    test_file = os.path.join(test_module_path, f"test_day_{day:02}_{year}.py")
    create_module_dir(test_module_path)
    write_test_template(test_file, year, day)

    verify_input_exists(year, day)


def write_solution_template(path: str, year: int, day: int) -> None:
    """Writes the solution template to a solution file"""
    if not os.path.exists(path):
        write_template(path, read_solution_template(year, day))
        console.print(f"[green]Wrote template to {path}")
    else:
        console.print(
            f"[yellow]Did not write template for year {year} day {day}"
            ", the file already exists."
        )


def write_test_template(path: str, year: int, day: int) -> None:
    """Writes the test template to a test file"""
    if not os.path.exists(path):
        write_template(path, read_test_template(year, day))
        console.print(f"[green]Wrote test template to {path}")
    else:
        console.print(
            f"[yellow]Did not write test template for year {year} day {day}"
            ", the file already exists."
        )


def create_module_dir(path: str) -> None:
    """Creates a __init__ file if it does not exist in the provided path"""
    create_dir(path)

    if not os.path.exists(init_file := os.path.join(path, "__init__.py")):
        with open(init_file, "a+"):
            pass


def create_dir(path: str) -> None:
    """Creates a directory if it doesn't exist"""
    if not os.path.exists(path):
        os.mkdir(path)


def verify_input_exists(year: int, day: int) -> None:
    """Verifies if user input exists, and downloads it if not"""
    try:
        _ = get_input_for_day(year, day)
        console.print(
            f"Input data already exists for year {year} day {day}, skipping download"
        )
        return
    except FileNotFoundError:
        try:
            get_input(year, day)
            console.print(
                f"Automatically downloaded input data for year {year} day {day}"
            )
            return
        except HTTPError as e:
            console.print(
                "[red]Could not retrieve input data for "
                f"year {year} day {day} automatically: {e}"
            )
            return
        except FileNotFoundError:
            console.print(
                "[red]Could not retrieve input data for "
                f"year {year} day {day}: .session not set correctly"
            )
            return


def _read_solution_template(template_path: str, year: str, day: str) -> str:
    """Reads solution template and fills the year and day"""
    with open(template_path) as f:
        template = f.read()

    template = template.replace("{year}", year)
    template = template.replace("{day}", day)

    return template


def _read_test_template(template_path: str, year: str, day: str, file_day: str) -> str:
    """Reads test template and fills year, day and file location"""
    with open(template_path) as f:
        template = f.read()

    template = template.replace("{year}", year)
    template = template.replace("{day}", day)
    template = template.replace("{file_day}", file_day)

    return template


def read_solution_template(year: int, day: int) -> str:
    """Read and fill solution template"""
    template_path = os.path.join(ROOT_DIR, "scripts/templates/day_template.txt")
    return _read_solution_template(template_path, str(year), str(day))


def read_test_template(year: int, day: int) -> str:
    """Read and fill test template"""
    template_path = os.path.join(ROOT_DIR, "scripts/templates/test_template.txt")
    return _read_test_template(template_path, str(year), str(day), f"{day:02}")


def write_template(filename: str, template: str):
    """Write template to file"""
    with open(filename, "w") as f:
        f.write(template)


def _parse_args(args: list[str]) -> tuple[int, int]:
    """Parse cli args"""
    parser = ArgumentParser(description="Add a day")
    parser.add_argument("year", type=int, help="The year of the exercise")
    parser.add_argument("day", type=int, help="The day of the exercise")
    parsed = parser.parse_args(args)
    return parsed.year, parsed.day


if __name__ == "__main__":
    add_day()
