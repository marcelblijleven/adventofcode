import pytest

from adventofcode.year_2015.day_13_2015 import (
    get_all_combinations,
    get_happiness_chart,
    get_seating_happiness,
    get_unique_persons,
    update_happiness_chart,
)

test_input = [
    "Alice would gain 54 happiness units by sitting next to Bob.",
    "Alice would lose 79 happiness units by sitting next to Carol.",
    "Alice would lose 2 happiness units by sitting next to David.",
    "Bob would gain 83 happiness units by sitting next to Alice.",
    "Bob would lose 7 happiness units by sitting next to Carol.",
    "Bob would lose 63 happiness units by sitting next to David.",
    "Carol would lose 62 happiness units by sitting next to Alice.",
    "Carol would gain 60 happiness units by sitting next to Bob.",
    "Carol would gain 55 happiness units by sitting next to David.",
    "David would gain 46 happiness units by sitting next to Alice.",
    "David would lose 7 happiness units by sitting next to Bob.",
    "David would gain 41 happiness units by sitting next to Carol.",
]


def test_get_happiness_chart():
    expected = {
        ("Alice", "Bob"): 54,
        ("Alice", "Carol"): -79,
        ("Alice", "David"): -2,
        ("Bob", "Alice"): 83,
        ("Bob", "Carol"): -7,
        ("Bob", "David"): -63,
        ("Carol", "Alice"): -62,
        ("Carol", "Bob"): 60,
        ("Carol", "David"): 55,
        ("David", "Alice"): 46,
        ("David", "Bob"): -7,
        ("David", "Carol"): 41,
    }
    assert expected == get_happiness_chart(test_input)


def test_get_seating_happiness():
    chart = get_happiness_chart(test_input)
    persons = get_unique_persons(chart)
    assert 330 == get_seating_happiness(persons, chart)


def test_update_happiness_chart():
    chart = get_happiness_chart(test_input)
    chart = update_happiness_chart(chart, "Marcel")
    assert ("Marcel", "David") in chart
    assert ("Marcel", "Carol") in chart
    assert ("Marcel", "Alice") in chart
    assert ("Marcel", "Bob") in chart
    assert ("David", "Marcel") in chart
    assert ("Carol", "Marcel") in chart
    assert ("Alice", "Marcel") in chart
    assert ("Bob", "Marcel") in chart


@pytest.mark.parametrize(
    ["value", "expected"],
    [
        (["Marcel", "Julia"], [("Marcel", "Julia")]),
        (
            ["Marcel", "Julia", "Pixel"],
            [("Marcel", "Julia"), ("Marcel", "Pixel"), ("Julia", "Pixel")],
        ),
    ],
)
def test_get_all_combinations(value, expected):
    assert expected == get_all_combinations(value)


def test_get_unique_persons():
    chart = get_happiness_chart(test_input)
    assert sorted(["Carol", "Alice", "Bob", "David"]) == sorted(
        get_unique_persons(chart)
    )
