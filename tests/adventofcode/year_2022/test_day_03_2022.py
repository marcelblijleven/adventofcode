from adventofcode.year_2022.day_03_2022 import compare_rucksacks, part_two, part_one, split_rucksack, compare_compartments, rucksacks_part_one

test_input = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]


def test_split_rucksack():
    assert split_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp') == ('vJrwpWtwJgWr', 'hcsFMMfFFhFp')
    assert split_rucksack('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL') == ('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL')


def test_compare_compartments():
    assert compare_compartments('vJrwpWtwJgWr', 'hcsFMMfFFhFp') == 'p'
    assert compare_compartments('jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL') == 'L'


def test_rucksacks_part_one():
    assert rucksacks_part_one(test_input) == 157


def test_compare_rucksacks():
    assert compare_rucksacks('abc', 'cde', 'fgc') == 'c'


def test_part_one():
    assert part_one(test_input) == 157


def test_part_two():
    assert part_two(test_input) == 70
