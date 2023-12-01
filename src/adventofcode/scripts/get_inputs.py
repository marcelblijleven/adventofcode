import os

from httpx import get

from adventofcode.config import ROOT_DIR


def get_input(year: int, day: int):
    session = _read_session()
    data = _download_input(year, day, session)
    _save_input(data, year, day)


def _download_input(year: int, day: int, session: str) -> bytes:
    """
    Downloads the input as text from the advent of code site
    """
    cookies = {"session": session}
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    resp = get(url, cookies=cookies)
    resp.raise_for_status()
    return resp.content  # type: ignore


def _save_input(data: bytes, year: int, day: int) -> None:
    inputs_path = os.path.join(ROOT_DIR, "inputs")

    if not os.path.exists(year_path := os.path.join(inputs_path, str(year))):
        os.mkdir(year_path)

    with open(os.path.join(year_path, f"day_{day:02}.txt"), "wb") as file:
        file.write(data)


def _read_session():
    target = os.path.join(ROOT_DIR, "../../.session")
    path = os.path.abspath(target)

    with open(path) as f:
        return f.read()
