import pytest

from adventofcode.year_2015.day_07_2015 import (
    Graph,
    do_and,
    do_lshift,
    do_not,
    do_or,
    do_rshift,
    is_operation,
)


@pytest.mark.parametrize(
    ["key", "expected"],
    [
        ("d", 72),
        ("e", 507),
        ("f", 492),
        ("g", 114),
        ("h", 65412),
        ("i", 65079),
        ("x", 123),
        ("y", 456),
    ],
)
def test_get_value(key, expected):
    test_lines = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i",
    ]

    graph = Graph(test_lines)
    assert expected == graph.get_value(key)


@pytest.mark.parametrize(
    ["op", "expected"],
    [
        ("is NOT", True),
        ("is AND", True),
        ("is OR", True),
        ("is LSHIFT", True),
        ("is RSHIFT", True),
        ("is XOR", False),
    ],
)
def test_is_operation(op, expected):
    assert expected == is_operation(op)


@pytest.mark.parametrize(
    ["value", "expected"],
    [
        (0b1111111100000000, 0b0000000011111111),
        (0b1010101010101010, 0b0101010101010101),
    ],
)
def test_do_not(value, expected):
    assert expected == do_not(value)


@pytest.mark.parametrize(
    ["left", "right", "expected"],
    [
        (0b1111111100000000, 0b0000000011111111, 0b1111111111111111),
        (0b1010101010101010, 0b0101010101010101, 0b1111111111111111),
        (0b1111111100000000, 0b0000000000000000, 0b1111111100000000),
    ],
)
def test_do_or(left, right, expected):
    assert expected == do_or(left, right)


@pytest.mark.parametrize(
    ["left", "right", "expected"],
    [
        (0b1111111100000000, 0b0000000011111111, 0b0000000000000000),
        (0b1010101010101010, 0b0101010101010101, 0b0000000000000000),
        (0b1111111100000000, 0b0000000000000000, 0b0000000000000000),
        (0b1111111100000000, 0b1111111100000000, 0b1111111100000000),
        (0b1010100011111111, 0b0000000011111111, 0b0000000011111111),
    ],
)
def test_do_and(left, right, expected):
    assert expected == do_and(left, right)


@pytest.mark.parametrize(
    ["left", "right", "expected"],
    [
        (0b0000001111111111, 1, 0b0000011111111110),
        (0b0000001111111111, 2, 0b0000111111111100),
        (0b0000001111111111, 3, 0b0001111111111000),
    ],
)
def test_do_lshift(left, right, expected):
    assert expected == do_lshift(left, right)


@pytest.mark.parametrize(
    ["left", "right", "expected"],
    [
        (0b0000001111111111, 1, 0b0000000111111111),
        (0b0000001111111111, 2, 0b0000000011111111),
        (0b0000001111111111, 3, 0b0000000001111111),
    ],
)
def test_do_rshift(left, right, expected):
    assert expected == do_rshift(left, right)
