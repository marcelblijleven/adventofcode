import json
from itertools import zip_longest

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

Packet = list[int] | list["Packet"]
Pair = tuple[Packet, Packet]


def parse_line(line: str) -> Packet:
    """Parse line into Packet"""
    return json.loads(line)


def parse_pairs(input_data: list[str]) -> list[Pair]:
    """Parse input into list of Pair"""
    pairs: list[tuple[Packet, Packet]] = []
    current_pair: Pair = ()  # type: ignore

    for line in [*input_data, ""]:
        if not line:
            pairs.append(current_pair)
            current_pair = ()  # type: ignore
        else:
            current_pair += (parse_line(line),)  # type: ignore

    return pairs


def compare_pairs(left: Packet, right: Packet) -> bool | None:
    """
    Check if the packets in the pair are in the correct order

    When both are ints:
    If left is less than right, packets are in the correct order
    If left is greater than right, packets are not in the correct order
    If left equals right, continue

    When exactly one is int:
    Convert the int to a list and compare recursively

    When both are lists:
    If left runs out before right, packets are in the correct order
    If right runs out before left, packets are not in the correct order
    Compare each value recursively if necessary
    """
    for left_value, right_value in zip_longest(left, right):
        if left_value is None:
            return True
        if right_value is None:
            return False

        if isinstance(left_value, int) and isinstance(right_value, int):
            if left_value == right_value:
                continue

            return left_value < right_value

        # Either left or right is an int, or both are list
        _left_value = left_value if isinstance(left_value, list) else [left_value]
        _right_value = right_value if isinstance(right_value, list) else [right_value]

        if (outcome := compare_pairs(_left_value, _right_value)) is not None:
            return outcome

    return None


def find_packets(input_data: list[str]) -> int:
    """Find sum of Pair indexes that are in the correct order"""
    pairs = parse_pairs(input_data)
    sum_of_pairs = 0

    for index, pair in enumerate(pairs, start=1):
        if compare_pairs(*pair):
            sum_of_pairs += index

    return sum_of_pairs


def find_distress_signal(input_data: list[str]) -> int:
    """
    Find the distress signal by injecting two divider packets,
    sorting all packets using a bubble sort and then find the position
    of the two divider packets
    """
    pairs = parse_pairs(input_data)
    divider_packet_one = [[2]]
    divider_packet_two = [[6]]
    packets: list[Packet] = [divider_packet_one, divider_packet_two]  # type: ignore

    for pair in pairs:
        left, right = pair
        packets += [left, right]

    # Bubble sort
    for _ in range(len(packets)):
        for index in range(len(packets) - 1):
            # Swap if packet is not in right order
            if not compare_pairs(packets[index], packets[index + 1]):
                packets[index], packets[index + 1] = packets[index + 1], packets[index]

    # Find divider packets
    one = packets.index(divider_packet_one) + 1  # type: ignore
    two = packets.index(divider_packet_two) + 1  # type: ignore
    return one * two


@register_solution(2022, 13, 1)
def part_one(input_data: list[str]):
    answer = find_packets(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 13, 1)

    return answer


@register_solution(2022, 13, 2, "bubble sort")
def part_two(input_data: list[str]):
    answer = find_distress_signal(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 13, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 13)
    part_one(data)
    part_two(data)
