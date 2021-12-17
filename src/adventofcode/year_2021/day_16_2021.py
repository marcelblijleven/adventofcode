import io
from typing import List

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day

translation_dict: dict[str, str] = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def peek(size: int, buffer: io.StringIO) -> str:
    """
    Reads the next x bits before resetting the position and returning the read value
    """
    position = buffer.tell()
    value = buffer.read(size)
    buffer.seek(position)
    return value


def peek_version_and_type_id(buffer: io.StringIO) -> tuple[int, int]:
    """
    Reads the version and type id from the buffer before returning to the original buffer position
    """
    position = buffer.tell()
    version = buffer.read(3)
    type_id = buffer.read(3)

    if version == '':
        raise ValueError('could not read version from buffer')

    if type_id == '':
        raise ValueError('could not read type id from buffer')

    buffer.seek(position)
    return int(version, 2), int(type_id, 2)


def peek_version_type_id_and_length_type(buffer: io.StringIO) -> tuple[int, int, int]:
    """
    Reads the version, type id and length type id before returning to the original buffer position
    """
    position = buffer.tell()
    version = buffer.read(3)
    type_id = buffer.read(3)
    length_type_id = buffer.read(1)

    if version == '':
        raise ValueError('could not read version from buffer')

    if type_id == '':
        raise ValueError('could not read type id from buffer')

    if length_type_id == '':
        raise ValueError('could not read length type id from buffer')

    buffer.seek(position)
    return int(version, 2), int(type_id, 2), int(length_type_id, 2)


def input_to_binary_string(input_data: str) -> str:
    """
    Translates the provided (hex) input data to a string of 0 and 1
    """
    return input_data.translate(str.maketrans(translation_dict))


def input_to_binary_string_faster(input_data: str) -> str:
    """
    Translates the provided (hex) input data to a binary string using the builtin bin method (without the 0b prefix).

    Using the builtin bin method strips leading zeroes ('0000' becomes '0') so zfill
    is needed to pad the string to a multiple of four as each hex character is four bits

    When the total length is less than four, zfill(4) is used to get a length of four. If the total length is more than
    four, but not a multiple of four, the total length becomes total length plus the remainder of total length % 4,
    making it a multiple of four.

    NOTE: This function is faster than using the translate table in function input_to_binary_string
    (0.02 vs 0.17ms with puzzle input), but results in incorrect value for 620080001611562C8802118E34
    """
    value = bin(int(input_data, 16))[2:]

    if (len_value := len(value)) < 4:
        return value.zfill(4)

    if (remainder := len_value % 4) != 0:
        return value.zfill(len_value + remainder)

    return value


def read_outer_packet(buffer: io.StringIO) -> int:
    """
    Reads the most outer packet and returns the sum of all versions in the packet and any sub-packet
    """
    versions: list[int] = []
    version = int(buffer.read(3), 2)
    type_id = int(buffer.read(3), 2)

    if type_id == 4:
        return version
    else:
        versions.append(version)
        length_type = int(buffer.read(1), 2)

        if length_type == 0:
            total_length = int(buffer.read(15), 2)
            versions += read_packets_until_length(buffer, total_length)
        else:
            number_of_packets = int(buffer.read(11), 2)
            versions += read_packets_until_all_read(buffer, number_of_packets)

    read_garbage_bits(buffer)
    return sum(versions)


def read_packets_until_length(buffer: io.StringIO, total_length: int) -> list[int]:
    """
    Reads packets from the buffer until the total amount of bits read equals the total length parameter
    """
    versions: list[int] = []
    start_position = buffer.tell()

    while buffer.tell() - start_position < total_length:
        version, type_id, length_type_id = peek_version_type_id_and_length_type(buffer)

        if type_id == 4:
            versions.append(version)
            value = read_type_four_packet(buffer)
        else:
            versions += read_operator_packet(buffer)

        if buffer.tell() - start_position > total_length:
            raise ValueError('read past total length of packet')

    return versions


def read_packets_until_all_read(buffer: io.StringIO, number_of_packets: int) -> list[int]:
    """
    Reads packets from the buffer until the number of packets provided has been read
    """
    versions: list[int] = []
    packets_read = 0

    while packets_read < number_of_packets:
        version, type_id, length_type_id = peek_version_type_id_and_length_type(buffer)

        if type_id == 4:
            versions.append(version)
            value = read_type_four_packet(buffer)
        else:
            versions += read_operator_packet(buffer)

        packets_read += 1

    return versions


def read_type_four_packet(buffer: io.StringIO) -> int:
    """
    Reads type 4 packet and returns the literal value inside the packet groups
    """
    buffer.read(3)  # version
    buffer.read(3)  # type
    value = ''

    while True:
        group = buffer.read(5)
        value += group[1:]

        if group.startswith('0'):
            break

    return int(value, 2)


def read_operator_packet(buffer: io.StringIO) -> list[int]:
    """
    Determines the length type id for the packet and calls the correct operator packet
    reader.
    Returns a list of read versions
    """
    version = int(buffer.read(3), 2)
    type_id = int(buffer.read(3), 2)
    length_type_id = int(buffer.read(1), 2)
    versions = [version]

    if length_type_id == 0:
        total_length = int(buffer.read(15), 2)
        versions += read_packets_until_length(buffer, total_length)
    elif length_type_id == 1:
        total_packets = int(buffer.read(11), 2)
        versions += read_packets_until_all_read(buffer, total_packets)
    else:
        raise ValueError(f'unexpected length type "{length_type_id}" received')

    return versions


def read_garbage_bits(buffer: io.StringIO) -> None:
    read_bits = buffer.tell()

    if read_bits % 4 > 0:
        buffer.read(4 - read_bits % 4)

    assert buffer.tell() % 4 == 0


@solution_timer(2021, 16, 1)
def part_one(input_data: List[str]):
    binary_string = input_to_binary_string(input_data[0])
    buffer = io.StringIO(binary_string)
    answer = read_outer_packet(buffer)

    if not answer:
        raise SolutionNotFoundException(2021, 16, 1)

    return answer


@solution_timer(2021, 16, 2)
def part_two(input_data: List[str]):
    answer = ...

    if not answer:
        raise SolutionNotFoundException(2021, 16, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 16)
    part_one(data)
    part_two(data)
