import re
import networkx as nx
import matplotlib.pyplot as plt


VALVE_REGEX = re.compile(
    r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([\w,\s]+)"
)


def part_1(input: str) -> int:
    graph = nx.DiGraph()

    for line in input.splitlines():
        groups = VALVE_REGEX.search(line).groups()
        valve = groups[0]
        flow = int(groups[1])
        tunnels = groups[2].split(", ")

        graph.add_node(valve, demand=1)
        graph.add_weighted_edges_from([(valve, tunnel, 1) for tunnel in tunnels])

        if flow > 0:
            with_valve_name = f"{valve}_V"
            graph.add_node(with_valve_name, demand=1)
            graph.add_weighted_edges_from([(valve, tunnel, 1) for tunnel in tunnels])


def part_2(input: str) -> int:
    pass
