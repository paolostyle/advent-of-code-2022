def part_1(input: str) -> int:
    shape_to_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    def get_result(game: str) -> int:
        [opponent_shape, my_shape] = game.split(" ")

        if opponent_shape == "A":
            result = {"X": 3, "Y": 6, "Z": 0}
        elif opponent_shape == "B":
            result = {"X": 0, "Y": 3, "Z": 6}
        elif opponent_shape == "C":
            result = {"X": 6, "Y": 0, "Z": 3}

        return shape_to_points[my_shape] + result[my_shape]

    return sum([get_result(game) for game in input.splitlines()])


def part_2(input: str) -> int:
    result_to_points = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    shape_to_points = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    def get_result(game: str) -> int:
        [opponent_shape, result] = game.split(" ")

        if opponent_shape == "A":
            shape_to_use = {"X": "C", "Y": "A", "Z": "B"}
        elif opponent_shape == "B":
            shape_to_use = {"X": "A", "Y": "B", "Z": "C"}
        elif opponent_shape == "C":
            shape_to_use = {"X": "B", "Y": "C", "Z": "A"}

        shape_points = shape_to_points[shape_to_use[result]]
        result_points = result_to_points[result]

        return shape_points + result_points

    return sum([get_result(game) for game in input.splitlines()])
