import sys


def get_shortest_paths(
    graph: dict[tuple, list[tuple]], start: tuple
) -> dict[tuple, int]:
    nodes_to_visit = list(graph.keys())
    paths_length = {node: sys.maxsize for node in nodes_to_visit}
    paths_length[start] = 0

    while nodes_to_visit:
        min_node = nodes_to_visit[0]
        for node in nodes_to_visit:
            if paths_length[node] < paths_length[min_node]:
                min_node = node

        nodes_to_visit.remove(min_node)

        for neighbour in graph[min_node]:
            new_length = paths_length[min_node] + 1
            if new_length < paths_length[neighbour]:
                paths_length[neighbour] = new_length

    return paths_length


class Graph:
    def __init__(self, input: str, going_up: bool = True):
        self.map = [list(line) for line in input.splitlines()]
        self.graph: dict[tuple, list[tuple]] = {}
        self.reversed_elevations = 1 if going_up else -1

        width = len(self.map[0])
        height = len(self.map)

        for i in range(height):
            for j in range(width):
                node = (i, j)
                elevation = self.map[i][j]

                if elevation == "S":
                    self.start = node
                if elevation == "E":
                    self.end = node

                self.graph[node] = []

                if i > 0:
                    if self._can_climb(elevation, self.map[i - 1][j]):
                        self.graph[node].append((i - 1, j))
                if i + 1 < height:
                    if self._can_climb(elevation, self.map[i + 1][j]):
                        self.graph[node].append((i + 1, j))
                if j > 0:
                    if self._can_climb(elevation, self.map[i][j - 1]):
                        self.graph[node].append((i, j - 1))
                if j + 1 < width:
                    if self._can_climb(elevation, self.map[i][j + 1]):
                        self.graph[node].append((i, j + 1))

    def _can_climb(self, start: str, goal: str) -> bool:
        if start == "S":
            start = "a"
        elif start == "E":
            start = "z"

        if goal == "S":
            goal = "a"
        elif goal == "E":
            goal = "z"

        return (ord(start) - ord(goal)) * self.reversed_elevations >= -1


def part_1(input: str) -> int:
    graph = Graph(input, going_up=True)
    return get_shortest_paths(graph.graph, graph.start)[graph.end]


def part_2(input: str) -> int:
    graph = Graph(input, going_up=False)
    shortest_paths = get_shortest_paths(graph.graph, graph.end)
    nodes_with_low_elevation = [
        node for node in graph.graph.keys() if graph.map[node[0]][node[1]] in ("a", "S")
    ]
    return min(
        [
            length
            for node, length in shortest_paths.items()
            if node in nodes_with_low_elevation
        ]
    )
