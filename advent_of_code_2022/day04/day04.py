from typing import Callable


def to_range(range: str) -> tuple[int]:
    return tuple(map(int, range.split("-")))


def in_range(num: int, range: tuple[int]):
    range_start, range_end = range
    return range_start <= num <= range_end


def is_contained(range1, range2):
    range_start, range_end = range1
    return in_range(range_start, range2) and in_range(range_end, range2)


def is_overlapping(range1, range2):
    range_start, range_end = range1
    return in_range(range_start, range2) or in_range(range_end, range2)


def count_pairs(input: str, compare_fn: Callable) -> int:
    pairs = 0
    for line in input.splitlines():
        [range1, range2] = line.split(",")
        range1 = to_range(range1)
        range2 = to_range(range2)

        if compare_fn(range1, range2) or compare_fn(range2, range1):
            pairs += 1

    return pairs


def part_1(input: str) -> int:
    return count_pairs(input, is_contained)


def part_2(input: str) -> int:
    return count_pairs(input, is_overlapping)
