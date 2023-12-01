from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


@register_solution(2015, 1, 1)
def part_one(input_data: list[str]) -> int:
    floor = 0

    for char in input_data[0]:
        if char == "(":
            floor += 1
        else:
            floor -= 1

    return floor


@register_solution(2015, 1, 2)
def part_two(input_data: list[str]) -> int:
    floor = 0

    for i, char in enumerate(input_data[0]):
        if char == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return i + 1

    raise SolutionNotFoundError(2015, 1, 2)


if __name__ == "__main__":
    data = get_input_for_day(2015, 1)
    part_one(data)
    part_two(data)
