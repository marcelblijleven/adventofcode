import math
from itertools import combinations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def get_quantum_entanglement(packages: list[int]) -> int:
    return math.prod(packages)


def move_packages_into_groups(all_packages: list[int], number_of_groups: int) -> int:
    size = sum(all_packages) // number_of_groups

    for package_idx in range(len(all_packages)):
        entanglements = [
            get_quantum_entanglement(list(packages))
            for packages in combinations(all_packages, package_idx)
            if sum(packages) == size
        ]

        if len(entanglements):
            return min(entanglements)

    raise ValueError("could not find correct quantum entanglement")


@register_solution(2015, 24, 1)
def part_one(input_data: list[str]):
    packages = list(map(int, input_data))
    answer = move_packages_into_groups(packages, 3)

    if not answer:
        raise SolutionNotFoundError(2015, 24, 1)

    return answer


@register_solution(2015, 24, 2)
def part_two(input_data: list[str]):
    packages = list(map(int, input_data))
    answer = move_packages_into_groups(packages, 4)

    if not answer:
        raise SolutionNotFoundError(2015, 24, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 24)
    part_one(data)
    part_two(data)
