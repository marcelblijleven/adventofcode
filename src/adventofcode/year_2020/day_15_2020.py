from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def parse_input(input_data: list[str]) -> list[int]:
    return list(map(int, input_data[0].split(",")))


def solve(input_data: list[int], rounds: int) -> int:
    seen = {value: index + 1 for index, value in enumerate(input_data[:-1])}
    number = input_data[-1]

    for play_round in range(len(input_data), rounds):
        seen[number], number = (
            play_round,
            0 if number not in seen else play_round - seen[number],
        )
    return number


@register_solution(2020, 15, 1)
def part_one(input_data: list[str]):
    answer = solve(parse_input(input_data), 2020)

    if not answer:
        raise SolutionNotFoundError(2020, 15, 1)

    return answer


@register_solution(2020, 15, 2)
def part_two(input_data: list[str]):
    answer = solve(parse_input(input_data), 30000000)

    if not answer:
        raise SolutionNotFoundError(2020, 15, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2020, 15)
    part_one(data)
    part_two(data)
