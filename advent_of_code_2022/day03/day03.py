def get_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 64 + 26


def part_1(input: str) -> int:
    priorities = []
    for rucksack in input.splitlines():
        first_comp = set(rucksack[: len(rucksack) // 2])
        second_comp = set(rucksack[len(rucksack) // 2 :])
        common_items = first_comp.intersection(second_comp)
        priorities += [get_priority(item) for item in common_items]

    return sum(priorities)


def part_2(input: str) -> int:
    badge_priorities = []
    elves = input.splitlines()

    for i in range(0, len(elves), 3):
        group = [set(elf) for elf in elves[i : i + 3]]
        (common,) = set.intersection(*group)
        badge_priorities.append(get_priority(common))

    return sum(badge_priorities)
