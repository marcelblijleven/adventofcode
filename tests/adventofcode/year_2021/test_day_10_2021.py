import pytest

from adventofcode.year_2021.day_10_2021 import (
    count_points_autocomplete,
    count_points_corrupted_characters,
    filter_lines,
    find_closing_characters,
    find_corrupted_characters,
    part_one,
    part_two,
    reduce_line,
)

test_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_find_corrupted_lines():
    assert len(find_corrupted_characters(test_input)) == 5


@pytest.mark.parametrize(
    ["characters", "expected"],
    [
        ([")"], 3),
        ([")", ")"], 6),
        (["]"], 57),
        (["]", "]"], 114),
        (["}"], 1197),
        (["}", "}"], 2394),
        ([">"], 25137),
        ([">", ">"], 50274),
        ([")", ")", ">", ">"], 50280),
        ([")", "]", "}", ">"], 26394),
    ],
)
def test_count_points_corrupted_characters(characters, expected):
    assert count_points_corrupted_characters(characters) == expected


def test_filter_lines():
    assert len(filter_lines(test_input)) == 5


@pytest.mark.parametrize(
    ["line", "expected"],
    [
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", "]"),
        ("[<(<(<(<{}))><([]([]()", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
    ],
)
def test_reduce_line(line, expected):
    assert reduce_line(line) == expected


def test_reduce_line_raises():
    with pytest.raises(ValueError) as wrapped_e:
        reduce_line("[[[!]]]")

    assert str(wrapped_e.value) == "unknown character received: !"


def test_find_closing_characters():
    assert find_closing_characters(test_input) == [
        "}}]])})]",
        ")}>]})",
        "}}>}>))))",
        "]]}}]}]}>",
        "])}>",
    ]


@pytest.mark.parametrize(
    ["lines", "expected"],
    [
        (["])}>"], 294),
        (
            [
                "}}]])})]",
                ")}>]})",
                "}}>}>))))",
                "]]}}]}]}>",
                "])}>",
            ],
            288957,
        ),
    ],
)
def test_count_points_autocomplete(lines, expected):  # noqa
    assert count_points_autocomplete(["])}>"]) == 294


def test_part_one():
    assert part_one(test_input) == 26397


def test_part_two():
    assert part_two(test_input) == 288957
