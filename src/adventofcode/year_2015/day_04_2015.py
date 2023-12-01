import hashlib

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def find_number(secret: str, target: str, range_size: int) -> int:
    for i in range(range_size):
        h = hashlib.md5((secret + str(i)).encode("utf-8")).hexdigest()  # noqa: S324
        if h[: len(target)] == target:
            return i

    raise ValueError("number not found")


@register_solution(2015, 4, 1)
def part_one(input_data: list[str]) -> int:
    secret = input_data[0]
    number = find_number(secret, "00000", 1000000)

    if not number:
        raise SolutionNotFoundError(2015, 4, 1)

    return number


@register_solution(2015, 4, 2)
def part_two(input_data: list[str]) -> int:
    secret = input_data[0]
    number = find_number(secret, "000000", 10000000)

    if not number:
        raise SolutionNotFoundError(2015, 4, 1)

    return number


if __name__ == "__main__":
    data = get_input_for_day(2015, 4)
    part_one(data)
    part_two(data)
