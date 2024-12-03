import re
from itertools import combinations, permutations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

PATTERN = re.compile(r"^(\w+)[\w\s]+(gain|lose)\s(\d+)[\w\s]+\s(\w+)\.$")

HappinessChartType = dict[tuple[str, str], int]


def parse_line(line: str, chart: HappinessChartType) -> None:
    if (matched := PATTERN.match(line)) and matched is not None:
        person_a, would, number_str, person_b = matched.groups()

        number = int(number_str) if would == "gain" else int(number_str) * -1
        pair = (person_a, person_b)
        chart[pair] = number
        return

    raise ValueError(f"could not parse line: {line}")


def get_happiness_chart(input_data: list[str]) -> HappinessChartType:
    chart: HappinessChartType = {}

    for line in input_data:
        parse_line(line, chart)

    return chart


def get_unique_persons(chart: HappinessChartType) -> list[str]:
    persons = set()

    for keys in chart.keys():
        persons.add(keys[0])

    return list(persons)


def get_all_combinations(persons: list[str]) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []

    for combination in combinations(persons, 2):
        results.append(combination)

    return results


def get_seating_happiness(persons: list[str], chart: HappinessChartType) -> int:
    permutations_list = permutations(persons, len(persons))

    max_happiness = 0

    for permutation in permutations_list:
        happiness = 0
        for idx, person in enumerate(permutation):
            if idx == len(permutation) - 1:
                # use last person with first person
                first_person = permutation[0]
                happiness += chart[(first_person, person)]
                happiness += chart[(person, first_person)]
            else:
                next_person = permutation[idx + 1]
                happiness += chart[person, next_person]
                happiness += chart[next_person, person]

        if happiness > max_happiness:
            max_happiness = happiness

    return max_happiness


def update_happiness_chart(
    chart: HappinessChartType, person: str
) -> HappinessChartType:
    persons = get_unique_persons(chart)
    persons.append(person)

    for combination in get_all_combinations(persons):
        if person in combination:
            for permutation in permutations(combination, 2):
                chart[permutation] = 0  # type: ignore

    return chart


@register_solution(2015, 13, 1)
def part_one(input_data: list[str]):
    chart = get_happiness_chart(input_data)
    persons = get_unique_persons(chart)

    answer = get_seating_happiness(persons, chart)

    if not answer:
        raise SolutionNotFoundError(2015, 13, 1)

    return answer


@register_solution(2015, 13, 2)
def part_two(input_data: list[str]):
    chart = get_happiness_chart(input_data)
    chart = update_happiness_chart(chart, "Marcel")
    persons = get_unique_persons(chart)

    answer = get_seating_happiness(persons, chart)

    if not answer:
        raise SolutionNotFoundError(2015, 13, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 13)
    part_one(data)
    part_two(data)
