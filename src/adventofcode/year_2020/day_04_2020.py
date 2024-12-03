import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def get_passports(batch_file: str) -> list[dict[str, str]]:
    _data = batch_file.split("\n\n")
    passports: list[dict[str, str]] = []

    for value in _data:
        passports.append(get_passport_as_dict(value))

    return passports


def get_passport_as_dict(passport: str) -> dict[str, str]:
    values = {}

    for i in passport.split(" "):
        for j in i.split("\n"):
            key, value = j.split(":")
            values[key] = value

    return values


def validate_passport(passport: dict[str, str]) -> bool:
    keys = passport.keys()
    return len(keys) == 8 or (len(keys) == 7 and "cid" not in keys)


def _range_check(value: str, low: int, high: int) -> bool:
    try:
        return low <= int(value) <= high
    except ValueError:
        return False


def dob_check(value: str) -> bool:
    return _range_check(value, 1920, 2002)


def issue_check(value: str) -> bool:
    return _range_check(value, 2010, 2020)


def expiration_check(value: str) -> bool:
    return _range_check(value, 2020, 2030)


def height_check(value: str) -> bool:
    height = "".join([char for char in value if char.isdigit()])
    unit = "".join([char for char in value if char.isalpha()])
    return (unit == "cm" and _range_check(height, 150, 193)) or (
        unit == "in" and _range_check(height, 59, 76)
    )


def hair_color_check(value: str) -> bool:
    return re.compile(r"#[0-9a-f]{6}").match(value) is not None


def eye_color_check(value: str) -> bool:
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid_check(value):
    return re.compile(r"\d{9}$").match(value) is not None


def deep_validation(passport: dict[str, str]) -> bool:  # C901
    if not validate_passport(passport):
        return False

    checks = []

    for key, value in passport.items():
        if key == "byr":
            checks.append(dob_check(value))
        elif key == "iyr":
            checks.append(issue_check(value))
        elif key == "eyr":
            checks.append(expiration_check(value))
        elif key == "hgt":
            checks.append(height_check(value))
        elif key == "hcl":
            checks.append(hair_color_check(value))
        elif key == "ecl":
            checks.append(eye_color_check(value))
        elif key == "pid":
            checks.append(pid_check(value))
        elif key == "cid":
            checks.append(True)

    return all(checks)


@register_solution(2020, 4, 1)
def part_one(input_data: list[str]) -> int:
    passports = get_passports("\n".join(input_data))
    answer = len([passport for passport in passports if validate_passport(passport)])

    if not answer:
        raise SolutionNotFoundError(2020, 4, 1)

    return answer


@register_solution(2020, 4, 2)
def part_two(input_data: list[str]) -> int:
    passports = get_passports("\n".join(input_data))
    answer = len([passport for passport in passports if deep_validation(passport)])

    if not answer:
        raise SolutionNotFoundError(2020, 4, 1)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2020, 4)
    part_one(data)
    part_two(data)
