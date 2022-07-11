from collections import defaultdict
class Graph(object):
    def __init__(self, connections):
        self._graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
        self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

dodecahedral_graph = Graph(
    [
        (0, 1), (0, 2), (0, 3),
    ]
)
