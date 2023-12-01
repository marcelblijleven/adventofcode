from adventofcode.year_2015.day_09_2015 import (
    get_all_cities,
    get_all_routes,
    get_fastest_route,
    get_slowest_route,
)

test_input = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141",
]


def test_get_all_cities():
    dist_dict = {}
    expected_dist_dict = {
        ("London", "Dublin"): 464,
        ("London", "Belfast"): 518,
        ("Dublin", "Belfast"): 141,
    }

    assert sorted(["London", "Dublin", "Belfast"]) == sorted(
        get_all_cities(test_input, dist_dict)
    )
    assert expected_dist_dict == dist_dict


def test_get_all_routes():
    cities = ["London", "Dublin", "Belfast"]
    expected = [
        ("London", "Dublin", "Belfast"),
        ("London", "Belfast", "Dublin"),
        ("Dublin", "London", "Belfast"),
        ("Dublin", "Belfast", "London"),
        ("Belfast", "London", "Dublin"),
        ("Belfast", "Dublin", "London"),
    ]

    assert expected == get_all_routes(cities)


def test_get_fastest_route():
    dist_dict = {
        ("London", "Dublin"): 464,
        ("London", "Belfast"): 518,
        ("Dublin", "Belfast"): 141,
    }

    routes = [
        ("London", "Dublin", "Belfast"),
        ("London", "Belfast", "Dublin"),
        ("Dublin", "London", "Belfast"),
        ("Dublin", "Belfast", "London"),
        ("Belfast", "London", "Dublin"),
        ("Belfast", "Dublin", "London"),
    ]

    assert 605 == get_fastest_route(routes, dist_dict)


def test_get_slowest_route():
    dist_dict = {
        ("London", "Dublin"): 464,
        ("London", "Belfast"): 518,
        ("Dublin", "Belfast"): 141,
    }

    routes = [
        ("London", "Dublin", "Belfast"),
        ("London", "Belfast", "Dublin"),
        ("Dublin", "London", "Belfast"),
        ("Dublin", "Belfast", "London"),
        ("Belfast", "London", "Dublin"),
        ("Belfast", "Dublin", "London"),
    ]

    assert 982 == get_slowest_route(routes, dist_dict)
