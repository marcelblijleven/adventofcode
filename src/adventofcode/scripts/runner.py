from adventofcode import config
from adventofcode.util.console import console
from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.util.module_helpers import get_full_year_paths, clean_year, get_full_day_paths, year_dir_from_path, \
    get_full_module_from_day_file, clean_day


def run_all() -> None:
    """
    Gathers all year_*.day_* files and executes the
    part_one and part_two functions in those files.

    If input file is not found, or a function is not found, it will be printed to console
    """
    config.RUNNING_ALL = True

    for year_path in get_full_year_paths():
        year_dir = year_dir_from_path(year_path)
        year = clean_year(year_dir)
        console.print(year)

        for day_file in get_full_day_paths(year_path):
            day = clean_day(day_file)
            module_name = get_full_module_from_day_file(day_file)
            module = __import__(module_name, fromlist=['object'])

            try:
                _run_day(module, year, day)
            except FileNotFoundError:
                console.print(f'[blue]{year} day {day:02}: [red]input file not found')

    config.RUNNING_ALL = False


def _run_day(module: str, year: int, day: int):
    """
    Runs all solutions in the given day
    """
    data = get_input_for_day(year, day)
    try:
        getattr(module, 'part_one')(data)
    except AttributeError:
        pass

    try:
        getattr(module, 'part_two')(data)
    except AttributeError:
        pass


if __name__ == '__main__':
    run_all()
