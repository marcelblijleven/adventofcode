import dataclasses
import itertools

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


@dataclasses.dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


class Weapon(Item):
    pass


class Armor(Item):
    pass


class Ring(Item):
    pass


@dataclasses.dataclass
class Character:
    health: int
    damage: int
    armor: int


def get_shop_inventory():
    dagger = Weapon("Dagger", 8, 4, 0)
    shortsword = Weapon("Shortsword", 10, 5, 0)
    warhammer = Weapon("Warhammer", 25, 6, 0)
    longsword = Weapon("Longsword", 40, 7, 0)
    greataxe = Weapon("Greataxe", 74, 8, 0)
    # empty_hand = Weapon('Empty', 0, 0, 0)
    weapons = [dagger, shortsword, warhammer, longsword, greataxe]

    leather = Armor("Leather", 13, 0, 1)
    chainmail = Armor("Chainmail", 31, 0, 2)
    splintmail = Armor("Splintmail", 53, 0, 3)
    bandedmail = Armor("Bandedmail", 75, 0, 4)
    platemail = Armor("Platemail", 102, 0, 5)
    naked = Armor("Naked", 0, 0, 0)
    armor = [leather, chainmail, splintmail, bandedmail, platemail, naked]

    damage_1 = Ring("Damage +1", 25, 1, 0)
    damage_2 = Ring("Damage +2", 50, 2, 0)
    damage_3 = Ring("Damage +3", 100, 3, 0)
    defense_1 = Ring("Defense +1", 20, 0, 1)
    defense_2 = Ring("Defense +2", 40, 0, 2)
    defense_3 = Ring("Defense +3", 80, 0, 3)
    no_jewelry = Ring("No jewelry", 0, 0, 0)
    no_jewelry2 = Ring("No jewelry", 0, 0, 0)
    rings = [
        damage_1,
        damage_2,
        damage_3,
        defense_1,
        defense_2,
        defense_3,
        no_jewelry,
        no_jewelry2,
    ]

    return weapons, armor, rings


def calculate_cost(boss: Character):
    weapons, armor, rings = get_shop_inventory()

    wins: list[int] = []
    losses: list[int] = []
    max_cost: int = 0

    for weapon in weapons:
        # only one weapon
        for armor_item in armor:
            # only one armor
            for ring_one, ring_two in itertools.combinations(rings, 2):
                # two rings
                total_cost = (
                    weapon.cost + armor_item.cost + ring_one.cost + ring_two.cost
                )
                total_damage = (
                    weapon.damage
                    + armor_item.damage
                    + ring_one.damage
                    + ring_two.damage
                )
                total_armor = (
                    weapon.armor + armor_item.armor + ring_one.armor + ring_two.armor
                )

                player = Character(health=100, damage=total_damage, armor=total_armor)

                if fight(player, boss):
                    wins.append(total_cost)
                else:
                    losses.append(total_cost)
                    max_cost = max(total_cost, max_cost)

    return min(wins), max(losses)


def get_damage(attacker: Character, defender: Character) -> int:
    hit_points = attacker.damage - defender.armor

    if hit_points <= 0:
        return 1

    return hit_points


def get_boss(input_data: list[str]) -> Character:
    health = int(input_data[0].split(": ")[1])
    damage = int(input_data[1].split(": ")[1])
    armor = int(input_data[2].split(": ")[1])
    return Character(health, damage, armor)


def fight(player: Character, boss: Character) -> bool:
    player_health = player.health
    boss_health = player.health

    while True:
        # Player goes first
        boss_health -= get_damage(player, boss)

        if boss_health <= 0:
            return True

        # Boss is next
        player_health -= get_damage(boss, player)

        if player_health <= 0:
            return False


@register_solution(2015, 21, 1)
def part_one(input_data: list[str]):
    boss = get_boss(input_data)
    answer, _ = calculate_cost(boss)

    if not answer:
        raise SolutionNotFoundError(2015, 21, 1)

    return answer


# Solution isn't correct for part 2
@register_solution(2015, 21, 2)
def part_two(input_data: list[str]):
    boss = get_boss(input_data)
    _, answer = calculate_cost(boss)

    if not answer:
        raise SolutionNotFoundError(2015, 21, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 21)
    part_one(data)
    part_two(data)
