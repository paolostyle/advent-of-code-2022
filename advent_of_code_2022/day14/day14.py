import itertools


class Cave:
    def __init__(self, input: str):
        self.map = [["."] * 1000 for _ in range(200)]
        self.map[0][500] = "+"
        instructions = self._parse_input(input)
        self._draw_cave(instructions)
        self._find_boundaries(instructions)

    def pour_sand(self):
        sand_drops = 0
        y = 0
        x = 500
        while self.map[0][500] != "o" and y < self.max_y:
            if self.map[y + 1][x] == ".":
                y += 1
            elif self.map[y + 1][x - 1] == ".":
                y += 1
                x -= 1
            elif self.map[y + 1][x + 1] == ".":
                y += 1
                x += 1
            else:
                self.map[y][x] = "o"
                y = 0
                x = 500
                sand_drops += 1
        return sand_drops

    def add_floor(self):
        self._draw_line((0, self.max_y + 2), (999, self.max_y + 2))
        self.max_y += 2

    def _parse_input(self, input: str) -> list[list[tuple]]:
        instructions: list[list[tuple]] = []
        for line in input.splitlines():
            path = line.split(" -> ")
            instruction: list[tuple] = []
            for coord in path:
                x, y = coord.split(",")
                instruction.append((int(x), int(y)))
            instructions.append(instruction)
        return instructions

    def _find_boundaries(self, instructions: list[list[tuple]]):
        flat_list = list(itertools.chain(*instructions))
        flat_x = [x for x, _ in flat_list]
        self.min_x = min(flat_x)
        self.max_x = max(flat_x)
        self.max_y = max([y for _, y in flat_list])

    def _draw_cave(self, instructions: list[list[tuple]]):
        for instruction in instructions:
            for i in range(1, len(instruction)):
                self._draw_line(instruction[i - 1], instruction[i])

    def _draw_line(self, a: tuple, b: tuple):
        a_x, a_y = a
        b_x, b_y = b
        if a_x == b_x:
            for y in range(min((a_y, b_y)), max((a_y, b_y)) + 1):
                self.map[y][a_x] = "#"
        elif a_y == b_y:
            for x in range(min((a_x, b_x)), max((a_x, b_x)) + 1):
                self.map[a_y][x] = "#"

    def print_cave(self):
        print(
            "\n".join(
                [
                    "".join([str(cell) for cell in row])
                    for row in [
                        self.map[i][self.min_x - 1 : self.max_x + 1]
                        for i in range(self.max_y + 1)
                    ]
                ]
            )
        )


def part_1(input: str) -> int:
    cave = Cave(input)
    return cave.pour_sand()


def part_2(input: str) -> int:
    cave = Cave(input)
    cave.add_floor()
    return cave.pour_sand()
