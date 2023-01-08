import graphs.utils as gr
import numpy as np
from pprint import PrettyPrinter
import matplotlib.plt as plt
printer = PrettyPrinter()


connections = [
    (0, 1), (0, 2), (0, 3),
    # (1, 0), only edges out of home node, not back (don't want paths that go 'through' the home node)
    (1, 4), (1, 5), 
    # (2, 0), 
    (2, 6), (2, 7),
    # (3, 0),
    (3, 8), (3, 9),
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
g = gr.graph(connections)

adjacency = gr.adjacency(g)
for i in range(len(adjacency)):
    """
    special adjacency matrix - we don't want paths that go through node 0
    so we make A[i][0] for all i - ie: pretend there is no edge between i and 0
    we only want paths that begin with 0 and end at 1, 2 or 3
    """
    adjacency[i][0] = 0

res = np.identity(len(g))
exp = 0
prob = 1 / 3
total_prob = 0
print(adjacency)

def get_num_paths(adjacency):
    return int(sum([res[0][1], res[0][2], res[0][3]]))
    

for n in range(1, 700):
    N = n + 1
    np.matmul(adjacency, res, out=res)
    num_distinct_paths = get_num_paths(res)
    print('num paths', num_distinct_paths, N)
    prob = prob/3

    probability = num_distinct_paths * prob
    total_prob += probability

    exp += N * probability


print('expected value', exp, total_prob)
print('--------')
# expected value is ~19.999999
"""
can probably concentrate on B >= 20

"""
