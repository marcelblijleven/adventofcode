import re
from typing import List, Dict, Set

import math

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

Rules = Dict[str, List[int]]
Ticket = List[int]
rules_pattern = re.compile(r'^([a-z ]+): (?:(\d+)-(\d+)) or (?:(\d+)-(\d+))')


def parse_input(input_data: str) -> tuple[Rules, Ticket, List[Ticket]]:
    parsed = input_data.split('\n\n')
    rules = get_rules(parsed[0].split('\n'))
    ticket = get_ticket(parsed[1].split('\n')[1])
    tickets = get_tickets(parsed[2].split('\n')[1:])
    return rules, ticket, tickets


def get_rules(input_data: List[str]) -> Rules:
    rules: Rules = {}

    for line in input_data:
        match = rules_pattern.match(line)

        if match is None:
            raise ValueError(f'could not parse line "{line}"')

        matches = match.groups()
        rule = matches[0]
        lower_bound_a, upper_bound_a, lower_bound_b, upper_bound_b = map(int, matches[1:])
        rules[rule] = [lower_bound_a, upper_bound_a, lower_bound_b, upper_bound_b]

    return rules


def number_is_valid(number: int, rules: Rules) -> bool:
    for lower_a, upper_a, lower_b, upper_b in rules.values():
        if lower_a <= number <= upper_a or lower_b <= number <= upper_b:
            return True

    return False


def get_ticket(line: str) -> Ticket:
    return list(map(int, line.split(',')))


def get_tickets(lines: List[str]) -> List[Ticket]:
    return list(map(get_ticket, lines))


def evaluate_tickets(tickets: List[Ticket], rules: Rules) -> int:
    seen_invalid_numbers: List[int] = []

    for ticket in tickets:
        for number in ticket:
            if not number_is_valid(number, rules):
                seen_invalid_numbers.append(number)

    return sum(seen_invalid_numbers)


def find_rules_for_columns(columns: list[tuple[int, ...]], rules: Rules) -> dict[int, Set[str]]:
    rules_for_columns: dict[int, Set[str]] = {}

    for index, column in enumerate(columns):
        rules_for_columns[index] = set()

        for rule, bounds in rules.items():
            lower_a, upper_a, lower_b, upper_b = bounds
            if all([lower_a <= number <= upper_a or lower_b <= number <= upper_b for number in column]):
                rules_for_columns[index].add(rule)

    return rules_for_columns


def reduce_column_rules(column_rules: Dict[int, Set[str]], available_rules: Set[str]) -> Dict[str, int]:
    for column, rules in column_rules.items():
        if len(rules) == 1:
            try:
                available_rules.remove(list(rules)[0])
            except KeyError:
                pass
        else:
            column_rules[column] = rules.intersection(available_rules)

    if any([len(rules) > 1 for rules in column_rules.values()]):
        return reduce_column_rules(column_rules, available_rules)
    else:
        return {list(v)[0]: k for k, v in column_rules.items()}


def find_order(tickets: List[Ticket], rules: Rules) -> Dict[str, int]:
    columns = list(zip(*tickets))
    available_rules = {rule for rule in rules.keys()}
    column_rules: Dict[str, int] = reduce_column_rules(find_rules_for_columns(columns, rules), available_rules)
    return column_rules


def parse_own_ticket(ticket: Ticket, order: Dict[str, int], test: bool = False) -> int:
    departures: List[int] = []

    for rule, position in order.items():
        if not test:
            if rule.startswith('departure'):
                departures.append(ticket[position])
        else:
            departures.append(ticket[position])

    return math.prod(departures)


def get_departures(input_data: str, test: bool = False) -> int:
    rules, ticket, tickets = parse_input(input_data)
    filtered_tickets = filter_tickets(tickets, rules)
    order = find_order(filtered_tickets, rules)
    return parse_own_ticket(ticket, order, test)


def filter_tickets(tickets: List[Ticket], rules: Rules) -> List[Ticket]:
    valid_tickets: List[Ticket] = []

    for ticket in tickets:
        if all([number_is_valid(number, rules) for number in ticket]):
            valid_tickets.append(ticket)

    return valid_tickets


@solution_timer(2020, 16, 1)
def part_one(input_data: List[str]):
    input_as_string = '\n'.join(input_data)
    rules, ticket, tickets = parse_input(input_as_string)
    print(len(tickets))
    answer = evaluate_tickets(tickets, rules)

    if not answer:
        raise SolutionNotFoundException(2020, 16, 1)

    return answer


@solution_timer(2020, 16, 2)
def part_two(input_data: List[str]):
    input_as_string = '\n'.join(input_data)
    answer = get_departures(input_as_string)

    if not answer:
        raise SolutionNotFoundException(2020, 16, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2020, 16)
    part_one(data)
    part_two(data)
