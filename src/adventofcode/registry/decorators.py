from collections.abc import Callable
from functools import partial, wraps
from typing import ParamSpec, TypeAlias, TypeVar

from adventofcode.registry import registry
from adventofcode.registry.util import get_registry_key
from adventofcode.util.helpers import solution_timer

R = TypeVar("R")
P = ParamSpec("P")
SolutionFunc: TypeAlias = Callable[P, R]


def register_solution(
    year: int, day: int, part: int, version: str = "normal"
) -> Callable[[SolutionFunc], SolutionFunc]:
    """Register a solution to the solution registry"""

    def decorator(func: SolutionFunc) -> SolutionFunc:
        partial_func = partial(  # type: ignore
            solution_timer, func=func, year=year, day=day, part=part, version=version
        )
        registry[get_registry_key(year, day, part, version)] = partial_func

        @wraps(func)
        def wrapper(*args, **kwargs):
            return partial_func(*args, **kwargs)

        return wrapper

    return decorator
