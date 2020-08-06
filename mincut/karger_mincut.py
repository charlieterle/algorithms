# Charles Dieterle
# Karger graph minimum-cut algorithm
# 10 October 2019
# edited 28 July 2020

# In the current implementation, this is quite slow. More optimization would be
# needed to make this algorithm useful on large graphs, but it's at least correct.
# My guess is that my use of data structures is not ideal

import random

def min_cut(g):
    """
    Compute a minimum cut of graph g using Karger's algorithm
    args: g, a dict with tuple keys and list values

    g represents a graph where the keys are tuples representing one or more node ids
    and the values are the node ids towards which the key has outgoing edges.
    """

    def cutsubroutine(g):
        # find a cut of g (not a minimum cut)

        if len(g) < 2:
            return 0, g
        # copy g so it can be re-used in multiple calls to cutsubroutine
        graph = g.copy()
        while len(graph) > 2:
            # choose a random node u_node and the id
            # of a random adjacent node-id v
            u_node = random.choice(list(graph.keys()))
            v = random.choice(graph[u_node])

            # find node that contains node-id v, call it v-node
            for node in graph:
                if v in node:
                    v_node = node
                    break

            # merge u_node and v_node into a new node, then delete them
            new_node = u_node + v_node
            graph[new_node] = graph[u_node] + graph[v_node]
            del graph[v_node]
            del graph[u_node]

            # delete self-loops in new_node
            for x in new_node:
                while True:
                    try:
                        graph[new_node].remove(x)
                    except ValueError:
                        break

        # graph now has two elements of equal length
        # return the length of either one of them, and graph itself
        return len(random.choice(list(graph.values()))), graph


    min = len(g)
    cut = {}

    # run cutsubroutine multiple times
    # 5000 trials gives about 99% certainty of finding a min cut for graph size 200
    # In the current state, this algorithm takes about 5 minutes to
    # complete 5000 trials on my computer with a graph of 200 nodes.
    # Obviously, more speed optimization is needed
    for n in range(int(5000)):
        m, c = cutsubroutine(g)
        if m < min:
            min = m
            cut = c
    return min, cut


# tests
print(
    min_cut({}) == (0, {}),
    min_cut({(1,) : [2]}) == (0, {(1,) : [2]}),
    min_cut({(1,) : [2],
                (2,) : [1]})
            ==
            (1, {(1,) : [2],
                (2,) : [1]}),

    # for this test, we cannot check the resulting graph,
    # but we can check whether it found the size of the minimum cut
    min_cut({(1,) : [2, 3, 4, 5],
                (2,) : [1, 4],
                (3,) : [1, 4, 5],
                (4,) : [1, 2, 3, 5],
                (5,) : [1, 3, 4]})[0]
            == 2,
)
