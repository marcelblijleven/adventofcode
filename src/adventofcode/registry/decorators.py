from functools import partial, wraps

from adventofcode.registry import registry
from adventofcode.registry.util import get_registry_key
from adventofcode.util.helpers import solution_timer


def register_solution(year: int, day: int, part: int, version: str = "normal"):
    """Register a solution to the solution registry"""

    def decorator(func):
        partial_func = partial(  # type: ignore
            solution_timer, func=func, year=year, day=day, part=part, version=version
        )
        registry[get_registry_key(year, day, part, version)] = partial_func

        @wraps(func)
        def wrapper(*args, **kwargs):
            return partial_func(*args, **kwargs)

        return wrapper

    return decorator
