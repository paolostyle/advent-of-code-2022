import math
import re
from types import MethodType
from typing import Callable, Literal, Union


MONKEY_REGEX = re.compile(
    r"""Monkey (\d+):
  Starting items: ([\d\s,]+)
  Operation: new = old (\*|\+) (\d+|old)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""
)


class Monkey:
    def __init__(self, monkey_id: int, starting_items: str) -> None:
        self.id = int(monkey_id)
        self.items = [int(item) for item in starting_items.split(", ")]
        self.analyzed_items = 0

    def build_throw(
        self,
        operator: str,
        operand: Union[str, int],
        test: int,
        next_true: int,
        next_false: int,
        worry_reduction: int,
        test_values_product: int,
    ) -> None:
        def throw_item(self, item: int, throw_to: Callable[[int, int], None]):
            match [operator, operand]:
                case ["*", "old"]:
                    operation = lambda old: old * old
                case ["+", int()]:
                    operation = lambda old: old + operand
                case ["*", int()]:
                    operation = lambda old: old * operand

            self.analyzed_items += 1
            new_item = (operation(item) // worry_reduction) % test_values_product
            if new_item % test == 0:
                throw_to(next_true, new_item)
            else:
                throw_to(next_false, new_item)

        self.throw_item = MethodType(throw_item, self)

    def throw_items(self, throw_to: Callable[[int, int], None]) -> None:
        while self.items:
            item = self.items.pop()
            self.throw_item(item, throw_to)

    def catch_item(self, item: int) -> None:
        self.items.append(item)


def monkey_business(input: str, rounds: int, worry_reduction: int) -> int:
    monkey_configs = [
        MONKEY_REGEX.search(monkey_config).groups()  # type: ignore
        for monkey_config in input.split("\n\n")
    ]
    test_values_product = math.prod([int(monkey[4]) for monkey in monkey_configs])
    monkeys: list[Monkey] = []

    for monkey_config in monkey_configs:
        (
            monkey_id,
            starting_items,
            operator,
            operand,
            test,
            next_true,
            next_false,
        ) = monkey_config

        monkey = Monkey(int(monkey_id), starting_items)
        monkey.build_throw(
            operator=operator,
            operand=int(operand) if operand.isnumeric() else "old",
            test=int(test),
            next_true=int(next_true),
            next_false=int(next_false),
            worry_reduction=worry_reduction,
            test_values_product=test_values_product,
        )
        monkeys.append(monkey)

    throw_to = lambda monkey_id, item: monkeys[monkey_id].catch_item(item)

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.throw_items(throw_to)

    sorted_monkeys = sorted([monkey.analyzed_items for monkey in monkeys], reverse=True)

    return sorted_monkeys[0] * sorted_monkeys[1]


def part_1(input: str) -> int:
    return monkey_business(input, rounds=20, worry_reduction=3)


def part_2(input: str) -> int:
    return monkey_business(input, rounds=10000, worry_reduction=1)
