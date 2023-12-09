import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

pattern = re.compile("\\d+")


def parse_inputs(data: list[str]) -> list[list[str]]:
    as_text = "\n".join(data)
    return [line.split("\n") for line in as_text.split("\n\n")]


def find_locations(data: list[str]) -> int:
    """
    Parse input back to str, and split by \n\n to get the
    mappings easier
    """
    sections = parse_inputs(data)
    seeds = {x: x for x in map(int, pattern.findall(sections[0][0]))}

    for mapping in sections[1:]:
        for seed, value in seeds.items():
            for _range in mapping[1:]:
                dest, src, length = list(map(int, pattern.findall(_range)))
                if src <= value < (src + length):
                    seeds[seed] = dest + (value - src)

    return min(seeds.values())


def find_locations_part_two(data: list[str]) -> int:
    sections = parse_inputs(data)
    seeds = list(map(int, pattern.findall(sections[0][0])))
    seed_pairs: list[list[int]] = []

    for idx in range(0, len(seeds), 2):
        seed_pairs.append([seeds[idx], seeds[idx] + seeds[idx + 1] - 1])

    for mapping in sections[1:]:
        for idx, pair in enumerate(seed_pairs):
            start, end = pair
            for _range in mapping[1:]:
                dest, src, length = list(map(int, pattern.findall(_range)))

                if src <= start < (src + length):
                    seed_pairs[idx][0] = dest + (start - src)
                    if end < src + length:
                        seed_pairs[idx][1] = dest + (end - src)
                    else:
                        seed_pairs[idx][1] = dest + length - 1
                        seed_pairs.append([src + length, end])
                elif src <= end < (src + length):
                    seed_pairs[idx][1] = dest + (end - src)
                    if start > src:
                        seed_pairs[idx][0] = dest + (start - src)
                    else:
                        seed_pairs[idx][0] = dest
                        seed_pairs.append([start, src - 1])

    return min(min(seed_pairs))


@register_solution(2023, 5, 1)
def part_one(input_data: list[str]):
    answer = find_locations(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 5, 1)

    return answer


@register_solution(2023, 5, 2)
def part_two(input_data: list[str]):
    answer = find_locations_part_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 5, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 5)
    part_one(data)
    part_two(data)
