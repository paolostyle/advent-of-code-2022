import json
from functools import cmp_to_key
from typing import Literal


def is_order_right(left: list, right: list) -> Literal[-1, 0, 1]:
    left = list(left)
    right = list(right)
    i = 0

    while left:
        try:
            if type(left[i]) is type(right[i]):  # noqa: E721
                if isinstance(left[i], list):
                    result = is_order_right(left[i], right[i])
                    if result != 0:
                        return result
                elif isinstance(left[i], int):
                    if left[i] > right[i]:
                        return -1
                    elif left[i] < right[i]:
                        return 1
                i += 1
            else:
                if isinstance(left[i], int):
                    left[i] = [left[i]]
                elif isinstance(right[i], int):
                    right[i] = [right[i]]
        except IndexError:
            if len(left) > len(right):
                return -1
            elif len(left) < len(right):
                return 1
            else:
                return 0
    return 1


def part_1(input: str) -> int:
    correct_pairs = 0
    for idx, packets in enumerate(input.split("\n\n"), 1):
        left, right = [json.loads(packet) for packet in packets.splitlines()]
        if is_order_right(left, right) == 1:
            correct_pairs += idx
    return correct_pairs


def part_2(input: str) -> int:
    packets = [json.loads(packet) for packet in input.splitlines() if packet != ""]
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=cmp_to_key(is_order_right), reverse=True)
    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)
