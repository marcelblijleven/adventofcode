from itertools import groupby


from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def iterate(value: str) -> str:
    groups = groupby(value, lambda x: x)
    new_value = ""

    for k, group in groups:
        new_value += f"{len(list(group))}{k}"

    return new_value


@register_solution(2015, 10, 1)
def part_one(input_data: list[str]):
    value = input_data[0]

    for i in range(0, 40):
        value = iterate(value)

    answer = len(value)

    if not answer:
        raise SolutionNotFoundException(2015, 10, 1)

    return answer


@register_solution(2015, 10, 2)
def part_two(input_data: list[str]):
    value = input_data[0]

    for i in range(0, 50):
        value = iterate(value)

    answer = len(value)

    if not answer:
        raise SolutionNotFoundException(2015, 10, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 10)
    part_one(data)
    part_two(data)
