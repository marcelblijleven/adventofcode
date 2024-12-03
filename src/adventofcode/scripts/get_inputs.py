import json
import os
from typing import Required, TypedDict

from httpx import get

from adventofcode.config import ROOT_DIR


class Setup(TypedDict):
    user_agent: Required[str]
    session_cookie: Required[str]


def get_input(year: int, day: int):
    """
    Retrieves input from the Advent of Code website for the given year/day.
    After retrieving the input, the input is stored in the project.
    """
    setup = _read_setup()
    data = _download_input(year, day, setup)
    _save_input(data, year, day)


def _download_input(year: int, day: int, setup: Setup) -> bytes:
    """
    Downloads the input as text from the advent of code site
    """
    cookies = {"session": setup["session_cookie"]}
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    resp = get(url, cookies=cookies, headers={"User-Agent": setup["user_agent"]})
    resp.raise_for_status()
    return resp.content


def _save_input(data: bytes, year: int, day: int) -> None:
    inputs_path = os.path.join(ROOT_DIR, "inputs")

    if not os.path.exists(year_path := os.path.join(inputs_path, str(year))):
        os.mkdir(year_path)

    with open(os.path.join(year_path, f"day_{day:02}.txt"), "wb") as file:
        file.write(data)


def _read_setup() -> Setup:
    """
    Reads .setup.json from the projects' root directory

    Returns:
        Setup: a typed dict
    """
    target = os.path.join(ROOT_DIR, "../../.setup.json")
    path = os.path.abspath(target)

    with open(path) as f:
        return json.load(f)
