from typing import Callable

Range = tuple[int, ...]


def to_range(range: str) -> Range:
    return tuple(map(int, range.split("-")))


def is_in_range(num: int, range: Range) -> bool:
    range_start, range_end = range
    return range_start <= num <= range_end


def is_contained(range1: Range, range2: Range) -> bool:
    range_start, range_end = range1
    return is_in_range(range_start, range2) and is_in_range(range_end, range2)


def is_overlapping(range1: Range, range2: Range) -> bool:
    range_start, range_end = range1
    return is_in_range(range_start, range2) or is_in_range(range_end, range2)


def count_pairs(input: str, compare_fn: Callable[[Range, Range], bool]) -> int:
    pairs = 0
    for line in input.splitlines():
        ranges = line.split(",")
        range1 = to_range(ranges[0])
        range2 = to_range(ranges[1])

        if compare_fn(range1, range2) or compare_fn(range2, range1):
            pairs += 1

    return pairs


def part_1(input: str) -> int:
    return count_pairs(input, is_contained)


def part_2(input: str) -> int:
    return count_pairs(input, is_overlapping)
