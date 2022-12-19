import copy
from dataclasses import dataclass
from functools import cached_property
from itertools import cycle

GRID_WIDTH = 7


def get_blank_space(times=3):
    return [["."] * GRID_WIDTH for _ in range(times)]


def is_empty_line(line: list[str]):
    return ["."] * GRID_WIDTH == line


def print_grid(grid):
    for line in grid:
        print("".join(line))
    print()


@dataclass
class Shape:
    shape: list[list[str]]
    min_x = 0
    x = 2

    @cached_property
    def height(self) -> int:
        return len(self.shape)

    @cached_property
    def width(self) -> int:
        return len(self.shape[0])

    @cached_property
    def max_x(self) -> int:
        return GRID_WIDTH - self.width

    def move_left(self) -> None:
        if self.x > self.min_x:
            self.x -= 1

    def move_right(self) -> None:
        if self.x < self.max_x:
            self.x += 1

    def get_shape(self) -> list[list[str]]:
        return [self.pad_line(line) for line in self.shape]

    def check_boundaries(self, grid_part: list[str]) -> None:
        if is_empty_line(grid_part):
            return

        for test_x in range(self.x, self.max_x + 1):
            shape_floor = self.pad_line(self.shape[-1], test_x)
            for i in range(GRID_WIDTH):
                if grid_part[i] == "#" and shape_floor[i] == "#":
                    self.max_x = test_x - 1
                    break
            else:
                continue
            break

        for test_x in range(self.x, -1, -1):
            shape_floor = self.pad_line(self.shape[-1], test_x)
            print(self.x, test_x, shape_floor, grid_part)
            for i in range(GRID_WIDTH):
                if grid_part[i] == "#" and shape_floor[i] == "#":
                    self.min_x = test_x + 1
                    break
            else:
                continue
            break

    def should_put(self, floor: list[str]) -> bool:
        shape_floor = self.pad_line(self.shape[-1])
        for i in range(GRID_WIDTH):
            if shape_floor[i] == floor[i] == "#":
                return True
        return False

    def merge_shape(self, slice: list[list[str]]) -> list[list[str]]:
        shape = self.get_shape()
        new_slice = copy.deepcopy(slice)
        slice_len = len(slice)
        size_diff = abs(self.height - slice_len)

        if self.height > slice_len:
            spare_part = None
            new_slice = get_blank_space(size_diff) + new_slice
        elif self.height < slice_len:
            spare_part = new_slice[:size_diff]
            new_slice = new_slice[size_diff:]

        for i in range(self.height):
            for j in range(GRID_WIDTH):
                if new_slice[i][j] == "." and shape[i][j] == "#":
                    new_slice[i][j] = "#"
                elif new_slice[i][j] == "#" and shape[i][j] == "#":
                    raise ValueError("Collision detected")

        return spare_part + new_slice if spare_part is not None else new_slice

    def pad_line(self, line: list[str], x=None) -> list[str]:
        if x is None:
            x = self.x
        return list("".join(line).rjust(x + self.width, ".").ljust(GRID_WIDTH, "."))


class Minus(Shape):
    def __init__(self):
        self.shape = [["#", "#", "#", "#"]]


class Plus(Shape):
    def __init__(self):
        self.shape = [
            [".", "#", "."],
            ["#", "#", "#"],
            [".", "#", "."],
        ]


class L(Shape):
    def __init__(self):
        self.shape = [
            [".", ".", "#"],
            [".", ".", "#"],
            ["#", "#", "#"],
        ]


class Pole(Shape):
    def __init__(self):
        self.shape = [
            ["#"],
            ["#"],
            ["#"],
            ["#"],
        ]


class Square(Shape):
    def __init__(self):
        self.shape = [
            ["#", "#"],
            ["#", "#"],
        ]


def part_1(input: str) -> int:
    shapes = cycle([Minus, Plus, L, Pole, Square])
    moves = cycle(list(input))

    grid = [
        *get_blank_space(),
        ["#"] * GRID_WIDTH,
    ]

    round = 1
    while round <= 12:
        shape = next(shapes)()
        active_line = 0

        print(f"ROUND {round}")
        for line in grid:
            print("".join(line))
        print()

        for move in moves:
            next_row = grid[active_line]
            shape.check_boundaries(next_row)
            print()

            if move == ">":
                shape.move_right()
            else:
                shape.move_left()

            if shape.should_put(next_row):
                if active_line == 0:
                    grid = get_blank_space() + shape.get_shape() + grid
                else:
                    grid = (
                        get_blank_space()
                        + shape.merge_shape(grid[:active_line])
                        + grid[active_line:]
                    )
                round += 1
                break
            else:
                if is_empty_line(next_row):
                    grid.pop(active_line)
                else:
                    active_line += 1

    return 0


def part_2(input: str) -> int:
    pass
