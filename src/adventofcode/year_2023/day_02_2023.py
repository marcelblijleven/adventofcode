import math
import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

game_pattern = re.compile(r"(?:(?P<amount>\d+)\s|(?P<color>red|blue|green))")


def parse_game(line) -> list[dict[str, int]]:
    prefix, game = line.split(": ")
    game_values = []
    rounds = game.split("; ")

    for _round in rounds:
        pairs = _round.split(", ")

        round_values = {}
        for pair in pairs:
            number, color = pair.split(" ")
            round_values[color] = int(number)

        game_values.append(round_values)

    return game_values


def check_game(constraints: dict[str, int], game_values: list[dict[str, int]]) -> bool:
    for color, value in constraints.items():
        for game_value in game_values:
            if (check := game_value.get(color)) is not None and check > value:
                return False

    return True


def check_minimum(game_values: list[dict[str, int]]) -> int:
    minimums: dict[str, int] = {}

    for game_value in game_values:
        for color, value in game_value.items():
            if color not in minimums:
                minimums[color] = value
            else:
                minimums[color] = max(value, minimums[color])
    return math.prod(minimums.values())


def find_possibilities(lines: list[str]) -> int:
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    sum_of_ids: int = 0

    for game_number, line in enumerate(lines, start=1):
        game_values = parse_game(line)

        if check_game(constraints, game_values):
            sum_of_ids += game_number

    return sum_of_ids


def find_minimum_possible(lines: list[str]) -> int:
    total: int = 0
    for line in lines:
        game_values = parse_game(line)

        total += check_minimum(game_values)

    return total


@register_solution(2023, 2, 1)
def part_one(input_data: list[str]):
    answer = find_possibilities(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 2, 1)

    return answer


@register_solution(2023, 2, 2)
def part_two(input_data: list[str]):
    answer = find_minimum_possible(input_data)

    if not answer:
        raise SolutionNotFoundError(2023, 2, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 2)
    part_one(data)
    part_two(data)
