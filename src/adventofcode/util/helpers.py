import cProfile
import os
import pstats
import time
from collections.abc import Callable
from typing import Any, Literal

from adventofcode.config import RUNNING_ALL, RUNNING_BENCHMARKS
from adventofcode.util.console import console


def _get_year_from_segment(segment: str) -> int:
    if not segment.startswith("year_"):
        raise ValueError(f"invalid year segment received: {segment}")

    return int(segment[5:])


def get_year_from_file(file: str):
    """
    Pass __file__ as parameter to get the year the file is in.

    Should not be used outside of a year_* module
    """
    segments = os.path.dirname(os.path.realpath(file)).split(os.sep)
    year_segment = segments[-1]
    return _get_year_from_segment(year_segment)


def _get_prefix(year: int, day: int, part: int, version: str) -> str:
    if not day or not part:
        raise ValueError("incorrect values provided for solution timer")

    if version and version != "normal":
        version = f" [yellow]{version}[/yellow]"
    else:
        version = ""

    if RUNNING_ALL:
        prefix = f"[blue]  - day {day:02} part {part:02}[/blue]{version}: "
    else:
        prefix = f"[blue]{year} day {day:02} part {part:02}[/blue]{version}: "

    return prefix


def solution_timer(
    solution_input: Any, func: Callable, year: int, day: int, part: int, version: str
):  # type: ignore
    prefix = _get_prefix(year, day, part, version)
    try:
        start = time.perf_counter()
        solution = func(solution_input)
        diff = (time.perf_counter() - start) * 1000
    except (ValueError, ArithmeticError, TypeError):
        console.print_exception()
        return

    if solution is None:
        console.print(f"{prefix}[red]solution not found")
        return

    if not RUNNING_BENCHMARKS:
        console.print(f"{prefix}{solution} in {diff:.2f} ms")
        return solution

    return diff


def solution_profiler(
    year: int,
    day: int,
    part: int,
    version: str = "",
    stats_amount: int = 10,
    sort: Literal["time", "cumulative"] = "time",
):  # , type: ignore
    prefix = _get_prefix(year, day, part, version)

    def decorator(func: Callable):  # type: ignore
        def wrapper(*args, **kwargs):
            with cProfile.Profile() as profiler:
                solution = func(*args, **kwargs)

            stats = pstats.Stats(profiler)

            if sort == "time":
                stats.sort_stats(pstats.SortKey.TIME)
            elif sort == "cumulative":
                stats.sort_stats(pstats.SortKey.CUMULATIVE)
            else:
                raise ValueError('only "time" and "cumulative" are supported')

            stats.sort_stats(pstats.SortKey.TIME)
            console.print(f"{prefix} profiling")
            stats.print_stats(stats_amount)
            return solution

        return wrapper

    return decorator


def memoize(func: Callable):  # type: ignore
    cache: dict[Any, Any] = {}

    def memoized_func(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def manhattan_distance(start: tuple[int, int], end: tuple[int, int]):
    x1, y1 = start
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)


def grid_to_string(grid: dict[tuple[int, int], Any]) -> str:
    lines: list[str] = []
    max_x, max_y = max(grid.keys())

    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            line += str(grid[(x, y)])

        lines.append(line)

    return "\n".join(lines)
