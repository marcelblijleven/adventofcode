import os

import pytest
import pytest_mock

from adventofcode.config import ROOT_DIR
from adventofcode.util.module_helpers import (
    clean_day,
    clean_year,
    get_full_day_paths,
    get_full_module_from_day_file,
    get_full_year_paths,
    get_functions_from_day_file,
    year_dir_from_path,
)


def test_get_full_year_paths(mocker: pytest_mock.MockerFixture):
    mocker.patch("adventofcode.util.module_helpers.ROOT_DIR", "root_dir")
    mock_os_list_dir = mocker.patch("adventofcode.util.module_helpers.os.listdir")
    mock_os_list_dir.return_value = ["year_2015", "year_2020", "day_01"]
    assert ["root_dir/year_2015", "root_dir/year_2020"] == get_full_year_paths()


def test_get_full_day_paths(mocker: pytest_mock.MockerFixture):
    mock_os_list_dir = mocker.patch("adventofcode.util.module_helpers.os.listdir")
    mock_os_list_dir.return_value = ["day_02", "helper.py", "day_01"]
    assert ["year_2015/day_01", "year_2015/day_02"] == get_full_day_paths("year_2015")


def test_get_functions_from_day_file():
    template_file = os.path.join(ROOT_DIR, "scripts/templates/day_template.txt")

    assert ["part_one", "part_two"] == get_functions_from_day_file(template_file)


@pytest.mark.parametrize(
    ["path", "expected"],
    [
        ("/Users/marcelblijleven/project/year_2015", 2015),
        ("/Users/marcelblijleven/project/year_201", 201),
        ("/Users/marcelblijleven/project/year_20", 20),
        ("/Users/marcelblijleven/project/year_2", 2),
    ],
)
def test_clean_year(path, expected):
    assert expected == clean_year(path)


@pytest.mark.parametrize(
    ["path", "expected"],
    [
        ("/Users/marcelblijleven/project/year_2015/day_01_2015.py", 1),
        ("/Users/marcelblijleven/project/year_2015/day_02_2015.py", 2),
        ("/Users/marcelblijleven/project/year_2015/day_10_2015.py", 10),
        ("/Users/marcelblijleven/project/year_2015/day_25_2015.py", 25),
    ],
)
def test_clean_day(path, expected):
    assert expected == clean_day(path)


@pytest.mark.parametrize(
    ["path", "expected"],
    [
        ("/Users/marcelblijleven/project/year_2015", "year_2015"),
        ("/Users/marcelblijleven/project/A/year_2016", "year_2016"),
        ("/Users/marcelblijleven/project/A/B/year_2017", "year_2017"),
        ("/Users/marcelblijleven/project/A/B/C/year_2018", "year_2018"),
        ("/Users/marcelblijleven/project/year_2", "year_2"),
    ],
)
def test_year_dir_from_path(path, expected):
    assert expected == year_dir_from_path(path)


@pytest.mark.parametrize(
    ["path", "expected"],
    [
        (
            "/Users/marcelblijleven/project/year_2015/day_01_2015.py",
            "adventofcode.year_2015.day_01_2015",
        ),
        (
            "/Users/marcelblijleven/project/year_2016/day_02_2016.py",
            "adventofcode.year_2016.day_02_2016",
        ),
        (
            "/Users/marcelblijleven/project/year_2017/day_10_2017.py",
            "adventofcode.year_2017.day_10_2017",
        ),
        (
            "/Users/marcelblijleven/project/year_2018/day_25_2018.py",
            "adventofcode.year_2018.day_25_2018",
        ),
    ],
)
def test_get_full_module_from_day_file(expected, path):
    assert expected == get_full_module_from_day_file(path)
