def can_climb(start: str, goal: str):
    if start == "S":
        start = "a"
    elif start == "E":
        start = "z"

    if goal == "S":
        goal = "a"
    elif goal == "E":
        goal = "z"

    return (ord(start) - ord(goal)) >= -1


class Graph:
    def __init__(self, input: str):
        matrix = [list(line) for line in input.splitlines()]
        width = len(matrix[0])
        height = len(matrix)

        self.graph = {}

        for i in range(height):
            for j in range(width):
                coord = (i, j)
                position = matrix[i][j]
                if position == "S":
                    self.start = coord
                if position == "E":
                    self.end = coord
                self.graph[coord] = []

                if i > 0:
                    if can_climb(position, matrix[i - 1][j]):
                        self.graph[coord].append((i - 1, j))
                if i + 1 < height:
                    if can_climb(position, matrix[i + 1][j]):
                        self.graph[coord].append((i + 1, j))
                if j > 0:
                    if can_climb(position, matrix[i][j - 1]):
                        self.graph[coord].append((i, j - 1))
                if j + 1 < width:
                    if can_climb(position, matrix[i][j + 1]):
                        self.graph[coord].append((i, j + 1))

    def road_length(self):
        path = self.find_shortest_path(self.start, self.end)
        return len(path)

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if self.graph.get(start, None) is None:
            return None
        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


def part_1(input: str) -> int:
    graph = Graph(input)
    return graph.road_length()


def part_2(input: str) -> int:
    pass
