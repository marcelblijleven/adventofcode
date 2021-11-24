from typing import List, Dict

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

mfcsam = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


class Aunt:
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.kwargs = kwargs

    @property
    def number(self):
        return int(self.name.split('Sue ')[1])


def parse_lines(input_data: List[str]) -> List[Aunt]:
    aunts: List[Aunt] = []

    for line in input_data:
        name, property_content = line.split(': ', 1)
        properties: Dict[str, int] = {}

        for prop in property_content.split(', '):
            key, value = prop.split(': ')
            properties[key] = int(value)

        aunts.append(Aunt(name, **properties))

    return aunts


def find_aunt_sue(aunts: List[Aunt]) -> Aunt:
    for aunt in aunts:
        if all_properties_match(aunt):
            return aunt


def find_aunt_sue_part_two(aunts: List[Aunt]) -> Aunt:
    aunts = [aunt for aunt in aunts if matches_part_two(aunt)]

    if len(aunts) != 1:
        raise ValueError('could not locate Aunt Sue')

    return aunts[0]


def all_properties_match(aunt: Aunt) -> bool:
    for key, value in aunt.kwargs.items():
        if mfcsam[key] != value:
            return False

    return True


def matches_part_two(aunt: Aunt) -> bool:
    for key, value in aunt.kwargs.items():
        if key in ['cats', 'trees']:
            if mfcsam[key] >= value:
                return False
        elif key in ['pomeranians', 'goldfish']:
            if mfcsam[key] <= value:
                return False
        else:
            if mfcsam[key] != value:
                return False
    return True


@solution_timer(2015, 16, 1)
def part_one(input_data: List[str]):
    aunts = parse_lines(input_data)
    answer = find_aunt_sue(aunts).number

    if not answer:
        raise SolutionNotFoundException(2015, 16, 1)

    return answer


@solution_timer(2015, 16, 2)
def part_two(input_data: List[str]):
    aunts = parse_lines(input_data)
    answer = find_aunt_sue_part_two(aunts).number

    if not answer:
        raise SolutionNotFoundException(2015, 16, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2015, 16)
    part_one(data)
    part_two(data)
