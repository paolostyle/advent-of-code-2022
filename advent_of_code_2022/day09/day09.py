class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def is_neighbour(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1


class Map:
    def __init__(self):
        self.map = [[False] * 1000 for _ in range(1000)]
        self.head = Coord(400, 400)
        self.tail = Coord(400, 400)
        self.map[400][400] = True

    def move(self, instruction):
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
            self.head += direction
            if not self.head.is_neighbour(self.tail):
                self.tail += self._get_move_vector()
                self.map[self.tail.y][self.tail.x] = True

    def count_visited(self):
        return sum([sum(row) for row in self.map])

    def _get_move_vector(self):
        y = self.head.y - self.tail.y
        x = self.head.x - self.tail.x

        if y != 0:
            y = y // abs(y)
        if x != 0:
            x = x // abs(x)

        return Coord(x, y)


def part_1(input: str) -> int:
    map = Map()
    for instruction in input.splitlines():
        map.move(instruction)

    return map.count_visited()


def part_2(input: str) -> int:
    pass
