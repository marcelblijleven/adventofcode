from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def evaluate_slope(input_data: list[str], x_movement: int, y_movement: int) -> int:
    position = [0, 0]
    grid_width = len(input_data[0])
    counter = 0

    while position[1] <= len(input_data):
        position[0] += x_movement
        position[1] += y_movement

        if position[0] >= grid_width:
            position[0] = position[0] - grid_width

        x, y = position

        if y >= len(input_data):
            break

        if input_data[y][x] != ".":
            counter += 1

    return counter


@register_solution(2020, 3, 1)
def part_one(input_data: list[str]) -> int:
    answer = evaluate_slope(input_data, 3, 1)

    if not answer:
        raise SolutionNotFoundError(2020, 3, 1)

    return answer


@register_solution(2020, 3, 2)
def part_two(input_data: list[str]) -> int:
    import math

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    evaluated = []

    for slope in slopes:
        x, y = slope
        evaluated.append(evaluate_slope(input_data, x, y))

    return math.prod(evaluated)


if __name__ == "__main__":
    data = get_input_for_day(2020, 3)
    part_one(data)
    part_two(data)
