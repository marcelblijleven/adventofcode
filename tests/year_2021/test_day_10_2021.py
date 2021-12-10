import pytest

from adventofcode.year_2021.day_10_2021 import part_two, part_one, find_corrupted_characters, \
    count_points_corrupted_characters, filter_lines, find_closing_characters, count_points_autocomplete

test_input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]',
]


def test_find_corrupted_lines():
    assert len(find_corrupted_characters(test_input)) == 5


def test_count_points_corrupted_characters():
    assert count_points_corrupted_characters([')', ')', '>', '>']) == 50280


def test_filter_lines():
    assert len(filter_lines(test_input)) == 5


def test_find_closing_characters():
    assert find_closing_characters(test_input) == [
        '}}]])})]',
        ')}>]})',
        '}}>}>))))',
        ']]}}]}]}>',
        '])}>',
    ]


@pytest.mark.parametrize(['lines', 'expected'], [
    (['])}>'], 294),
    ([
        '}}]])})]',
        ')}>]})',
        '}}>}>))))',
        ']]}}]}]}>',
        '])}>',
    ], 288957)
])
def test_count_points_autocomplete(lines, expected):
    assert count_points_autocomplete(['])}>']) == 294


def test_part_one():
    assert part_one(test_input) == 26397


def test_part_two():
    assert part_two(test_input) == 288957
