from collections import defaultdict
from typing import Set, Tuple, NewType
Graph = NewType('Graph', dict[int, Set[int]])


def graph(connections: list[Tuple[int, int]]) -> Graph:
    g = defaultdict(set)
    for node1, node2 in connections:
        g[node1].add(node2)
        g[node2].add(node1)
    return g
