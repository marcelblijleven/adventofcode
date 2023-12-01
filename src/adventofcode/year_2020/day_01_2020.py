from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2020, 1, 1)
def part_one(input_data: list[str]) -> int:
    numbers = map(int, input_data)
    seen = []

    for number in numbers:
        need = 2020 - number
        if need in seen:
            return need * number
        seen.append(number)

    raise SolutionNotFoundError(2020, 1, 1)


@register_solution(2020, 1, 2)
def part_two(input_data: list[str]) -> int:
    import math
    from itertools import combinations

    numbers = map(int, input_data)

    for c in combinations(numbers, 3):
        if sum(c) == 2020:
            return math.prod(c)

    raise SolutionNotFoundError(2020, 1, 2)


if __name__ == "__main__":
    data = get_input_for_day(2020, 1)
    part_one(data)
    part_two(data)
