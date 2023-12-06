import re

from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day


def find_locations(data: list[str]) -> None:
    """
    Parse input back to str, and split by \n\n to get the
    mappings easier
    """
    pattern = re.compile("\\d+")
    as_text = "\n".join(data)
    sections = [line.split("\n") for line in as_text.split("\n\n")]
    seeds = {x: x for x in map(int, pattern.findall(sections[0][0]))}

    for mapping in sections[1:]:
        for seed, value in seeds.items():
            for _range in mapping[1:]:
                dest, src, length = list(map(int, pattern.findall(_range)))
                if src <= value < (src + length):
                    seeds[seed] = dest + (value - src)

    return min(seeds.values())


@register_solution(2023, 5, 1)
def part_one(input_data: list[str]):
    answer = find_locations(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 5, 1)

    return answer


@register_solution(2023, 5, 2)
def part_two(input_data: list[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundError(2023, 5, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2023, 5)
    part_one(data)
    part_two(data)
