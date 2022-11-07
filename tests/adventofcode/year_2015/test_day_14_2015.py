from adventofcode.year_2015.day_14_2015 import (
    check_leaderboard_and_assign_points,
    get_reindeer,
    race,
)

test_input = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
]


def test_check_leaderboard_and_assign_points():
    reindeer = get_reindeer(test_input)

    for racer in reindeer:
        racer.cycle_second()

    assert reindeer[0].points == 0
    assert reindeer[1].points == 0
    check_leaderboard_and_assign_points(reindeer)
    assert reindeer[0].points == 0
    assert reindeer[1].points == 1


def test_race():
    reindeer = get_reindeer(test_input)
    winner = race(reindeer, 1)
    assert winner.name == "Dancer"


def test_get_reindeer():
    reindeer = get_reindeer(test_input)
    assert len(reindeer) == 2
    assert reindeer[0].name == "Comet"
    assert reindeer[1].name == "Dancer"
