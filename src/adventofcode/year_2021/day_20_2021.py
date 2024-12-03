from collections import defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

Algorithm = list[int]
Pixel = tuple[int, int]
LIGHT = 1
DARK = 0
STEP = 0


def get_algorithm_position_for_pixel_simplified(
    pixel: Pixel, infinity_grid: defaultdict[Pixel, int]
) -> int:
    pixel_grid = [
        (-1, -1),
        (+0, -1),
        (+1, -1),
        (-1, +0),
        (+0, +0),
        (+1, +0),
        (-1, +1),
        (+0, +1),
        (+1, +1),
    ]
    algo_position = "".join(
        [
            str(infinity_grid[pixel[0] + offset[0], pixel[1] + offset[1]])
            for offset in pixel_grid
        ]
    )
    return int(algo_position, 2)


def get_algorithm_position_for_pixel(
    pixel: Pixel, infinity_grid: defaultdict[Pixel, int]
) -> int:
    pixel_grid = [
        (-1, -1),
        (+0, -1),
        (+1, -1),
        (-1, +0),
        (+0, +0),
        (+1, +0),
        (-1, +1),
        (+0, +1),
        (+1, +1),
    ]

    algo_position = 0

    for i, offset in enumerate(pixel_grid):
        x, y = pixel[0] + offset[0], pixel[1] + offset[1]
        bit = 9 - i - 1

        value = infinity_grid[x, y]

        if value == 0:
            algo_position = algo_position & ~(1 << bit)
        else:
            algo_position = algo_position | (1 << bit)

    return algo_position


class Image:
    def __init__(self, input_data: list[str], algorithm: Algorithm) -> None:
        self.grid: defaultdict[Pixel, int] = defaultdict(int)
        self.algorithm = algorithm
        self.toggles = algorithm[0] == LIGHT and algorithm[-1] == DARK

        self._init_grid(input_data)

    def _init_grid(self, input_data: list[str]):
        for y, line in enumerate(input_data):
            for x, value in enumerate(line):
                if value == "#":
                    self.grid[x, y] = 1

    def enhance(self, times: int) -> int:
        for step in range(times):
            x_values = [key[0] for key in self.grid.keys()]
            y_values = [key[1] for key in self.grid.keys()]
            min_x, max_x, min_y, max_y = (
                min(x_values),
                max(x_values),
                min(y_values),
                max(y_values),
            )
            infinity_grid = get_infinity_grid(self.toggles, int(step % 2 == 0))

            for y in range(min_y - 1, max_y + 2):  # provide padding around grid
                for x in range(min_x - 1, max_x + 2):
                    algo_position = get_algorithm_position_for_pixel((x, y), self.grid)
                    infinity_grid[x, y] = self.algorithm[algo_position]

            self.grid = infinity_grid

        return sum(self.grid.values())


def get_infinity_grid(toggles: bool, default_value: int) -> defaultdict[Pixel, int]:
    if toggles:
        return defaultdict(lambda: default_value)

    return defaultdict(int)


def parse_input(input_data: list[str]) -> Image:
    algorithm = [1 if x == "#" else 0 for x in input_data[0]]
    image = Image(input_data[2:], algorithm)
    return image


@register_solution(2021, 20, 1)
def part_one(input_data: list[str]):
    image = parse_input(input_data)
    answer = image.enhance(2)

    if not answer:
        raise SolutionNotFoundError(2021, 20, 1)

    return answer


@register_solution(2021, 20, 2)
def part_two(input_data: list[str]):
    image = parse_input(input_data)
    answer = image.enhance(50)

    if not answer:
        raise SolutionNotFoundError(2021, 20, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 20)
    part_one(data)
    part_two(data)
