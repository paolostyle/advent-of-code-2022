from typing import TypeVar


TCoord = TypeVar("TCoord", bound="Coord")


class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: TCoord) -> TCoord:
        self.x += other.x
        self.y += other.y
        return self

    def is_neighbour(self, other: TCoord) -> bool:
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def move_closer_to(self, other: TCoord) -> None:
        y = other.y - self.y
        x = other.x - self.x

        if y != 0:
            y = y // abs(y)
        if x != 0:
            x = x // abs(x)

        self.y += y
        self.x += x


class Simulation:
    def __init__(self, knots: int, size=550) -> None:
        self.map = [[False] * size for _ in range(size)]
        middle_point = size // 2

        self.knots = [Coord(middle_point, middle_point) for _ in range(knots)]
        self.head = self.knots[0]
        self.tail = self.knots[-1]

        self.mark(self.tail)

    def move(self, instruction: str) -> None:
        match instruction.split(" "):
            case ["R", step]:
                direction = Coord(y=0, x=1)
            case ["L", step]:
                direction = Coord(y=0, x=-1)
            case ["U", step]:
                direction = Coord(y=1, x=0)
            case ["D", step]:
                direction = Coord(y=-1, x=0)

        for _ in range(int(step)):
            self.knots[0] += direction
            for idx, knot in list(enumerate(self.knots))[1:]:
                front_knot = self.knots[idx - 1]
                if not front_knot.is_neighbour(knot):
                    knot.move_closer_to(front_knot)
                    if knot == self.tail:
                        self.mark(knot)

    def mark(self, coord: Coord) -> None:
        self.map[coord.y][coord.x] = True

    def simulate(self, instructions: list[str]) -> int:
        for instruction in instructions:
            self.move(instruction)

        return sum([sum(row) for row in self.map])


def part_1(input: str) -> int:
    instructions = input.splitlines()
    return Simulation(knots=2).simulate(instructions)


def part_2(input: str) -> int:
    instructions = input.splitlines()
    return Simulation(knots=10).simulate(instructions)
