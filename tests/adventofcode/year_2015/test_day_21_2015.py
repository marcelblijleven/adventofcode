import pytest

from adventofcode.year_2015.day_21_2015 import (
    Armor,
    Character,
    Ring,
    Weapon,
    get_boss,
    get_damage,
    get_shop_inventory,
    part_one,
)

test_input = [
    "Hit Points: 100",
    "Damage: 8",
    "Armor: 2",
]


def test_get_boss():
    assert get_boss(test_input) == Character(health=100, armor=2, damage=8)


@pytest.mark.parametrize(
    ["attacker", "defender", "expected"],
    [
        (
            Character(health=100, damage=10, armor=10),
            Character(health=100, damage=10, armor=10),
            1,
        ),
        (
            Character(health=100, damage=100, armor=10),
            Character(health=100, damage=10, armor=10),
            90,
        ),
        (
            Character(health=100, damage=10, armor=10),
            Character(health=100, damage=10, armor=100),
            1,
        ),
    ],
)
def test_get_damage(attacker, defender, expected):
    assert get_damage(attacker, defender) == expected


def test_get_shop_inventory():
    weapons = [
        Weapon(name="Dagger", cost=8, damage=4, armor=0),
        Weapon(name="Shortsword", cost=10, damage=5, armor=0),
        Weapon(name="Warhammer", cost=25, damage=6, armor=0),
        Weapon(name="Longsword", cost=40, damage=7, armor=0),
        Weapon(name="Greataxe", cost=74, damage=8, armor=0),
    ]

    armor = [
        Armor(name="Leather", cost=13, damage=0, armor=1),
        Armor(name="Chainmail", cost=31, damage=0, armor=2),
        Armor(name="Splintmail", cost=53, damage=0, armor=3),
        Armor(name="Bandedmail", cost=75, damage=0, armor=4),
        Armor(name="Platemail", cost=102, damage=0, armor=5),
        Armor(name="Naked", cost=0, damage=0, armor=0),
    ]

    rings = [
        Ring(name="Damage +1", cost=25, damage=1, armor=0),
        Ring(name="Damage +2", cost=50, damage=2, armor=0),
        Ring(name="Damage +3", cost=100, damage=3, armor=0),
        Ring(name="Defense +1", cost=20, damage=0, armor=1),
        Ring(name="Defense +2", cost=40, damage=0, armor=2),
        Ring(name="Defense +3", cost=80, damage=0, armor=3),
        Ring(name="No jewelry", cost=0, damage=0, armor=0),
        Ring(name="No jewelry", cost=0, damage=0, armor=0),
    ]

    assert get_shop_inventory() == (weapons, armor, rings)


def test_part_one():
    assert part_one(test_input) == 91
