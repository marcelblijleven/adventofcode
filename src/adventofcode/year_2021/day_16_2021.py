import io
import math

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

translation_dict: dict[str, str] = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
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

    if version == "":
        raise ValueError("could not read version from buffer")

    if type_id == "":
        raise ValueError("could not read type id from buffer")

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

    if version == "":
        raise ValueError("could not read version from buffer")

    if type_id == "":
        raise ValueError("could not read type id from buffer")

    if length_type_id == "":
        raise ValueError("could not read length type id from buffer")

    buffer.seek(position)
    return int(version, 2), int(type_id, 2), int(length_type_id, 2)


def input_to_binary_string(input_data: str) -> str:
    """
    Translates the provided (hex) input data to a string of 0 and 1
    """
    return input_data.translate(str.maketrans(translation_dict))  # type: ignore


def input_to_binary_string_faster(input_data: str) -> str:
    """
    Translates the provided (hex) input data to a binary string using the builtin bin method (without the 0b prefix).

    Using the builtin bin method strips leading zeroes ('0000' becomes '0') so zfill
    is needed to pad the string to a multiple of four as each hex character is four bits

    When the total length is less than four, zfill(4) is used to get a length of four. If the total length is more than
    four, but not a multiple of four, the total length becomes total length plus the remainder of total length % 4,
    making it a multiple of four.

    NOTE:
    if the remainder >= 2, it should zfill with the difference between 4 and the remainder,
    if it is less than 2, it should zfill with the remainder itself.

    Discovered this with 620080001611562C8802118E34 and 38006F45291200
    """
    value = bin(int(input_data, 16))[2:]

    if (len_value := len(value)) < 4:
        return value.zfill(4)

    remainder = len_value % 4

    if remainder >= 2:
        return value.zfill(len_value + (4 - remainder))
    else:
        return value.zfill(len_value + remainder)


def _process_type_ids_0123(type_id: int, values: list[int]) -> int:
    """
    Processes values with type id 0, 1, 2 or 3
    """
    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        return math.prod(values)
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)
    else:
        raise ValueError("type id does not equal 0, 1, 2 or 3")


def _process_type_ids_567(type_id: int, values: list[int]) -> int:
    """
    Processes values with type id 5, 6 or 7
    """
    if len(values) != 2:
        raise ValueError(f"values should have length of 2, got: {values}")

    if type_id == 5:
        return int(values[0] > values[1])
    elif type_id == 6:
        return int(values[0] < values[1])
    else:
        return int(values[0] == values[1])


def process_values(type_id: int, values: list[int]) -> int:
    """
    Retrieves the packet value by applying the type id of the parent operator packet to the list of values
    """
    if type_id in [0, 1, 2, 3]:
        return _process_type_ids_0123(type_id, values)
    elif type_id in [5, 6, 7]:
        return _process_type_ids_567(type_id, values)
    else:
        raise ValueError(f"unexpected type id received: {type_id}")


def read_outer_packet(buffer: io.StringIO) -> tuple[list[int], int]:
    """
    Reads the most outer packet and returns the sum of all versions in the packet and any sub-packet
    """
    versions: list[int] = []
    version = int(buffer.read(3), 2)
    type_id = int(buffer.read(3), 2)

    if type_id == 4:
        buffer.seek(buffer.tell() - 6)
        value = read_type_four_packet(buffer)
        return [version], value
    else:
        versions.append(version)
        length_type = int(buffer.read(1), 2)

        if length_type == 0:
            total_length = int(buffer.read(15), 2)
            packet_versions, packet_value = read_packets_until_length(
                buffer, total_length, type_id
            )
            versions += packet_versions
        else:
            number_of_packets = int(buffer.read(11), 2)
            packet_versions, packet_value = read_packets_until_all_read(
                buffer, number_of_packets, type_id
            )
            versions += packet_versions

    read_garbage_bits(buffer)
    return versions, packet_value


