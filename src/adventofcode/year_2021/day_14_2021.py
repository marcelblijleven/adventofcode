import itertools
from collections import Counter, defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

Rules = dict[str, str]


def parse_input(input_data: list[str]) -> tuple[str, Rules]:
    template = input_data[0]
    rules: Rules = {}

    for rule in input_data[2:]:
        a, b = rule.split(" -> ")
        rules[a] = b

    return template, rules


def process(template: str, rules: Rules) -> str:
    new_template = ""

    for pair in itertools.pairwise(template):
        key = "".join(pair)
        new_template += f"{pair[0]}{rules[key]}"

    return new_template + template[-1]


def get_answer_slow(input_data: list[str], steps: int) -> int:
    """
    The iteration in process(template, rules) causes the program to run out of memory on large steps
    Use get_answer instead
    """
    template, rules = parse_input(input_data)

    for _ in range(steps):
        template = process(template, rules)

    counter = Counter(template)
    most_common = counter.most_common()
    most = most_common[0][1]
    least = most_common[-1][1]

    return most - least


def pair_counter_in_template(template: str) -> defaultdict[str, int]:
    pair_counter: defaultdict[str, int] = defaultdict(int)

    for pair in itertools.pairwise(template):
        pair_counter["".join(pair)] += 1

    return pair_counter


def get_new_pairs(pair: str, target: str):
    a: str = pair[0]
    b: str = pair[1]
    return a + target, target + b


def get_answer(input_data: list[str], steps: int) -> int:
    """
    Get answer uses hash tables (dicts) instead of iterations, which are a lot faster O(1) compared to O(n).
    It creates a new dict after each step with the updated count and fills a Counter to keep track of the occurrences of
    each letter
    """
    template, rules = parse_input(input_data)
    counter = Counter(template)
    pairs = pair_counter_in_template(template)

    for _ in range(steps):
        pair_counter_in_step: defaultdict[str, int] = defaultdict(int)

        for pair, count in pairs.items():
            if pair in pairs and count > 0:
                target = rules[pair]
                new_pair_a, new_pair_b = get_new_pairs(pair, target)
                pair_counter_in_step[new_pair_a] += count
                pair_counter_in_step[new_pair_b] += count
                counter[target] += count

        pairs = pair_counter_in_step

    most_common = counter.most_common()
    return most_common[0][1] - most_common[-1][1]


@register_solution(2021, 14, 1)
def part_one(input_data: list[str]):
    answer = get_answer(input_data, 10)

    if not answer:
        raise SolutionNotFoundError(2021, 14, 1)

    return answer


@register_solution(2021, 14, 2)
def part_two(input_data: list[str]):
    answer = get_answer(input_data, 40)

    if not answer:
        raise SolutionNotFoundError(2021, 14, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 14)
    part_one(data)
    part_two(data)
