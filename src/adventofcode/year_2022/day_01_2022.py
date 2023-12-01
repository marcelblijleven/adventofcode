from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def find_most_calories(input_data: list[str]) -> int:
    """Find the most calories a single Elf carries"""
    calories = 0
    max_calories = 0

    for row in [*input_data, ""]:
        if row == "":
            max_calories = calories if calories > max_calories else max_calories
            calories = 0
            continue

        calories += int(row)

    return max_calories


def find_top_three_most_calories(input_data: list[str]) -> int:
    """Find the sum of calories of the top 3 Elves"""
    calories = 0
    chunks = []

    for row in [*input_data, ""]:
        if row == "":
            chunks.append(calories)
            calories = 0
            continue
        calories += int(row)

    chunks.sort(reverse=True)
    return sum(chunks[:3])


@register_solution(2022, 1, 1)
def part_one(input_data: list[str]):
    answer = find_most_calories(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 1, 1)

    return answer


@register_solution(2022, 1, 2)
def part_two(input_data: list[str]):
    answer = find_top_three_most_calories(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 1)
    part_one(data)
    part_two(data)
