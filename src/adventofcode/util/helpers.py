import time
import os
from typing import Callable

from rich.console import Console


console = Console(color_system='truecolor')


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


def solution_timer(day: int, part: int):  # type: ignore
    if not day or not part:
        raise ValueError('incorrect values provided for solution timer')

    prefix = f'[blue]day {day:02} part {part:02}[/blue]: '

    def decorator(func: Callable):  # type: ignore
        def wrapper(*args, **kwargs):
            try:
                start = time.perf_counter()
                solution = func(*args, **kwargs)
                diff = time.perf_counter() - start
                console.print(f'{prefix}{solution} in {diff:.4f} ms')
            except (ValueError, ArithmeticError, TypeError):
                console.print_exception()
            else:
                return solution

        return wrapper
    return decorator
