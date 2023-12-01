from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def get_pairs(row: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """Split a row into two tuple[int, int]"""
    left, right = row.split(",")
    left_start, left_end = left.split("-")
    right_start, right_end = right.split("-")

    return (int(left_start), int(left_end)), (int(right_start), int(right_end))


def does_contain(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """Checks if one range contains another"""
    left_a, right_a = a
    left_b, right_b = b

    # B contains A
    if left_b <= left_a <= right_b and left_b <= right_a <= right_b:
        return True

    # A contains B
    if left_a <= left_b <= right_a and left_a <= right_b <= right_a:
        return True

    return False


def does_overlap(a: tuple[int, int], b: tuple[int, int]) -> bool:
    """Checks if the ranges overlap"""
    left_a, right_a = a
    left_b, right_b = b
    return bool(set(range(left_a, right_a + 1)) & set(range(left_b, right_b + 1)))


def find_containing(input_data: list[str]) -> int:
    """Find all pairs that contain another pair"""
    containing: int = 0

    for row in input_data:
        if does_contain(*get_pairs(row)):
            containing += 1
    return containing


def find_overlapping(input_data: list[str]) -> int:
    """Find all overlapping pairs"""
    overlapping: int = 0

    for row in input_data:
        if does_overlap(*get_pairs(row)):
            overlapping += 1

    return overlapping


@register_solution(2022, 4, 1)
def part_one(input_data: list[str]):
    answer = find_containing(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 4, 1)

    return answer


@register_solution(2022, 4, 2)
def part_two(input_data: list[str]):
    answer = find_overlapping(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 4, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 4)
    part_one(data)
    part_two(data)
