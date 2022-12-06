def find_distinct(input: str, length: int) -> int:
    for i in range(0, len(input)):
        if len(set(input[i : i + length])) == length:
            return i + length


def part_1(input: str) -> int:
    return find_distinct(input, 4)


def part_2(input: str) -> int:
    return find_distinct(input, 14)
