import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]
Velocity = tuple[int, int]
TargetArea = tuple[int, int, int, int]


def get_target_area(input_data: list[str]) -> TargetArea:
    """
    Get the target area from the input data
    """
    found = re.findall(r"(-?\d+)", input_data[0])
    int_values = list(map(int, found))
    return (
        int_values[0],
        int_values[1],
        int_values[2],
        int_values[3],
    )


def calculate_new_velocity(velocity: Velocity) -> Velocity:
    """
    Calculate the velocity for the next step
    """
    x, y = velocity

    if x < 0:
        x += 1
    elif x > 0:
        x -= 1

    y -= 1
    return x, y


def apply_velocity(position: Position, velocity: Velocity) -> Position:
    """
    Applies the velocity to the position to calculate the next position
    """
    px, py = position
    vx, vy = velocity

    x = px + vx
    y = py + vy
    return x, y


def in_target(position: Position, target: TargetArea) -> bool:
    """
    Checks whether the position is in the target area
    """
    x, y = position
    min_x, max_x, min_y, max_y = target
    return min_x <= x <= max_x and min_y <= y <= max_y


def is_out_of_bounds(position: Position, target: TargetArea) -> bool:
    """
    Checks whether the current position is below or passed the target area
    """
    x, y = position
    min_x, max_x, min_y, max_y = target

    if y < min_y or x > max_x:
        return True

    return False


def is_overshot(position: Position, target: TargetArea) -> bool:
    """
    Checks if it overshot the target
    """
    x, y = position
    min_x, max_x, min_y, max_y = target

    return y <= max_y and x > max_x


def fire(velocity: Velocity, target: TargetArea) -> tuple[bool, int, bool]:
    """
    Fires the probe with the provided velocity.
    Returns True if the probe is in the target area, False if the probe is below the target.
    Second value in the returned tuple is the highest y point
    """
    position = 0, 0
    steps = 1
    max_y = 0

    while True:
        if is_out_of_bounds(position, target):
            break

        if is_overshot(position, target):
            return False, max_y, True

        position = apply_velocity(position, velocity)
        max_y = max(position[1], max_y)

        if in_target(position, target):
            return True, max_y, False

        velocity = calculate_new_velocity(velocity)
        steps += 1

    return False, max_y, False


def try_velocities(target: TargetArea, size: int = 100) -> tuple[int, int]:
    """
    Try all initial velocities and return the highest y and hit count
    """
    max_y = 0
    hits: list[bool] = []

    for vy in range(-1000, size):
        for vx in range(size):
            hit, y, overshot = fire((vx, vy), target)

            if overshot:
                break

            hits.append(hit)

            if hit:
                max_y = max(y, max_y)

            vx += 1  # noqa

    return max_y, sum(hits)


@register_solution(2021, 17, 1, version="bruteforce")
def part_one(input_data: list[str]):
    target = get_target_area(input_data)
    max_y, _ = try_velocities(target, 73)
    answer = max_y

    if not answer:
        raise SolutionNotFoundError(2021, 17, 1)

    return answer


@register_solution(2021, 17, 1, version="quick maths")
def part_one_quick_maths(input_data: list[str]):
    """
    Learned about this solution after my bruteforce solution
    """
    target = get_target_area(input_data)
    answer = int(target[2] * (target[2] + 1) / 2)

    if not answer:
        raise SolutionNotFoundError(2021, 17, 1)

    return answer


@register_solution(2021, 17, 2)
def part_two(input_data: list[str]):
    target = get_target_area(input_data)
    _, hit_count = try_velocities(target, target[1] + 1)
    answer = hit_count

    if not answer:
        raise SolutionNotFoundError(2021, 17, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 17)
    part_one(data)
    part_one_quick_maths(data)
    part_two(data)