def read_packets_until_length(
    buffer: io.StringIO, total_length: int, parent_type_id: int
) -> tuple[list[int], int]:
    """
    Reads packets from the buffer until the total amount of bits read equals the total length parameter
    """
    versions: list[int] = []
    values: list[int] = []
    start_position = buffer.tell()

    while buffer.tell() - start_position < total_length:
        version, type_id, length_type_id = peek_version_type_id_and_length_type(buffer)

        if type_id == 4:
            versions.append(version)
            values.append(read_type_four_packet(buffer))
        else:
            packet_versions, packet_value = read_operator_packet(buffer, type_id)
            versions += packet_versions
            values.append(packet_value)

        if buffer.tell() - start_position > total_length:
            raise ValueError("read past total length of packet")

    value = process_values(parent_type_id, values)
    return versions, value


def read_packets_until_all_read(
    buffer: io.StringIO, number_of_packets: int, parent_type_id: int
) -> tuple[list[int], int]:
    """
    Reads packets from the buffer until the number of packets provided has been read
    """
    versions: list[int] = []
    values: list[int] = []
    packets_read = 0

    while packets_read < number_of_packets:
        version, type_id, length_type_id = peek_version_type_id_and_length_type(buffer)

        if type_id == 4:
            versions.append(version)
            value = read_type_four_packet(buffer)
            values.append(value)
        else:
            packet_versions, packet_value = read_operator_packet(buffer, type_id)
            versions += packet_versions
            values.append(packet_value)

        packets_read += 1

    value = process_values(parent_type_id, values)
    return versions, value


def read_type_four_packet(buffer: io.StringIO) -> int:
    """
    Reads type 4 packet and returns the literal value inside the packet groups
    """
    buffer.read(3)  # version
    buffer.read(3)  # type
    value = ""

    while True:
        group = buffer.read(5)
        value += group[1:]

        if group.startswith("0"):
            break

    return int(value, 2)


def read_operator_packet(
    buffer: io.StringIO, parent_type_id: int
) -> tuple[list[int], int]:
    """
    Determines the length type id for the packet and calls the correct operator packet
    reader.
    Returns a list of read versions
    """
    version = int(buffer.read(3), 2)
    type_id = int(buffer.read(3), 2)
    assert type_id == parent_type_id  # noqa
    length_type_id = int(buffer.read(1), 2)
    versions = [version]

    if length_type_id == 0:
        total_length = int(buffer.read(15), 2)
        packet_versions, packet_value = read_packets_until_length(
            buffer, total_length, parent_type_id
        )
    elif length_type_id == 1:
        total_packets = int(buffer.read(11), 2)
        packet_versions, packet_value = read_packets_until_all_read(
            buffer, total_packets, parent_type_id
        )
    else:
        raise ValueError(f'unexpected length type "{length_type_id}" received')

    versions += packet_versions

    return versions, packet_value


def read_garbage_bits(buffer: io.StringIO) -> None:
    """
    Removes any trailing zero bits
    """
    read_bits = buffer.tell()

    if read_bits % 4 > 0:
        buffer.read(4 - read_bits % 4)

    assert buffer.tell() % 4 == 0  # noqa


@register_solution(2021, 16, 1)
def part_one(input_data: list[str]):
    binary_string = input_to_binary_string(input_data[0])
    buffer = io.StringIO(binary_string)
    versions, _ = read_outer_packet(buffer)
    answer = sum(versions)

    if answer is None:
        raise SolutionNotFoundError(2021, 16, 1)

    return answer


@register_solution(2021, 16, 2)
def part_two(input_data: list[str]):
    binary_string = input_to_binary_string(input_data[0])
    buffer = io.StringIO(binary_string)
    _, value = read_outer_packet(buffer)
    answer = value

    if answer is None:
        raise SolutionNotFoundError(2021, 16, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 16)
    part_one(data)
    part_two(data)
