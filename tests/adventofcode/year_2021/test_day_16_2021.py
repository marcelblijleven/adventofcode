import io

import pytest
import pytest_mock

from adventofcode.year_2021.day_16_2021 import (
    input_to_binary_string,
    input_to_binary_string_faster,
    part_one,
    part_two,
    peek_version_and_type_id,
    peek_version_type_id_and_length_type,
    read_operator_packet,
    read_outer_packet,
    read_type_four_packet,
)


@pytest.mark.parametrize(
    ["hex_string", "expected"],
    [
        ("0", "0000"),
        ("1", "0001"),
        ("2", "0010"),
        ("3", "0011"),
        ("4", "0100"),
        ("5", "0101"),
        ("6", "0110"),
        ("7", "0111"),
        ("8", "1000"),
        ("9", "1001"),
        ("A", "1010"),
        ("B", "1011"),
        ("C", "1100"),
        ("D", "1101"),
        ("E", "1110"),
        ("F", "1111"),
        ("D2FE28", "110100101111111000101000"),
        ("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000"),
        ("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
        (
            "620080001611562C8802118E34",
            "01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100",
        ),
    ],
)
def test_input_to_binary_string(hex_string, expected):
    assert input_to_binary_string(hex_string) == expected


@pytest.mark.parametrize(
    ["hex_string", "expected"],
    [
        ("0", "0000"),
        ("1", "0001"),
        ("2", "0010"),
        ("3", "0011"),
        ("4", "0100"),
        ("5", "0101"),
        ("6", "0110"),
        ("7", "0111"),
        ("8", "1000"),
        ("9", "1001"),
        ("A", "1010"),
        ("B", "1011"),
        ("C", "1100"),
        ("D", "1101"),
        ("E", "1110"),
        ("F", "1111"),
        ("D2FE28", "110100101111111000101000"),
        ("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000"),
        ("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
        (
            "620080001611562C8802118E34",
            "01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100",
        ),
    ],
)
def test_input_to_binary_string_faster(hex_string, expected):
    assert input_to_binary_string_faster(hex_string) == expected


def test_peek_version_and_type_id():
    # version
    bin_string = ""
    with pytest.raises(ValueError) as wrapped_e:
        peek_version_and_type_id(io.StringIO(bin_string))

    assert str(wrapped_e.value) == "could not read version from buffer"

    # type id
    bin_string = "010"
    with pytest.raises(ValueError) as wrapped_e:
        peek_version_and_type_id(io.StringIO(bin_string))

    assert str(wrapped_e.value) == "could not read type id from buffer"


def test_peek_version_type_id_and_length_type():
    # version
    bin_string = ""
    with pytest.raises(ValueError) as wrapped_e:
        peek_version_type_id_and_length_type(io.StringIO(bin_string))

    assert str(wrapped_e.value) == "could not read version from buffer"

    # type id
    bin_string = "010"
    with pytest.raises(ValueError) as wrapped_e:
        peek_version_type_id_and_length_type(io.StringIO(bin_string))

    assert str(wrapped_e.value) == "could not read type id from buffer"

    # length
    bin_string = "010101"
    with pytest.raises(ValueError) as wrapped_e:
        peek_version_type_id_and_length_type(io.StringIO(bin_string))

    assert str(wrapped_e.value) == "could not read length type id from buffer"


def test_read_type_four_packet():
    buffer = io.StringIO("110100101111111000101000")
    assert read_type_four_packet(buffer) == 2021


def test_read_operator_packet(mocker: pytest_mock.MockerFixture):
    hex_string = "00111000000000000110111101000101001010010001001000000000"
    buffer = io.StringIO(hex_string)

    type_four = mocker.patch("adventofcode.year_2021.day_16_2021.read_type_four_packet")
    type_four.side_effect = read_type_four_packet

    _, value = read_operator_packet(buffer, 6)
    assert type_four.call_count == 2
    assert value == 1


@pytest.mark.parametrize(
    ["transmission", "expected"],
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_read_outer_packet(transmission, expected):
    hex_string = transmission
    bin_string = input_to_binary_string(hex_string)
    buffer = io.StringIO(bin_string)
    versions, value = read_outer_packet(buffer)
    assert sum(versions) == expected


@pytest.mark.parametrize(
    ["transmission", "expected"],
    [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_part_one(transmission, expected):
    assert part_one([transmission]) == expected


@pytest.mark.parametrize(
    ["transmission", "expected"],
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_part_two(transmission, expected):
    assert part_two([transmission]) == expected
