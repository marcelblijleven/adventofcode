from collections import defaultdict
from typing import List, Set, DefaultDict

from adventofcode.util.console import console
from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

PathDict = DefaultDict[str, list[str]]


def is_big_cave(cave: str) -> bool:
    return cave.upper() == cave


def is_small_cave(cave: str) -> bool:
    return cave.lower() == cave


def default_dict_factory() -> List[str]:
    return []


def get_paths(input_data: List[str]) -> PathDict:
    path_dict: PathDict = defaultdict(default_dict_factory)

    for line in input_data:
        a, b = line.split('-')
        path_dict[a].append(b)
        path_dict[b].append(a)

    return path_dict


class CaveExplorer3000:
    def __init__(self, paths: PathDict, limit_small_caves: bool = False) -> None:
        self.paths = paths
        self.limit_small_caves = limit_small_caves
        self.path_count = 0

    def traverse(self, cave: str, visited: Set[str]) -> int:
        if cave == 'end':
            return 1
        elif cave == 'start' and cave in visited:
            return 0

        if cave in visited and is_small_cave(cave):
            return 0

        visited.add(cave)
        paths = self.paths[cave]
        return sum(self.traverse(path, visited.copy()) for path in paths)

    def traverse_part_two(self, cave: str, visited: Set[str], revisit=True) -> int:
        if cave == 'end':
            return 1
        elif cave == 'start' and cave in visited:
            return 0

        if cave in visited and is_small_cave(cave):
            if not revisit:
                return 0

            revisit = False

        visited.add(cave)
        paths = self.paths[cave]
        return sum(self.traverse_part_two(path, visited.copy(), revisit) for path in paths)

    def traverse_with_print(self, cave: str, visited: Set[str], path_flow: str = '') -> int:
        if path_flow == '':
            path_flow = f'{cave}'
        else:
            path_flow += f' -> {cave}'

        if cave == 'end':
            console.print(path_flow)
            return 1
        elif cave == 'start' and cave in visited:
            return 0

        if cave in visited and is_small_cave(cave):
            return 0

        visited.add(cave)
        paths = self.paths[cave]
        return sum(self.traverse_with_print(path, visited.copy(), path_flow) for path in paths)


@solution_timer(2021, 12, 1)
def part_one(input_data: List[str]):
    path_dict = get_paths(input_data)
    cave_explorer = CaveExplorer3000(path_dict)
    answer = cave_explorer.traverse('start', set())

    if not answer:
        raise SolutionNotFoundException(2021, 12, 1)

    return answer


@solution_timer(2021, 12, 2)
def part_two(input_data: List[str]):
    path_dict = get_paths(input_data)
    cave_explorer = CaveExplorer3000(path_dict, limit_small_caves=True)
    answer = cave_explorer.traverse_part_two('start', set())

    if not answer:
        raise SolutionNotFoundException(2021, 12, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 12)
    part_one(data)
    part_two(data)
