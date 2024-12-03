import pytest
import pytest_mock

from adventofcode.util import input_helpers
from adventofcode.util.input_helpers import (
    _get_input,
    _read_file,
    get_input_for_day,
    get_input_for_day_as_str,
)


def test_get_input_for_day(mocker: pytest_mock.MockerFixture):
    mock_get_input = mocker.patch("adventofcode.util.input_helpers._get_input")
    mock_get_input.return_value = ["c0ffee", "cafe"]

    original_root_dir = input_helpers.ROOT_DIR
    input_helpers.ROOT_DIR = "dir"

    data = get_input_for_day(2020, 1)
    assert ["c0ffee", "cafe"] == data
    mock_get_input.assert_called_with("dir/inputs/2020/day_01.txt")

    input_helpers.ROOT_DIR = original_root_dir


def test_get_input_for_day_as_str(mocker: pytest_mock.MockerFixture):
    mock_read_file = mocker.patch("adventofcode.util.input_helpers._read_file")
    mock_read_file.return_value = "c0ffee\ncafe"

    original_root_dir = input_helpers.ROOT_DIR
    input_helpers.ROOT_DIR = "dir"

    data = get_input_for_day_as_str(2020, 1)
    assert "c0ffee\ncafe" == data
    mock_read_file.assert_called_with("dir/inputs/2020/day_01.txt")

    input_helpers.ROOT_DIR = original_root_dir


@pytest.mark.skip()
def test__read_lines(): ...


def test__get_input(mocker: pytest_mock.MockerFixture):
    mock_read_lines = mocker.patch("adventofcode.util.input_helpers._read_lines")
    mock_read_lines.return_value = ["c0ffee\n", "cafe\n"]
    data = _get_input("testfile.text")
    assert ["c0ffee", "cafe"] == data


def test__read_file(mocker: pytest_mock.MockerFixture):
    mocker.patch("builtins.open", mocker.mock_open(read_data="test input"))
    content = _read_file("testfile.txt")
    assert "test input" == content
