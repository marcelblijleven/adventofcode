import asyncio
import multiprocessing
from asyncio import Queue
from collections import defaultdict
from itertools import repeat
from typing import List, DefaultDict, Set

import math

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]
CaveFloor = DefaultDict[Position, int]


def _cave_floor_factory() -> int:
    return 10


def parse_input(input_data: List[str]) -> tuple[CaveFloor, int, int]:
    cave_floor = defaultdict(_cave_floor_factory)
    height = 0
    width = 0

    for y, line in enumerate(input_data):
        for x, number in enumerate(line):
            cave_floor[(x, y)] = int(number)
            width = max(x, width)
        height = max(y, height)

    return cave_floor, width, height


def get_low_points(cave_floor: CaveFloor, width: int, height: int) -> List[Position]:
    positions: List[Position] = []

    for y in range(height + 1):
        for x in range(width + 1):
            number = cave_floor[(x, y)]
            adjacent_values = [
                cave_floor[(x - 1, y)], cave_floor[(x + 1, y)], cave_floor[(x, y - 1)], cave_floor[(x, y + 1)]
            ]

            if all([number < value for value in adjacent_values]):
                positions.append((x, y))

    return positions


def calculate_basin(cave_floor: CaveFloor, position: Position, basin: Set[Position]) -> Set[Position]:
    x, y = position
    left, right, top, down = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    if cave_floor[left] < 9 and left not in basin:
        basin.add(left)
        basin = calculate_basin(cave_floor, left, basin)

    if cave_floor[right] < 9 and right not in basin:
        basin.add(right)
        basin = calculate_basin(cave_floor, right, basin)

    if cave_floor[top] < 9 and top not in basin:
        basin.add(top)
        basin = calculate_basin(cave_floor, top, basin)

    if cave_floor[down] < 9 and down not in basin:
        basin.add(down)
        basin = calculate_basin(cave_floor, down, basin)

    return basin


def find_basin_size_product(cave_floor: CaveFloor, width: int, height: int) -> int:
    low_points = get_low_points(cave_floor, width, height)
    basin_sizes: List[int] = []

    for point in low_points:
        basin: Set[Position] = set()
        basin.add(point)
        basin = calculate_basin(cave_floor, point, basin)
        basin_sizes.append(len(basin))

    basin_sizes.sort()
    return math.prod(basin_sizes[-3:])


async def calculate_basin_async(cave_floor: CaveFloor, position: Position) -> list[tuple[int, int]]:
    basin: Set[Position] = set()
    basin = calculate_basin(cave_floor, position, basin)
    return list(basin)


async def find_basin_size_product_async(cave_floor: CaveFloor, width: int, height: int) -> int:
    low_points = get_low_points(cave_floor, width, height)
    position_queue: Queue[Position] = asyncio.Queue()
    tasks = []

    for position in low_points:
        await position_queue.put(position)
        tasks.append(asyncio.create_task(calculate_basin_async(cave_floor, position)))

    result = await asyncio.gather(*tasks)
    lengths = sorted([len(res) for res in result])
    return math.prod(lengths[-3:])


def calculate_basin_mp(cave_floor: CaveFloor, position: Position) -> list[tuple[int, int]]:
    basin: Set[Position] = set()
    basin = calculate_basin(cave_floor, position, basin)
    return list(basin)


def find_basin_size_product_mp(cave_floor: CaveFloor, width: int, height: int) -> int:
    low_points = get_low_points(cave_floor, width, height)
    args = zip(repeat(cave_floor), low_points)

    with multiprocessing.Pool(processes=2) as pool:
        results = pool.starmap(calculate_basin_mp, args)

    lengths = sorted([len(res) for res in results])
    return math.prod(lengths[-3:])


def get_risk_level(cave_floor: CaveFloor, width: int, height: int) -> int:
    points: List[int] = []

    for y in range(height + 1):
        for x in range(width + 1):
            number = cave_floor[(x, y)]
            adjacent_values = [
                cave_floor[(x - 1, y)], cave_floor[(x + 1, y)], cave_floor[(x, y - 1)], cave_floor[(x, y + 1)]
            ]

            if all([number < value for value in adjacent_values]):
                points.append(number + 1)

    return sum(points)


@solution_timer(2021, 9, 1)
def part_one(input_data: List[str]):
    answer = get_risk_level(*parse_input(input_data))

    if not answer:
        raise SolutionNotFoundException(2021, 9, 1)

    return answer


@solution_timer(2021, 9, 2)
def part_two(input_data: List[str]):
    answer = find_basin_size_product(*parse_input(input_data))

    if not answer:
        raise SolutionNotFoundException(2021, 9, 2)

    return answer


@solution_timer(2021, 9, 2, version='async')
def part_two_async(input_data: List[str]):
    answer = asyncio.run(find_basin_size_product_async(*parse_input(input_data)))

    if not answer:
        raise SolutionNotFoundException(2021, 9, 2)

    return answer


@solution_timer(2021, 9, 2, version='multiprocessing')
def part_two_mp(input_data: List[str]):
    answer = find_basin_size_product_mp(*parse_input(input_data))

    if not answer:
        raise SolutionNotFoundException(2021, 9, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 9)
    part_one(data)
    part_two(data)
    part_two_async(data)
    part_two_mp(data)
