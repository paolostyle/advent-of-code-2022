def part_1(input: str):
    lines = input.splitlines()
    max_calories = 0
    current_calories = 0

    for line in lines:
        if line != "":
            current_calories += int(line)
        else:
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0

    return max_calories


def part_2(input: str):
    lines = input.splitlines()
    max_calories = [0, 0, 0]
    current_calories = 0

    for line in lines:
        if line != "":
            current_calories += int(line)
        else:
            smallest_max = min(max_calories)
            if current_calories > smallest_max:
                smallest_max_index = max_calories.index(smallest_max)
                max_calories[smallest_max_index] = current_calories
            current_calories = 0

    return sum(max_calories)
