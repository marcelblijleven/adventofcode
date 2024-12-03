from __future__ import annotations

import dataclasses
from collections.abc import Callable
from copy import deepcopy

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.helpers import memoize
from adventofcode.util.input_helpers import get_input_for_day

"""
Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active,
it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active,
it gives you 101 new mana.
"""


@dataclasses.dataclass
class Spell:
    name: str
    cost: int
    damage: int
    health: int
    shield: int
    mana: int
    duration: int

    def __key(self):
        return (
            self.name,
            self.cost,
            self.damage,
            self.health,
            self.shield,
            self.mana,
            self.duration,
        )

    def __eq__(self, other):
        if not isinstance(other, Spell):
            raise NotImplementedError()

        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())


missile = Spell("magic missile", 53, 4, 0, 0, 0, 0)
drain = Spell("drain", 73, 2, 2, 0, 0, 0)
shield = Spell("shield", 113, 0, 0, 7, 0, 6)
poison = Spell("poison", 173, 3, 0, 0, 0, 6)
recharge = Spell("recharge", 229, 0, 0, 0, 101, 5)
spells = [missile, drain, shield, poison, recharge]


def apply_status_effects(
    status_effects: tuple[Spell, ...],
    boss_health: int,
    player_health: int,
    player_armor: int,
    player_mana: int,
) -> tuple[tuple[Spell, ...], int, int, int, int]:
    next_effects: tuple[Spell, ...] = ()
    for effect in status_effects:
        if effect.duration >= 0:
            boss_health -= effect.damage
            player_health += effect.health
            player_armor += effect.shield
            player_mana += effect.mana

        new_effect = Spell(
            effect.name,
            effect.cost,
            effect.damage,
            effect.health,
            effect.shield,
            effect.mana,
            effect.duration - 1,
        )

        if new_effect.duration > 0:
            next_effects = (*next_effects, new_effect)

    return next_effects, boss_health, player_health, player_armor, player_mana


def do_player_turn(
    next_effects: tuple[Spell, ...],
    boss_health: int,
    player_health: int,
    player_mana: int,
    mana_spent: int,
    simulation_func: Callable[[int, int, int, tuple[Spell, ...], bool, int], bool],
):
    for spell in spells:
        if spell.name in [effect.name for effect in next_effects]:
            continue

        if spell.cost > player_mana:
            continue

        copied_effects = deepcopy(next_effects)
        copied_effects = (*copied_effects, spell)

        simulation_func(
            boss_health,
            player_health,
            player_mana - spell.cost,
            tuple(copied_effects),
            False,
            mana_spent + spell.cost,
        )


def fight(
    player_starting_health: int,
    player_starting_mana: int,
    boss_starting_health: int,
    boss_damage: int,
    hard_mode: bool = False,
) -> int:
    minimum_mana = int(1e10)

    @memoize
    def run_simulation(
        boss_health,
        player_health,
        player_mana,
        status_effects: tuple[Spell],
        is_player_turn,
        mana_spent,
    ):
        nonlocal boss_damage
        player_armor = 0

        if hard_mode and is_player_turn:
            player_health -= 1
            if player_health <= 0:
                return False

        status_result = apply_status_effects(
            status_effects, boss_health, player_health, player_armor, player_mana
        )
        (
            next_effects,
            boss_health,
            player_health,
            player_armor,
            player_mana,
        ) = status_result

        nonlocal minimum_mana
        if boss_health <= 0:
            minimum_mana = min(minimum_mana, mana_spent)
            return True

        if mana_spent >= minimum_mana:
            return False

        if is_player_turn:
            do_player_turn(
                next_effects,
                boss_health,
                player_health,
                player_mana,
                mana_spent,
                run_simulation,
            )
        else:
            player_health += (
                player_armor - boss_damage if player_armor - boss_damage < 0 else -1
            )
            if player_health > 0:
                run_simulation(
                    boss_health,
                    player_health,
                    player_mana,
                    tuple(next_effects),
                    True,
                    mana_spent,
                )

    run_simulation(
        boss_starting_health, player_starting_health, player_starting_mana, (), True, 0
    )

    return minimum_mana


@register_solution(2015, 22, 1)
def part_one(_: list[str]):
    answer = fight(50, 500, 58, 9, False)

    if not answer:
        raise SolutionNotFoundError(2015, 22, 1)

    return answer


@register_solution(2015, 22, 2)
def part_two(_: list[str]):
    answer = fight(50, 500, 58, 9, True)

    if not answer:
        raise SolutionNotFoundError(2015, 22, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 22)
    part_one(data)
    part_two(data)
