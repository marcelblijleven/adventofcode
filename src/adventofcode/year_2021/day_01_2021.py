import queue
from collections import deque
from typing import List, Optional

from adventofcode.util.exceptions import SolutionNotFoundException
from adventofcode.util.helpers import solution_timer
from adventofcode.util.input_helpers import get_input_for_day


def sonar_sweep(measurements: List[int]) -> int:
    previous: Optional[int] = None
    count = 0

    for measurement in measurements:
        if previous is not None and measurement > previous:
            count += 1

        previous = measurement

    return count


def count_increasing_windows(windows: List[List[int]]) -> int:
    previous: Optional[int] = None
    count = 0

    for window in windows:
        if previous is not None and sum(window) > previous:
            count += 1

        previous = sum(window)

    return count


def sonar_sweep_sliding_window(measurements: List[int]) -> int:
    windows: List[List[int]] = []
    window: deque[int] = deque(maxlen=3)

    for measurement in measurements:
        window.append(measurement)

        if len(window) == 3:
            windows.append(list(window))

    return count_increasing_windows(windows)


@solution_timer(2021, 1, 1)
def part_one(input_data: List[str]):
    answer = sonar_sweep(list(map(int, input_data)))

    if not answer:
        raise SolutionNotFoundException(2021, 1, 1)

    return answer


@solution_timer(2021, 1, 2)
def part_two(input_data: List[str]):
    answer = sonar_sweep_sliding_window(list(map(int, input_data)))

    if not answer:
        raise SolutionNotFoundException(2021, 1, 2)

    return answer


if __name__ == '__main__':
    data = get_input_for_day(2021, 1)
    part_one(data)
    part_two(data)
