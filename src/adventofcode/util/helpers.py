import time
import os
from typing import Callable

from adventofcode.config import RUNNING_ALL
from adventofcode.util.console import console

from adventofcode.util.exceptions import SolutionNotFoundException


def _get_year_from_segment(segment: str) -> int:
    if not segment.startswith('year_'):
        raise ValueError(f'invalid year segment received: {segment}')

    return int(segment[5:])


def get_year_from_file(file: str):
    """
    Pass __file__ as parameter to get the year the file is in.

    Should not be used outside of a year_* module
    """
    segments = os.path.dirname(os.path.realpath(file)).split(os.sep)
    year_segment = segments[-1]
    return _get_year_from_segment(year_segment)


def solution_timer(year: int, day: int, part: int, version: str = ''):  # noqa: C901, type: ignore
    if not day or not part:
        raise ValueError('incorrect values provided for solution timer')

    if version:
        version = f' [yellow]{version}[/yellow]'

    if RUNNING_ALL:
        prefix = f'[blue]  - day {day:02} part {part:02}[/blue]{version}: '
    else:
        prefix = f'[blue]{year} day {day:02} part {part:02}[/blue]{version}: '

    def decorator(func: Callable):  # type: ignore
        def wrapper(*args, **kwargs):
            try:
                start = time.perf_counter()
                solution = func(*args, **kwargs)

                if not solution:
                    raise SolutionNotFoundException(year, day, part)

                diff = time.perf_counter() - start
                console.print(f'{prefix}{solution} in {diff:.4f} ms')
            except (ValueError, ArithmeticError, TypeError):
                console.print_exception()
            except SolutionNotFoundException:
                console.print(f'{prefix}[red]solution not found')
            else:
                return solution

        return wrapper
    return decorator
