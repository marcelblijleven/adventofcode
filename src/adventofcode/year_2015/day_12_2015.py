import json
import re
from typing import Any

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

PATTERN = re.compile(r"(-?\d+)")


def count_all_numbers(input_data: str) -> int:
    found = PATTERN.findall(input_data)
    numbers = [int(num) for num in found]
    return sum(numbers)


def get_json(input_data: str) -> Any:
    json_data = json.loads(input_data)
    return json_data


def traverser(input_data: Any):
    def recursive_sum(json_data: Any):
        if isinstance(json_data, int):
            return json_data
        elif isinstance(json_data, dict):
            if "red" in json_data.values():
                return 0
            return sum(map(recursive_sum, json_data.values()))
        elif isinstance(json_data, list):
            return sum(map(recursive_sum, json_data))

        return 0

    return recursive_sum(input_data)


@register_solution(2015, 12, 1)
def part_one(input_data: list[str]):
    answer = count_all_numbers(input_data[0])

    if not answer:
        raise SolutionNotFoundError(2015, 12, 1)

    return answer


@register_solution(2015, 12, 2)
def part_two(input_data: list[str]):
    answer = traverser(get_json(input_data[0]))

    if not answer:
        raise SolutionNotFoundError(2015, 12, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 12)
    part_one(data)
    part_two(data)
