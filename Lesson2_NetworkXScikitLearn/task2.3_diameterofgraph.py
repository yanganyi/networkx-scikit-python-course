# Task 2.3 - Write a function that given a graph, outputs the diameter of the graph
# This can be solved in O(V^5) maximum (where there are edges between any two vertices)
#  - use Floyd Warshall O(V^3) with a check through all pairs for maximum length O(V^2),
#    effectively finding the diameter
# There are various other methods but all take the same runtime
# We can also instead choose to use nx.all_pairs_shortest_path_length which is O(V^4+V^3E) actual value: O(2V^4+V^3E)

import networkx as nx
def get_diameter(graph: nx.Graph):
    # shortest path between pairs
    apsp=dict(nx.all_pairs_shortest_path_length(graph)) # O(V) + O(V+E)
    res=[]
    # iterating through all "starting" vertices
    for src in apsp.keys(): # O(V)
        # finding the max distance away from this vertex, save it
        res.append(max(apsp[src]).values()) # O(V)
    # find the max of max distance from each vertex, which is the diameter of the graph
    return max(res) # O(V)