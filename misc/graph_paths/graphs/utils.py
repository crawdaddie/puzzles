import numpy as np
from collections import defaultdict
from typing import Set, Tuple, NewType
Graph = NewType('Graph', dict[int, Set[int]])


def graph(connections: list[Tuple[int, int]]) -> Graph:
    g = defaultdict(set)
    for node1, node2 in connections:
        g[node1].add(node2)
        g[node2].add(node1)
    return g


def adjacency(graph: Graph) -> np.ndarray:
    matrix = np.zeros((len(graph), len(graph)))
    for i in graph:
        neighbors = graph[i]
        for j in neighbors:
            matrix[i][j] = 1
            # if j != 0 else 0
    return matrix


def num_n_length_cycles(adjacency: np.ndarray, origin=0, n=1):
    num = 0

    for _ in range(n):
        for k in range(len(adjacency)):
            num += adjacency[0][k] * adjacency[k][0]

    return num
# def power(matrix, res, k):
#     return matrix
