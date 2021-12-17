import io

import pytest
import pytest_mock

from adventofcode.year_2021.day_16_2021 import part_one, input_to_binary_string, \
    read_type_four_packet, input_to_binary_string_faster, read_operator_packet, read_outer_packet


@pytest.mark.parametrize(['hex_string', 'expected'], [
    ('0', '0000'),
    ('1', '0001'),
    ('2', '0010'),
    ('3', '0011'),
    ('4', '0100'),
    ('5', '0101'),
    ('6', '0110'),
    ('7', '0111'),
    ('8', '1000'),
    ('9', '1001'),
    ('A', '1010'),
    ('B', '1011'),
    ('C', '1100'),
    ('D', '1101'),
    ('E', '1110'),
    ('F', '1111'),
    ('D2FE28', '110100101111111000101000'),
    ('EE00D40C823060', '11101110000000001101010000001100100000100011000001100000'),
    ('38006F45291200', '00111000000000000110111101000101001010010001001000000000')
])
def test_input_to_binary_string(hex_string, expected):
    assert input_to_binary_string(hex_string) == expected


@pytest.mark.parametrize(['hex_string', 'expected'], [
    ('0', '0000'),
    ('1', '0001'),
    ('2', '0010'),
    ('3', '0011'),
    ('4', '0100'),
    ('5', '0101'),
    ('6', '0110'),
    ('7', '0111'),
    ('8', '1000'),
    ('9', '1001'),
    ('A', '1010'),
    ('B', '1011'),
    ('C', '1100'),
    ('D', '1101'),
    ('E', '1110'),
    ('F', '1111'),
    ('D2FE28', '110100101111111000101000'),
    ('EE00D40C823060', '11101110000000001101010000001100100000100011000001100000'),
    ('38006F45291200', '00111000000000000110111101000101001010010001001000000000')
])
def test_input_to_binary_string_two(hex_string, expected):
    assert input_to_binary_string_faster(hex_string) == expected


def test_read_type_four_packet():
    buffer = io.StringIO('110100101111111000101000')
    assert read_type_four_packet(buffer) == 2021


def test_read_operator_packet(mocker: pytest_mock.MockerFixture):
    hex_string = '00111000000000000110111101000101001010010001001000000000'
    buffer = io.StringIO(hex_string)

    type_four = mocker.patch('adventofcode.year_2021.day_16_2021.read_type_four_packet')
    type_four.side_effect = read_type_four_packet

    read_operator_packet(buffer)
    assert type_four.call_count == 2


@pytest.mark.parametrize(['transmission', 'expected'], [
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31),
])
def test_read_outer_packet(transmission, expected):
    hex_string = transmission
    bin_string = input_to_binary_string(hex_string)
    buffer = io.StringIO(bin_string)
    assert read_outer_packet(buffer) == expected


@pytest.mark.parametrize(['transmission', 'expected'], [
    ('8A004A801A8002F478', 16),
    ('620080001611562C8802118E34', 12),
    ('C0015000016115A2E0802F182340', 23),
    ('A0016C880162017C3686B18A3D4780', 31),
])
def test_part_one(transmission, expected):
    assert part_one([transmission]) == expected

# def test_part_two():
#     assert part_two(test_input) == 'x'
