from __future__ import annotations

import dataclasses
from collections import Counter
from itertools import combinations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


@dataclasses.dataclass()
class AxisOffset:
    axis: int  # 0, 1, 2
    sign: int  # -1, 1
    offset: int


Coordinates = tuple[int, int, int]
Edges = dict[int, AxisOffset]


def calculate_max_distance(scanners: list[Scanner]) -> int:
    max_distance = 0

    for scanner_a, scanner_b in combinations(scanners, 2):
        if scanner_a.position is None or scanner_b.position is None:
            raise ValueError("scanner position cannot be None")

        xa, ya, za = scanner_a.position
        xb, yb, zb = scanner_b.position
        distance = abs(xa - xb) + abs(ya - yb) + abs(za - zb)
        max_distance = max(distance, max_distance)

    return max_distance


def get_offset(number: int, edges: tuple[Edges, Edges, Edges]) -> Coordinates:
    return edges[0][number].offset, edges[1][number].offset, edges[2][number].offset


def apply_offset(
    coord: Coordinates,
    axis_offsets: tuple[AxisOffset, AxisOffset, AxisOffset],
    offset: Coordinates,
) -> Coordinates:
    x = offset[0] + axis_offsets[0].sign * coord[axis_offsets[0].axis]
    y = offset[1] + axis_offsets[1].sign * coord[axis_offsets[1].axis]
    z = offset[2] + axis_offsets[2].sign * coord[axis_offsets[2].axis]
    return x, y, z


class Scanner:
    def __init__(self, number: int, beacons: list[Coordinates]):
        self.number = number
        self.beacons = beacons
        self.position = (0, 0, 0) if number == 0 else None

    @classmethod
    def from_input(cls, input_data: list[str]) -> Scanner:
        number = int(input_data[0].lstrip("--- scanner ").rstrip(" ---"))  # noqa
        beacons: list[Coordinates] = []

        for beacon in input_data[1:]:
            x, y, z = tuple(map(int, beacon.split(",")))
            beacons.append((x, y, z))

        return cls(number, beacons)

    def _edges_x(self, scanner_map: ScannerMap) -> Edges:
        edges_x: Edges = {}

        for scanner in scanner_map.values():
            for axis in range(3):  # 0, 1, 2
                for sign in (-1, 1):
                    counter: Counter[int] = Counter()

                    for beacon in self.beacons:
                        for beacon_b in scanner.beacons:
                            counter[beacon[0] - beacon_b[axis] * sign] += 1

                    offset, count = counter.most_common(1)[0]
                    if count >= 12:
                        edges_x[scanner.number] = AxisOffset(axis, sign, offset)

        return edges_x

    def _edges_yz(self, edges_x: Edges, scanner_map: ScannerMap) -> tuple[Edges, Edges]:
        edges_y: Edges = {}
        edges_z: Edges = {}

        for number in edges_x:
            scanner = scanner_map[number]
            for axis in range(3):  # 0, 1, 2
                for sign in (-1, 1):
                    counter_y: Counter[int] = Counter()
                    counter_z: Counter[int] = Counter()

                    for beacon in self.beacons:
                        for beacon_b in scanner.beacons:
                            counter_y[beacon[1] - beacon_b[axis] * sign] += 1
                            counter_z[beacon[2] - beacon_b[axis] * sign] += 1

                    offset_y, count_y = counter_y.most_common(1)[0]
                    offset_z, count_z = counter_z.most_common(1)[0]

                    if count_y >= 12:
                        edges_y[number] = AxisOffset(axis, sign, offset_y)

                    if count_z >= 12:
                        edges_z[number] = AxisOffset(axis, sign, offset_z)

        return edges_y, edges_z

    def apply_offset(
        self,
        axis_offsets: tuple[AxisOffset, AxisOffset, AxisOffset],
        offset: Coordinates,
    ) -> list[Coordinates]:
        offset_beacons: list[Coordinates] = []

        for beacon in self.beacons:
            offset_beacons.append(apply_offset(beacon, axis_offsets, offset))

        self.beacons = offset_beacons
        return self.beacons

    def edges(self, scanner_map: ScannerMap) -> tuple[Edges, Edges, Edges]:
        edges_x = self._edges_x(scanner_map)
        edges_y, edges_z = self._edges_yz(edges_x, scanner_map)
        return edges_x, edges_y, edges_z


ScannerMap = dict[int, Scanner]


def get_scanners(input_data: list[str]) -> list[Scanner]:
    input_str = "\n".join(input_data)
    scanner_blocks = input_str.split("\n\n")
    scanners: list[Scanner] = []

    for block in scanner_blocks:
        scanners.append(Scanner.from_input(block.split("\n")))

    return scanners


def process_scanners(scanners: list[Scanner]) -> None:
    scanner_map: ScannerMap = {scanner.number: scanner for scanner in scanners}
    unprocessed_with_known_position: list[Scanner] = [scanner_map.pop(0)]

    while unprocessed_with_known_position:
        known_scanner = unprocessed_with_known_position.pop(0)

        edges = known_scanner.edges(scanner_map)
        edges_x, edges_y, edges_z = edges

        for number in edges_x:
            offset = get_offset(number, edges)
            process_scanner = scanner_map.pop(number)
            process_scanner.position = offset
            process_scanner.apply_offset(
                (edges_x[number], edges_y[number], edges_z[number]),
                offset,
            )

            unprocessed_with_known_position.append(process_scanner)


def count_unique_beacons(scanners: list[Scanner]) -> int:
    beacons: set[Coordinates] = set()
    for scanner in scanners:
        beacons.update(scanner.beacons)

    return len(beacons)


@register_solution(2021, 19, 1)
def part_one(input_data: list[str]):
    scanners = get_scanners(input_data)
    process_scanners(scanners)
    answer = count_unique_beacons(scanners)

    if not answer:
        raise SolutionNotFoundError(2021, 19, 1)

    return answer


@register_solution(2021, 19, 2)
def part_two(input_data: list[str]):
    scanners = get_scanners(input_data)
    process_scanners(scanners)
    answer = calculate_max_distance(scanners)

    if not answer:
        raise SolutionNotFoundError(2021, 19, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 19)
    part_one(data)
    part_two(data)
