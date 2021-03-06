import re
from itertools import permutations
from typing import List, Dict

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

PATTERN = re.compile(r'(\w+)')

DistDictType = Dict[tuple[str, str], int]


def get_all_cities(input_data: List[str], dist_dict: DistDictType) -> List[str]:
    cities = set()

    for line in input_data:
        groups = PATTERN.findall(line)
        start = groups[0]
        destination = groups[2]
        distance = int(groups[3])

        dist_dict[(start, destination)] = distance
        cities.add(start)
        cities.add(destination)

    return list(cities)


def get_all_routes(cities: List[str]) -> list[tuple[str, ...]]:
    routes = []

    for route in permutations(cities, len(cities)):
        routes.append(route)

    return routes


def _get_route_distances(routes: List[tuple[str, ...]], dist_dict: DistDictType) -> List[int]:
    distances = []
    for route in routes:
        distance = 0

        for i, city in enumerate(route):
            try:
                next_city = route[i + 1]
            except IndexError:
                break

            try:
                distance += dist_dict[(city, next_city)]
            except KeyError:
                distance += dist_dict[(next_city, city)]

        distances.append(distance)

    return distances


def get_fastest_route(routes: List[tuple[str, ...]], dist_dict: DistDictType) -> int:
    return min(_get_route_distances(routes, dist_dict))


def get_slowest_route(routes: List[tuple[str, ...]], dist_dict: DistDictType) -> int:
    return max(_get_route_distances(routes, dist_dict))


@solution_timer(2015, 9, 1)
def part_one(input_data: List[str]):
    dist_dict: DistDictType = {}
    cities = get_all_cities(input_data, dist_dict)
    routes = get_all_routes(cities)

    answer = get_fastest_route(routes, dist_dict)

    if not answer:
        raise SolutionNotFoundException(2015, 9, 1)

    return answer


@solution_timer(2015, 9, 2)
def part_two(input_data: List[str]):
    dist_dict: DistDictType = {}
    cities = get_all_cities(input_data, dist_dict)
    routes = get_all_routes(cities)

    answer = get_slowest_route(routes, dist_dict)

    if not answer:
        raise SolutionNotFoundException(2015, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2015, 9)
    part_one(data)
    part_two(data)
