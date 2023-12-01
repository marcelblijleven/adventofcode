from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

mul = 252533
mod = 33554393


def get_next_code(current_code: int, coords: tuple[int, int]) -> int:
    x, y = 1, 1
    want_x, want_y = coords

    while True:
        if y == 1:
            y = x + 1
            x = 1
        else:
            y -= 1
            x += 1

        current_code = (current_code * mul) % mod

        if x == want_x and y == want_y:
            return current_code


@register_solution(2015, 25, 1)
def part_one(_: list[str]):
    row = 2978
    column = 3083
    answer = get_next_code(20151125, (column, row))

    if not answer:
        raise SolutionNotFoundError(2015, 25, 1)

    return answer


@register_solution(2015, 25, 2)
def part_two(input_data: list[str]):  # noqa
    answer = "hooray"

    if not answer:
        raise SolutionNotFoundError(2015, 25, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 25)
    part_one(data)
    part_two(data)
