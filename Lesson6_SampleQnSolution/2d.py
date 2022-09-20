from soln_lib import * 
import random
import numpy as np
from sklearn.linear_model import LinearRegression 

def make_data(n: int, k_nodes_to_remove: int = 0) -> tuple[np.ndarray, np.ndarray]: 
    """
    Makes training data for q2d.
    :param n: The size of the lattice graph
    :param k_nodes_to_remove: The number of random nodes to remove. Randomly sampled. :return: tuple of features, labels
    """
    vertices, edges = make_square_graph(n)
    nodes_to_remove = random.sample(vertices, k_nodes_to_remove)
    for node in nodes_to_remove: 
        vertices.remove(node)
    possible_shw_positions = make_possible_superhighway_positions(vertices)
    

    def _remove_nodes(g: nx.Graph, nodes: list[Vertex]): 
        for nd in nodes:
            g.remove_node(nd) 
        return g
    
    x = []
    y = []
    for pos in possible_shw_positions:
        gr = make_nx_square_graph(n, pos)
        _remove_nodes(gr, nodes_to_remove)
        diam = get_diameter(gr)
        x.append([*tuple(pos.dest), *sub_vert(pos.origin, pos.dest)])
        # instead of sending in pos.dest and relative distance
        # also send in pos.dest**2 and relative distance**2
        # check whatsapp
        # either test to improve in this area, or use make_data
        # make_data is not exhaustive so make more to train!
        y.append(diam)
    return np.array(x), np.array(y)


features, labels = make_data(5, 1)
model = LinearRegression()
model.fit(np.array(features), np.array(labels))
print("Score is: %.4f " % model.score(features, labels))