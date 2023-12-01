from __future__ import annotations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

# A, X Rock
# B, Y Paper
# C, Z Scissors
# A,X > C,Z
# B,Y > A,X
# C,Z > A,X


ROUND_ONE_MAPPING = {
    # Draws
    "A X": 1 + 3,
    "B Y": 2 + 3,
    "C Z": 3 + 3,
    # Losses
    "B X": 1 + 0,
    "C Y": 2 + 0,
    "A Z": 3 + 0,
    # Wins:
    "C X": 1 + 6,
    "A Y": 2 + 6,
    "B Z": 3 + 6,
}

ROUND_TWO_MAPPING = {
    # Losses
    "A X": 3 + 0,  # Player chooses Z
    "B X": 1 + 0,  # Player chooses X
    "C X": 2 + 0,  # Player chooses Y
    # Draws
    "A Y": 1 + 3,  # Player chooses X
    "B Y": 2 + 3,  # Player chooses Y
    "C Y": 3 + 3,  # Player chooses Z
    # Wins
    "A Z": 2 + 6,  # Player chooses Y
    "B Z": 3 + 6,  # Player chooses Z
    "C Z": 1 + 6,  # Player chooses X
}


class Shape:
    value: int

    @property
    def nemesis(self) -> Shape:
        raise NotImplementedError

    @property
    def easy_win(self) -> Shape:
        raise NotImplementedError


class Rock(Shape):
    value = 1

    @property
    def nemesis(self) -> Shape:
        return Paper()

    @property
    def easy_win(self) -> Shape:
        return Scissors()

    def __lt__(self, other):
        return isinstance(other, Paper)

    def __gt__(self, other):
        return isinstance(other, Scissors)

    def __eq__(self, other):
        return isinstance(other, Rock)


class Paper(Shape):
    value = 2

    @property
    def nemesis(self) -> Shape:
        return Scissors()

    @property
    def easy_win(self) -> Shape:
        return Rock()

    def __lt__(self, other):
        return isinstance(other, Scissors)

    def __gt__(self, other):
        return isinstance(other, Rock)

    def __eq__(self, other):
        return isinstance(other, Paper)


class Scissors(Shape):
    value = 3

    @property
    def nemesis(self) -> Shape:
        return Rock()

    @property
    def easy_win(self) -> Shape:
        return Paper()

    def __lt__(self, other):
        return isinstance(other, Rock)

    def __gt__(self, other):
        return isinstance(other, Paper)

    def __eq__(self, other):
        return isinstance(other, Scissors)


def get_shape(letter: str) -> Rock | Paper | Scissors:
    if letter in ["A", "X"]:
        return Rock()
    if letter in ["B", "Y"]:
        return Paper()
    if letter in ["C", "Z"]:
        return Scissors()

    raise ValueError("unknown letter received")


def play_round_one(input_data: list[str]) -> int:
    score = 0

    for row in input_data:
        their_move, your_move = row.split(" ")
        theirs = get_shape(their_move)
        yours = get_shape(your_move)

        if theirs > yours:
            score += 0 + yours.value
        elif yours > theirs:
            score += 6 + yours.value
        elif yours == theirs:
            score += 3 + yours.value

    return score


def get_shapes_round_two(row: str):
    theirs, yours = row.split(" ")
    their_shape = get_shape(theirs)

    if yours == "X":  # lose
        return their_shape, their_shape.easy_win
    if yours == "Y":  # draw
        return their_shape, their_shape
    if yours == "Z":  # win
        return their_shape, their_shape.nemesis


def play_round_two(input_data: list[str]) -> int:
    score = 0

    for row in input_data:
        theirs, yours = get_shapes_round_two(row)

        if theirs > yours:
            score += 0 + yours.value
        elif yours > theirs:
            score += 6 + yours.value
        elif yours == theirs:
            score += 3 + yours.value

    return score


def play_round_one_with_mapping(input_data: list[str]) -> int:
    score = 0
    for row in input_data:
        score += ROUND_ONE_MAPPING[row]
    return score


def play_round_two_with_mapping(input_data: list[str]) -> int:
    score = 0
    for row in input_data:
        score += ROUND_TWO_MAPPING[row]
    return score


@register_solution(2022, 2, 1)
def part_one(input_data: list[str]):
    answer = play_round_one(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 2, 1)

    return answer


@register_solution(2022, 2, 1, "mapping")
def part_one_with_mapping(input_data: list[str]):
    answer = play_round_one_with_mapping(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 2, 1)

    return answer


@register_solution(2022, 2, 2)
def part_two(input_data: list[str]):
    answer = play_round_two(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 2, 2)

    return answer


@register_solution(2022, 2, 2, "mapping")
def part_two_with_mapping(input_data: list[str]):
    answer = play_round_two_with_mapping(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 2, 1)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 2)
    part_one(data)
    part_one_with_mapping(data)
    part_two(data)
    part_two_with_mapping(data)
