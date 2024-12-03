import re
from itertools import permutations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

PATTERN = re.compile(r"(\w+)")

DistDictType = dict[tuple[str, str], int]


def get_all_cities(input_data: list[str], dist_dict: DistDictType) -> list[str]:
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


def get_all_routes(cities: list[str]) -> list[tuple[str, ...]]:
    routes = []

    for route in permutations(cities, len(cities)):
        routes.append(route)

    return routes


def _get_route_distances(
    routes: list[tuple[str, ...]], dist_dict: DistDictType
) -> list[int]:
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


def get_fastest_route(routes: list[tuple[str, ...]], dist_dict: DistDictType) -> int:
    return min(_get_route_distances(routes, dist_dict))


def get_slowest_route(routes: list[tuple[str, ...]], dist_dict: DistDictType) -> int:
    return max(_get_route_distances(routes, dist_dict))


@register_solution(2015, 9, 1)
def part_one(input_data: list[str]):
    dist_dict: DistDictType = {}
    cities = get_all_cities(input_data, dist_dict)
    routes = get_all_routes(cities)

    answer = get_fastest_route(routes, dist_dict)

    if not answer:
        raise SolutionNotFoundError(2015, 9, 1)

    return answer


@register_solution(2015, 9, 2)
def part_two(input_data: list[str]):
    dist_dict: DistDictType = {}
    cities = get_all_cities(input_data, dist_dict)
    routes = get_all_routes(cities)

    answer = get_slowest_route(routes, dist_dict)

    if not answer:
        raise SolutionNotFoundError(2015, 9, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 9)
    part_one(data)
    part_two(data)
