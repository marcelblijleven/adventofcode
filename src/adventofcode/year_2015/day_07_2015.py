import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

PATTERN = re.compile(r"(?:(\w+)?\s?(RSHIFT|LSHIFT|AND|OR|NOT) )?(\w+)")
OP_PATTERN = re.compile(r"\b(RSHIFT|LSHIFT|AND|OR|NOT)\b")


def is_operation(value: str) -> bool:
    # operations = ['AND', 'OR', 'SHIFT', 'NOT']
    # return any([operation for operation in operations if operation in value])
    return len(OP_PATTERN.findall(value)) > 0


def do_not(value: int) -> int:
    return (1 << 16) - 1 - value


def do_or(left: int, right: int) -> int:
    return left | right


def do_and(left: int, right: int) -> int:
    return left & right


def do_lshift(left: int, right: int) -> int:
    return left << right


def do_rshift(left: int, right: int) -> int:
    return left >> right


class Graph:
    def __init__(self, lines: list[str]):
        self._seen: dict[str, int] = {}
        self._values: dict[str, str | int] = {}
        self._parse_lines(lines)

    def _parse_lines(self, lines: list[str]):
        for line in lines:
            op, target = line.split(" -> ")
            self._values[target] = op

    def _execute_operation(self, left: str, operation: str, right: str) -> int:
        if operation == "NOT":
            right_value = self.get_value(right)
            return do_not(right_value)

        if operation == "OR":
            left_value = self.get_value(left)
            right_value = self.get_value(right)
            return do_or(left_value, right_value)

        if operation == "AND":
            left_value = self.get_value(left)
            right_value = self.get_value(right)
            return do_and(left_value, right_value)

        if operation == "LSHIFT":
            left_value = self.get_value(left)
            right_value = int(self.get_value(right))
            return do_lshift(left_value, right_value)

        if operation == "RSHIFT":
            left_value = self.get_value(left)
            right_value = int(self.get_value(right))
            return do_rshift(left_value, right_value)

        raise ValueError(f"unknown operation: {operation}")

    def get_value(self, key: str | int) -> int:
        """
        Recursively traverse the graph to find the value
        """
        if str(key) in self._seen:
            return self._seen[str(key)]

        try:
            int_value = int(key)
            return int_value
        except ValueError:
            # value is an operation or assignment and must be parsed
            pass

        value = self._values[str(key)]

        try:
            return int(value)
        except ValueError:
            pass

        if is_operation(str(value)):
            if (match := PATTERN.match(str(value))) is not None:
                groups = match.groups()
                left, operation, right = groups
                value = self._execute_operation(left, operation, right)
                self._seen[str(key)] = value
                return value

            raise ValueError("could not parse operation")
        else:
            # Direct assignment, get value either via key or parsed int
            retrieved_value = self.get_value(value)
            self._seen[str(key)] = retrieved_value
            return retrieved_value

    def set_value(self, key: str, value: int) -> None:
        """
        For part two, sets the value and clears _seen to recalculate the new values
        """
        self._seen = {}
        self._values[key] = value


@register_solution(2015, 7, 1)
def part_one(input_data: list[str]):
    graph = Graph(input_data)
    answer = graph.get_value("a")

    if not answer:
        raise SolutionNotFoundError(2015, 7, 1)

    return answer


@register_solution(2015, 7, 2)
def part_two(input_data: list[str]):
    graph = Graph(input_data)
    answer_part_one = graph.get_value("a")
    graph.set_value("b", answer_part_one)
    answer = graph.get_value("a")

    if not answer:
        raise SolutionNotFoundError(2015, 7, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 7)
    part_one(data)
    part_two(data)
