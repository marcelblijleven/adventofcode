import pytest

from adventofcode.year_2021.day_18_2021 import (
    addition,
    calculate_magnitude,
    explode,
    get_pair_numbers,
    parse_snailfish_number,
    parse_snailfish_numbers,
    part_one,
    part_two,
    reduce_snailfish_number,
)

test_input = [
    "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
    "[[[5,[2,8]],4],[5,[[9,9],0]]]",
    "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
    "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
    "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
    "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
    "[[[[5,4],[7,7]],8],[[8,3],8]]",
    "[[9,3],[[9,9],[6,[4,9]]]]",
    "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
    "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
]


@pytest.mark.parametrize(
    ["number", "expected"],
    [
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
    ],
)
def test_explode(number, expected):
    assert explode(number) == (expected, True)


def test_get_pair_numbers():
    assert get_pair_numbers("[1,2]") == (1, 2)
    assert get_pair_numbers("[30,40]") == (30, 40)
    assert get_pair_numbers("[500,6]") == (500, 6)

    with pytest.raises(ValueError) as wrapped_e:
        get_pair_numbers("1,2")

    assert str(wrapped_e.value) == "invalid pair: 1,2"


def test_addition():
    snailfish_number = "[[[[4,3],4],4],[7,[[8,4],9]]]"
    to_add = "[1,1]"
    assert addition(snailfish_number, to_add) == "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"


@pytest.mark.parametrize(
    ["number", "expected"],
    [("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")],
)
def test_reduce_snailfish_number(number, expected):
    assert reduce_snailfish_number(number) == expected


def test_parse_snailfish_number():
    snailfish_number = "[[[[4,3],4],4],[7,[[8,4],9]]]"
    assert (
        parse_snailfish_number(snailfish_number, "[1,1]")
        == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
    )


@pytest.mark.parametrize(
    ["numbers", "expected"],
    [
        ("[1,1]\n[2,2]\n[3,3]\n[4,4]", "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
        ("[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]", "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
        ("[1,1]\n[2,2]\n[3,3]\n[4,4]\n[5,5]\n[6,6]", "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
        (
            "\n".join(
                [
                    "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
                    "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
                    "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
                    "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
                    "[7,[5,[[3,8],[1,4]]]]",
                    "[[2,[2,2]],[8,[8,1]]]",
                    "[2,9]",
                    "[1,[[[9,3],9],[[9,0],[0,7]]]]",
                    "[[[5,[7,4]],7],1]",
                    "[[[[4,2],2],6],[8,7]]",
                ]
            ),
            "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]",
        ),
    ],
)
def test_parse_snailfish_numbers(numbers, expected):
    assert parse_snailfish_numbers(numbers.split("\n")) == expected


@pytest.mark.parametrize(
    ["number", "expected"],
    [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ],
)
def test_calculate_magnitude(number, expected):
    assert calculate_magnitude(number) == expected


def test_part_one():
    assert part_one(test_input) == 4140


def test_part_two():
    assert part_two(test_input) == 3993
