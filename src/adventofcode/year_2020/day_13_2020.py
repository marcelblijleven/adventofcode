from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

DepartureTimes = dict[int, list[int]]


def parse_input(input_data: list[str]) -> tuple[int, list[int]]:
    timestamp = int(input_data[0])
    busses = list(
        map(int, [value for value in input_data[1].split(",") if value.isdigit()])
    )
    return timestamp, busses


def get_departure_times(timestamp: int, busses: list[int]) -> DepartureTimes:
    departure_times: DepartureTimes = {}

    for bus in busses:
        departure_times[bus] = []

    while not all([len(value) for value in departure_times.values()]):  # noqa
        for bus in busses:
            if timestamp % bus == 0:
                departure_times[bus].append(timestamp)

        timestamp += 1

    return departure_times


def get_sequential_departure_times(bus_schedule: str):
    timestamp = 1
    index = 0

    for idx, bus in [
        (idx, bus) for idx, bus in enumerate(bus_schedule.split(",")) if bus.isdigit()
    ]:
        while True:
            index += timestamp

            if (index + idx) % int(bus) == 0:
                timestamp = timestamp * int(bus)
                break

    return index


def get_answer_part_one(arrival: int, departure_times: DepartureTimes) -> int:
    bus_id, wait_time = get_earliest_bus(arrival, departure_times)
    return bus_id * wait_time


def get_earliest_bus(arrival: int, departure_times: DepartureTimes) -> tuple[int, int]:
    min_wait_time = int(1e10)
    bus_id = 0

    for bus, times in departure_times.items():
        wait_time = times[0] - arrival
        min_wait_time = min(min_wait_time, wait_time)
        bus_id = bus if min_wait_time == wait_time else bus_id

    return bus_id, min_wait_time


@register_solution(2020, 13, 1)
def part_one(input_data: list[str]):
    timestamp, busses = parse_input(input_data)
    answer = get_answer_part_one(timestamp, get_departure_times(timestamp, busses))

    if not answer:
        raise SolutionNotFoundError(2020, 13, 1)

    return answer


@register_solution(2020, 13, 2)
def part_two(input_data: list[str]):
    schedule = input_data[1]
    answer = get_sequential_departure_times(schedule)

    if not answer:
        raise SolutionNotFoundError(2020, 13, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2020, 13)
    part_one(data)
    part_two(data)
