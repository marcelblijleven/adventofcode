from adventofcode import config
from adventofcode.registry import autodetect, registry
from adventofcode.registry.util import get_info_from_registry_key
from adventofcode.util.input_helpers import get_input_for_day


def run_all() -> None:
    """
    Gathers all year_*.day_* files and executes the
    part_one and part_two functions in those files.

    If input file is not found, or a function is not found, it will be printed to console
    """
    config.RUNNING_ALL = True
    autodetect()

    for key, solution in registry.items():
        year, day, part, version = get_info_from_registry_key(key)
        data = get_input_for_day(year, day)

        solution(data)

    config.RUNNING_ALL = False


def _run_day(module, year: int, day: int):
    """
    Runs all solutions in the given day
    """
    data = get_input_for_day(year, day)
    try:
        module.part_one(data)
    except AttributeError:
        pass

    try:
        module.part_two(data)
    except AttributeError:
        pass


if __name__ == "__main__":
    run_all()
