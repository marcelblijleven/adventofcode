from collections import Counter, deque
from collections.abc import Iterable
from functools import cmp_to_key, partial
from itertools import starmap

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

cards = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

cards_with_jokers = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}

hands = {
    "Five of a kind": 7,
    "Four of a kind": 6,
    "Full house": 5,
    "Three of a kind": 4,
    "Two pair": 3,
    "One pair": 2,
    "High card": 1,
}


def parse_input(data: list[str]) -> Iterable[tuple[str, int]]:
    def parse_line(line: str) -> tuple[str, int]:
        hand, number = line.split(" ")
        return hand, int(number)

    return map(parse_line, data)


def parse_hand(hand: str, with_jokers: bool) -> int:
    if "J" in hand and with_jokers:
        return parse_hand_with_jokers(hand)

    counter = Counter(hand)
    values = counter.values()

    if 5 in values:
        return hands["Five of a kind"]
    if 4 in values:
        return hands["Four of a kind"]
    if 3 in values:
        if 2 in values:
            return hands["Full house"]
        return hands["Three of a kind"]
    if 2 in values:
        if len(values) == 3:
            return hands["Two pair"]
        if len(values) == 4:
            return hands["One pair"]
    return hands["High card"]


def parse_hand_with_jokers(hand: str) -> int:
    values: list[int] = []
    for letter in set(hand):
        joker_hand = hand.replace("J", letter)
        values.append(parse_hand(joker_hand, with_jokers=False))

    return max(values)


def sort_hands(
    hand_a: tuple[str, int], hand_b: tuple[str, int], with_jokers: bool
) -> int:
    parsed_a = parse_hand(hand_a[0], with_jokers=with_jokers)
    parsed_b = parse_hand(hand_b[0], with_jokers=with_jokers)

    if parsed_a > parsed_b:
        return 1
    elif parsed_a < parsed_b:
        return -1
    else:
        deque_a = deque(hand_a[0])
        deque_b = deque(hand_b[0])

        while len(deque_a) != 0:
            if with_jokers:
                a = cards_with_jokers[deque_a.popleft()]
                b = cards_with_jokers[deque_b.popleft()]
            else:
                a = cards[deque_a.popleft()]
                b = cards[deque_b.popleft()]

            if a > b:
                return 1
            elif a < b:
                return -1

    return 0


def calculate_winnings(data: list[str], with_jokers: bool) -> int:
    sort_func = partial(sort_hands, with_jokers=with_jokers)
    sorted_hands = sorted(parse_input(data), key=cmp_to_key(sort_func))  # type: ignore
    return sum(
        starmap(lambda idx, hand: hand[1] * idx, enumerate(sorted_hands, start=1))
    )


@register_solution(2023, 7, 1)
def part_one(input_data: list[str]):
    answer = calculate_winnings(input_data, with_jokers=False)

    if not answer:
        raise SolutionNotFoundError(2023, 7, 1)

    return answer


@register_solution(2023, 7, 2)
def part_two(input_data: list[str]):
    answer = calculate_winnings(input_data, with_jokers=True)

    if not answer:
        raise SolutionNotFoundError(2023, 7, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2023, 7)
    part_one(data)
    part_two(data)
