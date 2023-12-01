from adventofcode.year_2021.day_14_2021 import get_answer_slow, part_one, part_two

test_input = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]


def test_get_answer_slow():
    assert get_answer_slow(test_input, 10) == 1588


def test_part_one():
    assert part_one(test_input) == 1588


def test_part_two():
    assert part_two(test_input) == 2188189693529
