from __future__ import annotations

import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

pattern = re.compile(r"(-?\d+)")

CuboidNumbers = tuple[int, int, int, int, int, int]
CubeDimensions = tuple[int, int, int]


def get_cuboid_from_line(line: str) -> tuple[bool, CuboidNumbers]:
    split = line.split(" ")
    state = split[0] == "on"
    (xa, xb, ya, yb, za, zb) = tuple(map(int, pattern.findall(split[1])))
    return state, (xa, xb, ya, yb, za, zb)


def get_cuboid(line: str, limit: bool = True) -> dict[CubeDimensions, bool]:
    state, coords = get_cuboid_from_line(line)
    cubes: dict[CubeDimensions, bool] = {}

    if limit and any([coord < -50 or coord > 50 for coord in coords]):  # noqa
        return cubes

    (xa, xb, ya, yb, za, zb) = coords

    for x in range(xa, xb + 1):
        for y in range(ya, yb + 1):
            for z in range(za, zb + 1):
                cubes[x, y, z] = state

    return cubes


def apply_reboot_line(
    line: str, cuboids: dict[CubeDimensions, bool], limit: bool = True
):
    cuboid = get_cuboid(line, limit)
    cuboids.update(cuboid)


def apply_reboot(input_data: list[str], limit: bool = True) -> int:
    cuboids: dict[CubeDimensions, bool] = {}

    for line in input_data:
        apply_reboot_line(line, cuboids, limit)

    return sum(cuboids.values())


class Cuboid:
    def __init__(self, numbers: CuboidNumbers, sign: int):
        (self.xa, self.xb, self.ya, self.yb, self.za, self.zb) = numbers
        self.sign = sign

    @property
    def volume(self) -> int:
        return (
            (self.xb - self.xa + 1) * (self.yb - self.ya + 1) * (self.zb - self.za + 1)
        )

    def intersects(self, other: Cuboid) -> bool:
        if (
            not (self.xa <= other.xb and self.xb >= other.xa)
            or not (self.ya <= other.yb and self.yb >= other.ya)
            or not (self.za <= other.zb and self.zb >= other.za)
        ):
            return False

        return True

    def intersection(self, other: Cuboid) -> Cuboid | None:
        if not self.intersects(other):
            return None

        xa = max(self.xa, other.xa)
        xb = min(self.xb, other.xb)
        ya = max(self.ya, other.ya)
        yb = min(self.yb, other.yb)
        za = max(self.za, other.za)
        zb = min(self.zb, other.zb)

        sign = -other.sign
        return Cuboid((xa, xb, ya, yb, za, zb), sign)


def apply_reboot_without_limit(input_data: list[str]):
    cuboids: list[Cuboid] = []

    for state, coords in [get_cuboid_from_line(line) for line in input_data]:
        sign = 1 if state else -1
        cuboid = Cuboid(coords, sign)

        for c in cuboids[:]:
            if (intersect := cuboid.intersection(c)) is not None:
                cuboids.append(intersect)

        if state:
            cuboids.append(cuboid)

    return sum(cuboid.sign * cuboid.volume for cuboid in cuboids)


@register_solution(2021, 22, 1)
def part_one(input_data: list[str]):
    answer = apply_reboot(input_data, limit=True)

    if not answer:
        raise SolutionNotFoundError(2021, 22, 1)

    return answer


@register_solution(2021, 22, 2)
def part_two(input_data: list[str]):
    answer = apply_reboot_without_limit(input_data)

    if not answer:
        raise SolutionNotFoundError(2021, 22, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 22)
    part_one(data)
    part_two(data)
