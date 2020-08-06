# Charles Dieterle
# Dijkstra's Shortest Path Algorithm (undirected, weighted graph)
# 28 January 2020
# edited 27 July 2020

def dijkstra(graph_file, source, all_nodes=True, print_nodes=None):
    """
    return list of all nodes in a graph and their shortest paths to a source node
    args: - graph_file, a filepath to a text file (see below for file specification)
          - source, an identifier string matching to the source node
    keyword args:
          - all_nodes, when changed to False, will print shortest paths
                for only the nodes in print_nodes
          - print_nodes, an optional list of node ids, where

    graph_file specification:
        -The first element in each line of text is the id of a node n
        -Each subsequent element in the line is of the form "n2,w"
            where n2 is a connected node and w is the weight of
            the edge between n and n2
        -The elements of each line are separated by tabs
    See dijkstraData.txt to view the graph data provided for this homework problem
    """

    # ensure correct usage of the function's keyword arguments
    if all_nodes == False and print_nodes == None:
        print("Error: must include list argument print_nodes if all_nodes is False")
        return

    if print_nodes != None and all_nodes == True:
        print("Error: must set argument all_nodes to False to utilize print_nodes")
        return

    # For each node "n" in graph, G[n] is a list of 2-tuples, where
    # G[n][0] is the id of another node and G[n][1] is the weight of the edge
    # between the nodes n and G[n][0].
    G = createG(graph_file)

    # create a dict to contain the shortest path values for all nodes
    shortest_paths = {}

    # set source node shortest path to 0
    shortest_paths[source] = 0

    # main loop
    number_of_nodes = len(G)
    explored_count = 1
    while explored_count < number_of_nodes:
        next_path = float("inf")  # store next shortest path
        next_node = None  # store next node to be added to shortest_paths

        # find the node with the shortest path from the already explored nodes
        for node in shortest_paths:
            for edge in G[node]:
                new_node = edge[0]
                weight = edge[1]
                if new_node not in shortest_paths and \
                        shortest_paths[node] + weight < next_path:
                    next_node = new_node
                    next_path = shortest_paths[node] + weight

        # next_node is guaranteed to be an actual node, rather than None
        shortest_paths[next_node] = next_path
        explored_count += 1

    if all_nodes:
        for node in shortest_paths:
            print("The shortest path from {} to {} is {}".format(source, node, shortest_paths[node]))

    else:
        for node in print_nodes:
            print("The shortest path from {} to {} is {}".format(source, node, shortest_paths[node]))

def createG(file):
    # create a graph G (a python dict) to search for shortest paths

    with open(file) as f:
        data = f.read().split("\n")[:-1]
        for x in range(len(data)):
            data[x] = data[x].split("\t")[:-1]

    G = {}
    # make each value in G a list of tuples of form (node, weight)
    for line in data:
        G[line[0]] = line[1:]
    for node in G:
        for edge in range(len(G[node])):
            new_value = G[node][edge].split(",")
            new_value = (new_value[0], int(new_value[1]))
            G[node][edge] = new_value

    return G


# example calls using "1" as source node and a previously provided graph_file
dijkstra("dijkstra_data.txt", "1")
dijkstra("dijkstra_data.txt", "1", all_nodes=False, print_nodes=["6", "19", "93", "42"])
