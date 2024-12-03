import pytest

from adventofcode.year_2020.day_04_2020 import (
    dob_check,
    expiration_check,
    eye_color_check,
    hair_color_check,
    height_check,
    issue_check,
    part_one,
    part_two,
    pid_check,
)

test_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split("\n")


@pytest.mark.parametrize(
    ["dob", "expected"],
    [(1920, True), (2002, True), (1919, False), (2003, False), ("a", False)],
)
def test_dob_check(dob, expected):
    assert expected == dob_check(dob)


@pytest.mark.parametrize(
    ["issue", "expected"],
    [("2010", True), ("2020", True), ("2009", False), ("2021", False), ("a", False)],
)
def test_issue_check(issue, expected):
    assert expected == issue_check(issue)


@pytest.mark.parametrize(
    ["expiration", "expected"],
    [("2020", True), ("2030", True), ("2019", False), ("2031", False), ("a", False)],
)
def test_expiration_check(expiration, expected):
    assert expected == expiration_check(expiration)


@pytest.mark.parametrize(
    ["height", "expected"],
    [
        ("150cm", True),
        ("193cm", True),
        ("59in", True),
        ("76in", True),
        ("149cm", False),
        ("194cm", False),
        ("58in", False),
        ("77in", False),
        ("150db", False),
    ],
)
def test_height_check(height, expected):
    assert expected == height_check(height)


@pytest.mark.parametrize(
    ["hair_color", "expected"],
    [
        ("#c0ffee", True),
        ("#000000", True),
        (
            "#ababab",
            True,
        ),
        ("#fg0000", False),
        ("1234567", False),
    ],
)
def test_hair_color_check(hair_color, expected):
    assert expected == hair_color_check(hair_color)


@pytest.mark.parametrize(
    ["eye_color", "expected"],
    [
        ("amb", True),
        ("blu", True),
        ("brn", True),
        ("gry", True),
        ("grn", True),
        ("hzl", True),
        ("oth", True),
        ("abc", False),
    ],
)
def test_eye_color_check(eye_color, expected):
    assert expected == eye_color_check(eye_color)


@pytest.mark.parametrize(
    ["pid", "expected"],
    [
        ("000000001", True),
        ("123456789", True),
        ("12345678", False),
        ("1234567890", False),
        ("12345678a", False),
    ],
)
def test_pid_check(pid, expected):
    assert expected == pid_check(pid)


def test_part_one():
    assert 2 == part_one(test_input)


def test_part_two():
    assert 2 == part_two(test_input)
