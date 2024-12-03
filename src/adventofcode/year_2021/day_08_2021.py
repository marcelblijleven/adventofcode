from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

segment_0 = "abcefg"
segment_1 = "cf"
segment_2 = "acdeg"
segment_3 = "acdfg"
segment_4 = "bcdf"
segment_5 = "abdfg"
segment_6 = "abdefg"
segment_7 = "acf"
segment_8 = "abcdefg"
segment_9 = "abcdfg"
lengths = [len(segment_1), len(segment_4), len(segment_7), len(segment_8)]

InputLine = tuple[str, str]
TranslationTable = dict[frozenset[str], int]


def parse_input(input_data: list[str]) -> list[InputLine]:
    lines: list[InputLine] = []

    for line in input_data:
        input_segments, output = line.split(" | ")
        lines.append((input_segments, output))

    return lines


def get_unique_segments(line: str) -> list[str]:
    unique = [inp for inp in get_digits(line) if len(inp) in lengths]
    return unique


def count_unique_segments(lines: list[InputLine]) -> int:
    count = 0

    for line in lines:
        _, output = line
        count += len(get_unique_segments(line[1]))

    return count


def get_digits(line: str) -> list[str]:
    return line.split(" ")


def get_output_for_line(line: InputLine) -> int:
    output = 0
    input_data, output_data = line
    output_sets = list(map(frozenset, output_data.split(" ")))  # type: ignore
    patterns = patterns_as_frozen_sets(input_data.split(" "))
    table = pattern_translation_table(patterns)

    output += table[output_sets[0]] * 1000  # type: ignore
    output += table[output_sets[1]] * 100  # type: ignore
    output += table[output_sets[2]] * 10  # type: ignore
    output += table[output_sets[3]]  # type: ignore

    return output


def get_all_outputs(lines: list[InputLine]) -> list[int]:
    outputs: list[int] = []

    for line in lines:
        outputs.append(get_output_for_line(line))

    return outputs


def patterns_as_frozen_sets(patterns: list[str]) -> list[frozenset[str]]:
    return list(map(frozenset, patterns))  # type: ignore


def _fill_table_with_know_patterns(
    patterns: list[frozenset[str]], table: TranslationTable
):
    for pattern in patterns:
        if len(pattern) == 2:
            table[pattern] = 1
        elif len(pattern) == 3:
            table[pattern] = 7
        elif len(pattern) == 4:
            table[pattern] = 4
        elif len(pattern) == 7:
            table[pattern] = 8


def pattern_translation_table(patterns: list[frozenset[str]]) -> TranslationTable:
    translation_table: TranslationTable = {}
    _fill_table_with_know_patterns(patterns, translation_table)

    reversed_table = {v: k for k, v in translation_table.items()}

    for pattern in patterns:
        if len(pattern) == 5:
            if len(pattern.intersection(reversed_table[1])) == 2:
                translation_table[pattern] = 3
            elif len(pattern.intersection(reversed_table[4])) == 3:
                translation_table[pattern] = 5
            else:
                translation_table[pattern] = 2
        elif len(pattern) == 6:
            if len(pattern.intersection(reversed_table[4])) == 4:
                translation_table[pattern] = 9
            elif len(pattern.intersection(reversed_table[7])) == 2:
                translation_table[pattern] = 6
            else:
                translation_table[pattern] = 0

    return translation_table


@register_solution(2021, 8, 1)
def part_one(input_data: list[str]):
    parsed = parse_input(input_data)
    answer = count_unique_segments(parsed)

    if not answer:
        raise SolutionNotFoundError(2021, 8, 1)

    return answer


@register_solution(2021, 8, 2)
def part_two(input_data: list[str]):
    parsed = parse_input(input_data)
    answer = sum(get_all_outputs(parsed))

    if not answer:
        raise SolutionNotFoundError(2021, 8, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 8)
    part_one(data)
    part_two(data)
