from __future__ import annotations

import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

PATTERN = re.compile(r"(-?\d)")


class Ingredient:
    def __init__(
        self,
        name: str,
        capacity: int,
        durability: int,
        flavor: int,
        texture: int,
        calories: int,
    ):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
        self._quantity = 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.name}: capacity: {self.capacity}, durability: {self.durability}, flavor: {self.flavor}, texture: {self.texture}"  # noqa

    @property
    def quantity(self) -> int:
        return self._quantity

    def set_quantity(self, quantity: int) -> Ingredient:
        self._quantity = quantity
        return self

    def get_capacity(self) -> int:
        return self.capacity * self.quantity

    def get_durability(self) -> int:
        return self.durability * self.quantity

    def get_flavor(self) -> int:
        return self.flavor * self.quantity

    def get_texture(self) -> int:
        return self.texture * self.quantity

    def get_calories(self) -> int:
        return self.calories * self.quantity


class Cookie:
    def __init__(self, ingredients: list[Ingredient]):
        self.ingredients = ingredients

    @property
    def calories(self) -> int:
        return sum([ingredient.get_calories() for ingredient in self.ingredients])

    @property
    def score(self) -> int:
        capacity = sum([ingredient.get_capacity() for ingredient in self.ingredients])
        durability = sum(
            [ingredient.get_durability() for ingredient in self.ingredients]
        )
        flavor = sum([ingredient.get_flavor() for ingredient in self.ingredients])
        texture = sum([ingredient.get_texture() for ingredient in self.ingredients])

        if capacity < 0:
            capacity = 0
        if durability < 0:
            durability = 0
        if flavor < 0:
            flavor = 0
        if texture < 0:
            texture = 0

        return capacity * durability * flavor * texture


def parse_ingredients(input_data: list[str]) -> list[Ingredient]:
    ingredients: list[Ingredient] = []

    for line in input_data:
        name, content = line.split(": ")
        capacity, durability, flavor, texture, calories = map(
            int, PATTERN.findall(content)
        )
        ingredient = Ingredient(name, capacity, durability, flavor, texture, calories)
        ingredients.append(ingredient)

    return ingredients


def find_highest_scoring_cookie(
    input_data: list[str], match_calories: bool = False
) -> int:
    highest_score = 0
    ingredients = parse_ingredients(input_data)
    max_ingredients = 100

    if len(ingredients) == 2:
        for a in range(max_ingredients):
            for _ in range(max_ingredients - a):
                _b = 100 - a
                ingredients[0].set_quantity(a)
                ingredients[1].set_quantity(_b)

                cookie = Cookie(ingredients)

                if match_calories and cookie.calories != 500:
                    continue

                if cookie.score > highest_score:
                    highest_score = cookie.score
    else:
        for a in range(max_ingredients):
            for b in range(max_ingredients - a):
                for c in range(max_ingredients - a - b):
                    d = max_ingredients - a - b - c
                    ingredients[0].set_quantity(a)
                    ingredients[1].set_quantity(b)
                    ingredients[2].set_quantity(c)
                    ingredients[3].set_quantity(d)
                    cookie = Cookie(ingredients)

                    if match_calories and cookie.calories != 500:
                        continue

                    if cookie.score > highest_score:
                        highest_score = cookie.score

    return highest_score


@register_solution(2015, 15, 1)
def part_one(input_data: list[str]):
    answer = find_highest_scoring_cookie(input_data)

    if not answer:
        raise SolutionNotFoundError(2015, 15, 1)

    return answer


@register_solution(2015, 15, 2)
def part_two(input_data: list[str]):
    answer = find_highest_scoring_cookie(input_data, match_calories=True)

    if not answer:
        raise SolutionNotFoundError(2015, 15, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2015, 15)
    part_one(data)
    part_two(data)
