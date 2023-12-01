from adventofcode.year_2020.day_16_2020 import (
    filter_tickets,
    get_departures,
    get_rules,
    parse_input,
    part_one,
    part_two,
)

test_input = [
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "",
    "your ticket:",
    "7,1,14",
    "",
    "nearby tickets:",
    "7,3,47",
    "40,4,50",
    "55,2,20",
    "38,6,12",
]

test_input_part_two = [
    "class: 0-1 or 4-19",
    "row: 0-5 or 8-19",
    "seat: 0-13 or 16-19",
    "",
    "your ticket:",
    "11,12,13",
    "",
    "nearby tickets:",
    "3,9,18",
    "15,1,5",
    "5,14,9",
]

rules_input = [
    "departure location: 37-594 or 615-952",
    "departure station: 50-562 or 573-968",
    "departure platform: 49-584 or 592-971",
    "departure track: 28-727 or 744-957",
    "departure date: 35-930 or 943-965",
    "departure time: 38-811 or 829-962",
    "arrival location: 35-446 or 467-950",
    "arrival station: 29-234 or 245-969",
    "arrival platform: 47-416 or 431-970",
    "arrival track: 38-134 or 160-962",
    "class: 30-493 or 506-953",
    "duration: 43-335 or 346-949",
    "price: 33-635 or 654-953",
    "route: 43-399 or 410-974",
    "row: 32-848 or 854-951",
    "seat: 36-777 or 788-965",
    "train: 35-109 or 122-969",
    "type: 38-673 or 694-960",
    "wagon: 50-168 or 193-971",
    "zone: 46-215 or 232-954",
]

rules_output = {
    "departure location": [37, 594, 615, 952],
    "departure station": [50, 562, 573, 968],
    "departure platform": [49, 584, 592, 971],
    "departure track": [28, 727, 744, 957],
    "departure date": [35, 930, 943, 965],
    "departure time": [38, 811, 829, 962],
    "arrival location": [35, 446, 467, 950],
    "arrival station": [29, 234, 245, 969],
    "arrival platform": [47, 416, 431, 970],
    "arrival track": [38, 134, 160, 962],
    "class": [30, 493, 506, 953],
    "duration": [43, 335, 346, 949],
    "price": [33, 635, 654, 953],
    "route": [43, 399, 410, 974],
    "row": [32, 848, 854, 951],
    "seat": [36, 777, 788, 965],
    "train": [35, 109, 122, 969],
    "type": [38, 673, 694, 960],
    "wagon": [50, 168, 193, 971],
    "zone": [46, 215, 232, 954],
}


def test_parse_input():
    assert parse_input("\n".join(test_input)) == (
        {"class": [1, 3, 5, 7], "row": [6, 11, 33, 44], "seat": [13, 40, 45, 50]},
        [7, 1, 14],
        [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]],
    )


def test_get_rules():
    assert get_rules(rules_input) == rules_output


def test_filter_tickets():
    rules, _, tickets = parse_input("\n".join(test_input))
    assert len(tickets) == 4
    assert len(filter_tickets(tickets, rules)) == 1


def test_get_departures():
    assert get_departures("\n".join(test_input_part_two), test=True) == 11 * 12 * 13


def test_part_one():
    assert part_one(test_input) == 71


def test_part_two():
    assert part_two(test_input) == 1
