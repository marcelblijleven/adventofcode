import math
import re
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


pattern = re.compile(r'(\d+)x(\d+)x(\d+)')


class Box:
    def __init__(self, width: int, height: int, length: int):
        self.width = width
        self.height = height
        self.length = length

    @property
    def surface(self) -> int:
        surface_area = (
            2 * self.length * self.width +
            2 * self.width * self.height +
            2 * self.height * self.length
        )

        extra = [
            self.length * self.width,
            self.width * self.height,
            self.height * self.length,
        ]

        return surface_area + min(extra)


def parse_line(line: str) -> Box:
    match = pattern.match(line)

    if not match:
        raise ValueError('could not parse line')

    groups = match.groups()
    return Box(int(groups[0]), int(groups[1]), int(groups[2]))


def get_surface(line: str) -> int:
    box = parse_line(line)
    return box.surface


def calculate_ribbon(box: Box) -> int:
    dimensions = sorted([box.width, box.height, box.length])
    ribbon = sum([dimensions[0] * 2, dimensions[1] * 2])
    bow = math.prod(dimensions)
    return ribbon + bow


def get_ribbon(line: str) -> int:
    box = parse_line(line)
    return calculate_ribbon(box)


@solution_timer(2015, 2, 1)
def part_one(input_data: List[str]):
    answer = map(get_surface, input_data)

    if not answer:
        raise SolutionNotFoundException(2015, 2, 1)

    return sum(answer)


@solution_timer(2015, 2, 2)
def part_two(input_data: List[str]):
    answer = map(get_ribbon, input_data)

    if not answer:
        raise SolutionNotFoundException(2015, 2, 2)

    return sum(answer)


if __name__ == '__main__':
    data = get_input_for_day(2015, 2)
    part_one(data)
    part_two(data)
