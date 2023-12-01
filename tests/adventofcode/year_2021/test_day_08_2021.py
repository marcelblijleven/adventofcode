from adventofcode.year_2021.day_08_2021 import (
    count_unique_segments,
    get_output_for_line,
    get_unique_segments,
    parse_input,
    part_one,
    part_two,
    pattern_translation_table,
    patterns_as_frozen_sets,
)

test_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]

test_input_single_line = [
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf",
]


def test_parse_input():
    parsed = parse_input(test_input)
    assert len(parsed) == 10


def test_pattern_translation_table():
    patterns, _ = parse_input(test_input_single_line)[0]
    fs_patterns = patterns_as_frozen_sets(patterns.split(" "))
    assert pattern_translation_table(fs_patterns) == {
        frozenset({"a", "b"}): 1,
        frozenset({"a", "d", "b"}): 7,
        frozenset({"a", "f", "b", "e"}): 4,
        frozenset({"d", "c", "f", "b", "e"}): 5,
        frozenset({"a", "d", "c", "f", "g"}): 2,
        frozenset({"a", "d", "c", "f", "b"}): 3,
        frozenset({"a", "d", "c", "f", "b", "e"}): 9,
        frozenset({"d", "c", "f", "b", "g", "e"}): 6,
        frozenset({"a", "d", "c", "b", "g", "e"}): 0,
        frozenset({"a", "d", "c", "f", "b", "g", "e"}): 8,
    }


def test_get_output_for_line():
    line = parse_input(test_input_single_line)[0]
    assert get_output_for_line(line) == 5353


def test_get_unique_segments():
    parsed = parse_input(test_input_single_line)
    assert get_unique_segments(parsed[0][0]) == ["acedgfb", "dab", "eafb", "ab"]


def test_count_unique_segments():
    parsed = parse_input(test_input)
    assert count_unique_segments(parsed) == 26


def test_part_one():
    answer = part_one(test_input)
    assert answer == 26


def test_part_two():
    answer = part_two(test_input)
    assert answer == 61229
