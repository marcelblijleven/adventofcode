from __future__ import annotations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]


class Octopus:
    def __init__(self, energy: int, position: Position):
        self.energy = energy
        self.position = position
        self.adjacent_octopuses = self._adjacent_octopuses()
        self._has_flashed = False

    def __str__(self):
        return f"{self.energy}"

    def __repr__(self):
        return f"Octopus at ({self.position[0], self.position[1]}) with energy {self.energy}"

    @property
    def can_flash(self) -> bool:
        return self.energy > 9 and not self._has_flashed

    def reset_tick(self):
        self._has_flashed = False

    def respond_to_flash(self):
        if not self._has_flashed:
            self.energy += 1

    def _adjacent_octopuses(self) -> list[Position]:
        x, y = self.position
        octopuses = [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]

        return [
            octopus
            for octopus in octopuses
            if 0 <= octopus[0] <= 9 and 0 <= octopus[1] <= 9
        ]

    def flash(self, grid: dict[Position, Octopus]):
        self.energy = 0
        self._has_flashed = True

        for octopus in self.adjacent_octopuses:
            grid[octopus].respond_to_flash()

    def update_energy(self):
        if not self._has_flashed:
            self.energy += 1


Grid = dict[Position, Octopus]


def parse_input(input_data: list[str]) -> Grid:
    grid: Grid = {}

    for y, line in enumerate(input_data):
        for x, energy in enumerate(line):
            grid[(x, y)] = Octopus(int(energy), (x, y))

    return grid


def run_ticks(grid: OctopusGrid, iterations: int = 100):
    for _ in range(iterations):
        grid.tick()


def run_ticks_until_sync(grid: OctopusGrid) -> int:
    tick = 0

    while True:
        tick += 1

        if grid.tick():
            return tick


class OctopusGrid:
    def __init__(self, input_data: list[str]):
        self.grid = parse_input(input_data)
        self.can_flash: list[Octopus] = []
        self.flash_counter = 0
        self.total_octopuses = 100

    def _get_flashers_for_tick(self):
        for octopus in self.grid.values():
            octopus.reset_tick()
            octopus.update_energy()

            if octopus.can_flash:
                self.can_flash.append(octopus)

    def tick(self):
        initial_run = True
        flashed_during_tick = 0

        while initial_run or len(self.can_flash):
            if initial_run:
                initial_run = False
                self._get_flashers_for_tick()

            if not len(self.can_flash):
                break

            octopus = self.can_flash.pop()
            octopus.flash(self.grid)
            flashed_during_tick += 1
            self.flash_counter += 1

            for coord in octopus.adjacent_octopuses:
                adjacent_octopus = self.grid[coord]
                if (
                    adjacent_octopus not in self.can_flash
                    and adjacent_octopus.can_flash
                ):
                    self.can_flash.append(adjacent_octopus)

        if flashed_during_tick == self.total_octopuses:
            return True
        return False


@register_solution(2021, 11, 1)
def part_one(input_data: list[str]):
    grid = OctopusGrid(input_data)
    run_ticks(grid, 100)

    answer = grid.flash_counter

    if not answer:
        raise SolutionNotFoundError(2021, 11, 1)

    return answer


@register_solution(2021, 11, 2)
def part_two(input_data: list[str]):
    grid = OctopusGrid(input_data)
    answer = run_ticks_until_sync(grid)

    if not answer:
        raise SolutionNotFoundError(2021, 11, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 11)
    part_one(data)
    part_two(data)
