import re
from types import MethodType
from typing import Callable


MONKEY_REGEX = re.compile(
    r"""Monkey (\d+):
  Starting items: ([\d\s,]+)
  Operation: new = old (\*|\+) (\d+|old)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)"""
)


class Monkey:
    def __init__(
        self,
        monkey_id,
        starting_items,
        operator,
        operand,
        test,
        next_true,
        next_false,
        worry_reduction,
    ):
        self.id = int(monkey_id)
        self.items = [int(item) for item in starting_items.split(", ")]
        self.analyzed_items = 0
        self.build_throw(
            operator, operand, test, next_true, next_false, worry_reduction
        )

    def build_throw(
        self, operator, operand, test, next_true, next_false, worry_reduction
    ):
        def throw_item(self, item: int, throw_to: int):
            match [operator, operand]:
                case ["+", "old"]:
                    operation = lambda old: old + old
                case ["*", "old"]:
                    operation = lambda old: old * old
                case ["+", int()]:
                    operation = lambda old: old + operand
                case ["*", int()]:
                    operation = lambda old: old * operand
                case _:
                    operation = None

            self.analyzed_items += 1
            new_item = operation(item) // worry_reduction
            if new_item % test == 0:
                throw_to(next_true, new_item)
            else:
                throw_to(next_false, new_item)

        self.throw_item = MethodType(throw_item, self)

    def throw_items(self, throw_to: Callable[[int, int], None]):
        while self.items:
            item = self.items.pop()
            self.throw_item(item, throw_to)

    def catch_item(self, item: int) -> None:
        self.items.append(item)


def monkey_business(input: str, rounds: int, worry_reduction: int) -> list[Monkey]:
    monkeys: list[Monkey] = []
    for monkey_config in input.split("\n\n"):
        (
            monkey_id,
            starting_items,
            operator,
            operand,
            test,
            next_true,
            next_false,
        ) = MONKEY_REGEX.search(monkey_config).groups()
        monkeys.append(
            Monkey(
                monkey_id,
                starting_items,
                operator,
                int(operand) if operand.isnumeric() else "old",
                int(test),
                int(next_true),
                int(next_false),
                worry_reduction,
            )
        )

    throw_to = lambda monkey_id, item: monkeys[monkey_id].catch_item(item)

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.throw_items(throw_to)
        for monkey in monkeys:
            print(
                f"Monkey {monkey.id} has items {', '.join([str(i) for i in monkey.items])}"
            )

    sorted_monkeys = sorted([monkey.analyzed_items for monkey in monkeys], reverse=True)

    return sorted_monkeys[0] * sorted_monkeys[1]


def part_1(input: str) -> int:
    return monkey_business(input, rounds=20, worry_reduction=3)


def part_2(input: str) -> int:
    # return monkey_business(input, rounds=10000, worry_reduction=1)
