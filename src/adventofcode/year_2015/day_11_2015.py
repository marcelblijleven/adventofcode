import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

PAIR_PATTERN = re.compile(r"(([a-z])\2)+")


def check_characters(password: str) -> bool:
    for char in ["i", "o", "l"]:
        if char in password:
            return False

    return True


def check_length(password: str) -> bool:
    return len(password) == 8


def check_lowercase(password: str) -> bool:
    return password == password.lower()


def check_pairs(password: str) -> bool:
    pairs = PAIR_PATTERN.findall(password)

    if len(pairs) < 2:
        return False

    return pairs[0] != pairs[1]  # type: ignore


def check_sequential(password: str) -> bool:
    int_password = [ord(char) for char in password]

    for i, value in enumerate(int_password):
        try:
            second = int_password[i + 1]
            third = int_password[i + 2]

            if (value + 1) == second and (value + 2) == third:
                return True
        except IndexError:
            return False

    return False


def is_valid(password: str) -> bool:
    if not check_characters(password):
        return False

    if not check_length(password):
        return False

    if not check_lowercase(password):
        return False

    if not check_pairs(password):
        return False

    if not check_sequential(password):
        return False

    return True


def increment_password(password: str) -> str:
    int_password = [ord(char) for char in password]

    # We need the earliest occurrence of two pairs (aa, cc) and one sequence (abc).
    # this is 5 characters (e.g. aabcc), so we can ignore the first three characters
    # and try to find the sequence based on the fourth letter

    fourth = int_password[3]  # e.g. 'a'
    fifth = fourth  # e.g. 'a'
    sixth = fourth + 1  # e.g. 'b'
    seventh = sixth + 1  # e.g. 'c'
    eighth = seventh  # e.g. 'c'

    password = "".join(
        [
            chr(char)
            for char in int_password[:3] + [fourth, fifth, sixth, seventh, eighth]
        ]
    )

    if not is_valid(password):
        raise ValueError("password invalid")

    return password


def increment_password_part_two(password: str) -> str:
    int_password = [ord(char) for char in password]

    # We need the earliest occurrence of two pairs (aa, cc) and one sequence (abc).
    # this is 5 characters (e.g. aabcc), for part two we need to ignore the first 2 characters
    # and increase the third by one. Then we can add the aabcc

    third = int_password[2] + 1

    password = "".join([chr(x) for x in int_password[:2] + [third]]) + "aabcc"

    if not is_valid(password):
        raise ValueError("password invalid")

    return password


@register_solution(2015, 11, 1)
def part_one(input_data: list[str]):
    answer = increment_password(input_data[0])

    if not answer:
        raise SolutionNotFoundError(2015, 11, 1)

    return answer


@register_solution(2015, 11, 2)
def part_two(input_data: list[str]):
    answer = increment_password_part_two(input_data[0])

    if not answer:
        raise SolutionNotFoundError(2015, 11, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 11)
    part_one(data)
    part_two(data)
