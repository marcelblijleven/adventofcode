from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

mfcsam = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


class Aunt:
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.kwargs = kwargs

    @property
    def number(self):
        return int(self.name.split("Sue ")[1])


def parse_lines(input_data: list[str]) -> list[Aunt]:
    aunts: list[Aunt] = []

    for line in input_data:
        name, property_content = line.split(": ", 1)
        properties: dict[str, int] = {}

        for prop in property_content.split(", "):
            key, value = prop.split(": ")
            properties[key] = int(value)

        aunts.append(Aunt(name, **properties))

    return aunts


def find_aunt_sue(aunts: list[Aunt]) -> Aunt | None:
    for aunt in aunts:
        if all_properties_match(aunt):
            return aunt

    return None


def find_aunt_sue_part_two(aunts: list[Aunt]) -> Aunt:
    aunts = [aunt for aunt in aunts if matches_part_two(aunt)]

    if len(aunts) != 1:
        raise ValueError("could not locate Aunt Sue")

    return aunts[0]


def all_properties_match(aunt: Aunt) -> bool:
    for key, value in aunt.kwargs.items():
        if mfcsam[key] != value:
            return False

    return True


def matches_part_two(aunt: Aunt) -> bool:
    for key, value in aunt.kwargs.items():
        if key in ["cats", "trees"]:
            if mfcsam[key] >= value:
                return False
        elif key in ["pomeranians", "goldfish"]:
            if mfcsam[key] <= value:
                return False
        elif mfcsam[key] != value:
            return False
    return True


@register_solution(2015, 16, 1)
def part_one(input_data: list[str]):
    aunts = parse_lines(input_data)
    aunt = find_aunt_sue(aunts)

    if not aunt:
        raise SolutionNotFoundError(2015, 16, 1)

    answer = aunt.number

    if not answer:
        raise SolutionNotFoundError(2015, 16, 1)

    return answer


@register_solution(2015, 16, 2)
def part_two(input_data: list[str]):
    aunts = parse_lines(input_data)
    answer = find_aunt_sue_part_two(aunts).number

    if not answer:
        raise SolutionNotFoundError(2015, 16, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 16)
    part_one(data)
    part_two(data)
