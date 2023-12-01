import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

bag_type_pattern = re.compile(r"^([a-z]+ [a-z]+)")
contents_pattern = re.compile(r"((\d) ([a-z]+ [a-z]+))")
gold_bag = "shiny gold"

BagType = dict[str, dict[str, int]]


@register_solution(2020, 7, 1)
def part_one(input_data: list[str]) -> int:
    bags = get_bags(input_data)
    gold_holders = []
    for bag in bags:
        if search(bags, bag, gold_bag):
            gold_holders.append(bag)

    if not gold_holders:
        raise SolutionNotFoundError(2020, 7, 1)

    return len(gold_holders)


@register_solution(2020, 7, 2)
def part_two(input_data: list[str]) -> int:
    bags = get_bags(input_data)

    answer = bag_counter(gold_bag, bags, 1, 0)

    if not answer:
        raise SolutionNotFoundError(2020, 7, 2)

    return answer


def get_bags(input_data: list[str]) -> BagType:
    bags: BagType = {}

    for line in input_data:
        bag = bag_type_pattern.match(line).group()  # type: ignore
        contents = contents_pattern.findall(line)
        bags[bag] = {}

        for content in contents:
            _, number_str, _bag = content
            bags[bag][_bag] = int(number_str)

    return bags


def search(bags: BagType, current_bag: str, bag: str) -> bool:
    contents = list(bags[current_bag].keys())
    if contents:
        for content in contents:
            if content == bag:
                return True
            elif search(bags, content, bag):
                return True

    return False


def bag_counter(bag: str, bags: BagType, multiplier: int, total: int) -> int:
    contents = bags[bag]
    total += sum([multiplier * value for _, value in contents.items()])

    for k, v in contents.items():
        total = bag_counter(k, bags, v * multiplier, total)

    return total


if __name__ == "__main__":
    data = get_input_for_day(2020, 7)
    part_one(data)
    part_two(data)
