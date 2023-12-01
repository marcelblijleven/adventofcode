from __future__ import annotations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.helpers import memoize
from adventofcode.util.input_helpers import get_input_for_day


def parse_input(input_data: list[str]) -> tuple[int, int]:
    player_one = int(input_data[0][-1])
    player_two = int(input_data[1][-1])
    return player_one, player_two


def get_new_position(current_position: int, moves: int) -> int:
    max_position = 10
    if (next_position := (current_position + moves) % max_position) != 0:
        return next_position

    return max_position


class DeterministicDie:
    def __init__(self):
        self.rolls = 0
        self._next_roll = 1
        self._last_roll = 0

    def roll(self) -> int:
        roll = self._next_roll

        if self._next_roll + 1 > 100:
            self._next_roll = 1
        else:
            self._next_roll += 1

        self._last_roll = roll
        self.rolls += 1
        return roll


class Player:
    def __init__(self, number: int, starting_position: int, max_score: int = 1000):
        self.number = number
        self._position = starting_position
        self._score = 0
        self._max_score = max_score

    @property
    def score(self) -> int:
        return self._score

    @property
    def has_won(self) -> bool:
        return self.score >= self._max_score

    def add_to_score(self, addition: int):
        self._score += addition

    def move(self, moves: int):
        self._position = get_new_position(self._position, moves)
        self.add_to_score(self._position)

    def roll_die(self, die: DeterministicDie) -> bool:
        moves = []

        for _ in range(3):
            moves.append(die.roll())

        self.move(sum(moves))
        # print(
        #   f'Player {self.number} rolls {"+".join(map(str, moves))} and moves to space {self._position} ' +
        #   'for a total score of {self.score}'
        # )
        return self.has_won


def game(player_one: Player, player_two: Player) -> int:
    players = [player_one, player_two]
    die = DeterministicDie()
    rounds = 0

    while True:
        player = players[rounds % 2]
        if player.roll_die(die):
            break

        rounds += 1

    rolls = die.rolls
    losing_score = [p for p in players if not p.has_won][0].score  # noqa
    return rolls * losing_score


def apply_wins(
    wins: tuple[int, int], universe_wins: tuple[int, int]
) -> tuple[int, int]:
    return wins[0] + universe_wins[1], wins[1] + universe_wins[0]


@memoize
def quantum_game(player_one_pos, player_two_pos, player_one_score, player_two_score):
    if player_one_score >= 21:
        return 1, 0
    elif player_two_score >= 21:
        return 0, 1

    wins = (0, 0)

    for r1 in [1, 2, 3]:
        for r2 in [1, 2, 3]:
            for r3 in [1, 2, 3]:
                next_pos = get_new_position(player_one_pos, r1 + r2 + r3)
                score = player_one_score + next_pos
                universe_wins = quantum_game(
                    player_two_pos, next_pos, player_two_score, score
                )
                wins = apply_wins(wins, universe_wins)

    return wins


@register_solution(2021, 21, 1)
def part_one(input_data: list[str]):
    positions = parse_input(input_data)
    answer = game(Player(1, positions[0]), Player(2, positions[1]))

    if not answer:
        raise SolutionNotFoundError(2021, 21, 1)

    return answer


@register_solution(2021, 21, 2)
def part_two(input_data: list[str]):
    positions = parse_input(input_data)
    answer = max(quantum_game(positions[0], positions[1], 0, 0))

    if not answer:
        raise SolutionNotFoundError(2021, 21, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 21)
    part_one(data)
    part_two(data)
