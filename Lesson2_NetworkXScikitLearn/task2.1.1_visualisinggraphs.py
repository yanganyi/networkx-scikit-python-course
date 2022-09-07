# Task 2.1 Visualising Graphs with NetworkX
# 2.1.1 to 2.1.5 are all different graph visuals, in increasing order of difficulty

import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
G.add_nodes_from([1,2,3])
G.add_edges_from([(1,2),(1,3),(3,1)])
nx.draw(G,with_labels=True)
plt.show()