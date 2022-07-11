import pprint
from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

def graph(connections):
    g = defaultdict(set)
    for node1, node2 in connections:
        g[node1].add(node2)
        g[node2].add(node1)
    return g


g = graph(
    [
        (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 4), (1, 5),
        (2, 0), (2, 6), (2, 7),
        (3, 0), (3, 8), (3, 9),
        (4, 1), (4, 9), (4, 10),
        (5, 1), (5, 6), (5, 11),
        (6, 5), (6, 2), (6, 12),
        (7, 2), (7, 8), (7, 13),
        (8, 3), (8, 7), (8, 14),
        (9, 3), (9, 4), (9, 15),
        (10, 4), (10, 11), (10, 16),
        (11, 5), (11, 10), (11, 17),
        (12, 6), (12, 17), (12, 13),
        (13, 7), (13, 18), (13, 12),
        (14, 8), (14, 15), (14, 18),
        (15, 9), (15, 14), (15, 16),
        (16, 10), (16, 15), (16, 19),
        (17, 11), (17, 12), (17, 19),
        (18, 13), (18, 19), (18, 14),
        (19, 16), (19, 18), (19, 17),
    ]
)

print(g[9])
