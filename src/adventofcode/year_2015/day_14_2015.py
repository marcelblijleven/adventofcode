import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

PATTERN = re.compile(r"(\w+)[^0-9]+(\d{1,2})[^0-9]+(\d{1,2})[^0-9]+(\d{2,3}).+")


class Reindeer:
    def __init__(self, name: str, speed: int, fly_duration: int, rest_duration: int):
        self.name = name
        self.speed = speed
        self.fly_duration = fly_duration
        self.rest_duration = rest_duration
        self._current_fly_count = fly_duration
        self._current_rest_count = 0
        self._distance_travelled: int = 0
        self._points: int = 0

    def __lt__(self, other):
        return self.distance_travelled < other.distance_travelled

    def __gt__(self, other):
        return self.distance_travelled > other.distance_travelled

    def __eq__(self, other):
        return self.distance_travelled == other.distance_travelled

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __str__(self):
        return (
            f"{self.name}. Speed: {self.speed} km/s, distance travelled: {self.distance_travelled}"
            f", points: {self.points}"
        )

    def __repr__(self):
        return str(self)

    @property
    def distance_travelled(self) -> int:
        return self._distance_travelled

    @property
    def can_fly(self) -> bool:
        return self._current_fly_count > 0

    @property
    def must_rest(self) -> bool:
        return self._current_rest_count > 0

    @property
    def points(self) -> int:
        return self._points

    def assign_point(self):
        self._points += 1

    def cycle_second(self):
        if self.can_fly:
            self._distance_travelled += self.speed
            self._current_fly_count -= 1

            if self._current_fly_count == 0:
                self._current_rest_count = self.rest_duration
        elif self.must_rest:
            self._current_rest_count -= 1

            if self._current_rest_count == 0:
                self._current_fly_count = self.fly_duration


def get_reindeer(input_data: list[str]) -> list[Reindeer]:
    reindeer: list[Reindeer] = []

    for line in input_data:
        if (matched := PATTERN.match(line)) and matched is not None:
            name, speed, fly_duration, rest_duration = matched.groups()
            reindeer.append(
                Reindeer(name, int(speed), int(fly_duration), int(rest_duration))
            )

    return reindeer


def check_leaderboard_and_assign_points(reindeer: list[Reindeer]):
    leader = sorted(reindeer, reverse=True)[0]
    tied_racers = [
        racer
        for racer in reindeer
        if racer.distance_travelled == leader.distance_travelled
    ]

    for racer in tied_racers:
        racer.assign_point()


def race(reindeer: list[Reindeer], race_duration: int) -> Reindeer:
    time_raced = 0

    while time_raced < race_duration:
        for racer in reindeer:
            racer.cycle_second()

        check_leaderboard_and_assign_points(reindeer)
        time_raced += 1

    winner = sorted(reindeer, reverse=True)[0]
    return winner


@register_solution(2015, 14, 1)
def part_one(input_data: list[str]):
    reindeer = get_reindeer(input_data)
    answer = race(reindeer, 2503)

    if not answer:
        raise SolutionNotFoundError(2015, 14, 1)

    return answer


@register_solution(2015, 14, 2)
def part_two(input_data: list[str]):
    reindeer = get_reindeer(input_data)
    _ = race(reindeer, 2503)
    answer = sorted(reindeer, key=lambda x: x.points, reverse=True)[0]

    if not answer:
        raise SolutionNotFoundError(2015, 14, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 14)
    part_one(data)
    part_two(data)
