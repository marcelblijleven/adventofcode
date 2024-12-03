from __future__ import annotations

import math
from collections import deque
from collections.abc import Callable
from functools import partial
from typing import Literal

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


class Monkey:
    number: int
    items: deque[int]
    operation: Callable[[int | None], int]
    test: tuple[int, int, int]
    other_monkeys: dict[int, Monkey]
    inspected: int
    allow_relief: bool
    common_modulo: int

    def __init__(
        self,
        number: int,
        starting_items: list[int],
        operation: Callable[[int | None], int],
        test: tuple[int, int, int],
        other_monkeys: dict[int, Monkey],
        allow_relief: bool,
    ):
        self.number = number
        self.items = deque()
        self.items += starting_items
        self.operation = operation
        self.test = test
        self.other_monkeys = other_monkeys
        self.inspected = 0
        self.allow_relief = allow_relief

    def inspect(self) -> None:
        """Monkey inspects the item"""
        self.inspected += 1

    def play_round(self) -> None:
        """
        Loop through all items and apply the rules
        If allow_relief is False, use the product of the divisble part
        of all the test values to keep the number low
        """
        while len(self.items):
            item = self.items.popleft()
            # inspect
            worry_level = self.operation(item)
            self.inspect()

            if self.allow_relief:
                worry_level = math.floor(worry_level / 3)
            else:
                worry_level = worry_level % self.common_modulo

            if worry_level % self.test[0] == 0:
                self.other_monkeys[self.test[1]].catch(worry_level)
            else:
                self.other_monkeys[self.test[2]].catch(worry_level)

    def catch(self, item: int) -> None:
        self.items.append(item)

    def __str__(self) -> str:
        return f"Monkey {self.number} items: {self.items}. inspected items {self.inspected} times"


def old_operand_number(old: int, operand: Literal["+", "*"], number: int) -> int:
    """Operation that performs the operand on the item value and the provided number"""
    if operand == "+":
        return old + number
    return old * number


def old_operand_old(old: int, operand: Literal["+", "*"]) -> int:
    """Operation that performs the operand on the item value with the item value"""
    if operand == "+":
        return old + old
    return old * old


def parse_instructions(input_data: list[str], allow_relief=True) -> dict[int, Monkey]:
    """Parse instructions into a dict of Monkeys"""
    monkeys: dict[int, Monkey] = {}

    idx = 0

    while idx < len(input_data):
        chunk = input_data[idx : idx + 7]

        number = int(chunk[0].split(" ")[-1].rstrip(":"))
        starting_items = [int(item) for item in chunk[1].split(": ")[-1].split(", ")]
        left, operand, right = chunk[2].split(" = ")[-1].split(" ")

        if right == "old":
            operation = partial(old_operand_old, operand=operand)
        else:
            operation = partial(old_operand_number, operand=operand, number=int(right))

        test = (
            int(chunk[3].split(" ")[-1]),
            int(chunk[4].split(" ")[-1]),
            int(chunk[5].split(" ")[-1]),
        )
        monkeys[number] = Monkey(
            number, starting_items, operation, test, monkeys, allow_relief
        )
        idx += 7

    common_modulo = math.prod([monkey.test[0] for monkey in monkeys.values()])
    for monkey in monkeys.values():
        monkey.common_modulo = common_modulo

    return monkeys


def play_rounds(input_data: list[str], rounds: int = 20, allow_relief=True) -> int:
    """Play rounds and let the monkeys do their thing"""
    monkeys = parse_instructions(input_data, allow_relief=allow_relief)

    for _ in range(rounds):
        for monkey in monkeys.values():
            monkey.play_round()

    inspections = sorted(
        [monkey.inspected for monkey in monkeys.values()], reverse=True
    )
    return inspections[0] * inspections[1]


@register_solution(2022, 11, 1)
def part_one(input_data: list[str]):
    answer = play_rounds(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 11, 1)

    return answer


@register_solution(2022, 11, 2)
def part_two(input_data: list[str]):
    answer = play_rounds(input_data, 10000, allow_relief=False)

    if not answer:
        raise SolutionNotFoundError(2022, 11, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 11)
    part_one(data)
    part_two(data)
