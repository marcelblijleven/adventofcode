from collections import deque

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def sonar_sweep(measurements: list[int]) -> int:
    previous: int | None = None
    count = 0

    for measurement in measurements:
        if previous is not None and measurement > previous:
            count += 1

        previous = measurement

    return count


def count_increasing_windows(windows: list[list[int]]) -> int:
    previous: int | None = None
    count = 0

    for window in windows:
        if previous is not None and sum(window) > previous:
            count += 1

        previous = sum(window)

    return count


def sonar_sweep_sliding_window(measurements: list[int]) -> int:
    windows: list[list[int]] = []
    window: deque[int] = deque(maxlen=3)

    for measurement in measurements:
        window.append(measurement)

        if len(window) == 3:
            windows.append(list(window))

    return count_increasing_windows(windows)


def sonar_sweep_sliding_window_reuse(measurements: list[int]) -> int:
    windows: list[list[int]] = []
    window: deque[int] = deque(maxlen=3)

    for measurement in measurements:
        window.append(measurement)

        if len(window) == 3:
            windows.append(list(window))

    return sonar_sweep(list(map(sum, windows)))  # type: ignore


@register_solution(2021, 1, 1)
def part_one(input_data: list[str]):
    answer = sonar_sweep(list(map(int, input_data)))

    if not answer:
        raise SolutionNotFoundError(2021, 1, 1)

    return answer


@register_solution(2021, 1, 2)
def part_two(input_data: list[str]):
    answer = sonar_sweep_sliding_window(list(map(int, input_data)))

    if not answer:
        raise SolutionNotFoundError(2021, 1, 2)

    return answer


@register_solution(2021, 1, 1, version="re-use part one")
def part_two_reuse_part_one(input_data: list[str]):
    answer = sonar_sweep_sliding_window_reuse(list(map(int, input_data)))

    if not answer:
        raise SolutionNotFoundError(2021, 1, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 1)
    part_one(data)
    part_two(data)
    part_two_reuse_part_one(data)
