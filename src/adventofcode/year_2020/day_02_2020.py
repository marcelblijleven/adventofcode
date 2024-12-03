import re
from collections.abc import Sequence

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


class PasswordHelper:
    def __init__(self, line: str):
        self.line: str = line
        self.pattern = re.compile(r"(\d+)-(\d+) (\w+): (\w+)")
        self._matches: Sequence[str] = []

    @property
    def lower_bound(self) -> int:
        return int(self.matches[0])

    @property
    def upper_bound(self) -> int:
        return int(self.matches[1])

    @property
    def letter(self) -> str:
        return self.matches[2]

    @property
    def password(self) -> str:
        return self.matches[3]

    @property
    def matches(self) -> Sequence[str]:
        if not self._matches:
            self._matches = re.match(self.pattern, self.line).groups()  # type: ignore
            return self._matches

        return self._matches

    def is_valid(self) -> bool:
        return self.password.count(self.letter) in range(
            self.lower_bound, self.upper_bound + 1
        )

    def is_valid_part_two(self) -> bool:
        position_one = self.password[self.lower_bound - 1] == self.letter
        position_two = self.password[self.upper_bound - 1] == self.letter
        return position_one != position_two


@register_solution(2020, 2, 1)
def part_one(input_data: list[str]) -> int:
    passwords = map(PasswordHelper, input_data)
    answer = len([password for password in passwords if password.is_valid()])

    if not answer:
        raise SolutionNotFoundError(2020, 2, 1)

    return answer


@register_solution(2020, 2, 2)
def part_two(input_data: list[str]) -> int:
    passwords = map(PasswordHelper, input_data)
    answer = len([password for password in passwords if password.is_valid_part_two()])

    if not answer:
        raise SolutionNotFoundError(2020, 2, 1)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2020, 2)
    part_one(data)
    part_two(data)
