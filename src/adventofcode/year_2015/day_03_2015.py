from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_for_day

GridType = dict[tuple[int, int], int]


def get_new_position(current: tuple[int, int], instruction: str) -> tuple[int, int]:
    x, y = current
    if instruction == "^":
        y += 1
    elif instruction == ">":
        x += 1
    elif instruction == "v":
        y -= 1
    elif instruction == "<":
        x -= 1
    else:
        raise ValueError(f"invalid instruction received: {instruction}")

    return x, y


@register_solution(2015, 3, 1)
def part_one(input_data: list[str]):
    str_data = "".join(input_data)
    current = (0, 0)
    grid: GridType = {current: 1}

    for instruction in str_data:
        current = get_new_position(current, instruction)

        if current not in grid:
            grid[current] = 1
        else:
            grid[current] += 1

    return len(grid)


def update_grid(santa_like: tuple[int, int], grid: GridType) -> GridType:
    if santa_like not in grid:
        grid[santa_like] = 1
    else:
        grid[santa_like] += 1

    return grid


@register_solution(2015, 3, 2)
def part_two(input_data: list[str]):
    str_data = "".join(input_data)
    santa = (0, 0)
    robo_santa = (0, 0)
    grid: GridType = {(0, 0): 2}

    for i, instruction in enumerate(str_data):
        if i % 2 != 0:
            santa = get_new_position(santa, instruction)
            grid = update_grid(santa, grid)
        else:
            robo_santa = get_new_position(robo_santa, instruction)
            grid = update_grid(robo_santa, grid)

    return len(grid)


if __name__ == "__main__":
    data = get_input_for_day(2015, 3)
    part_one(data)
    part_two(data)
