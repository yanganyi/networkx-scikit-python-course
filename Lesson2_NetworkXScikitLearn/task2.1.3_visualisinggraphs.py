# Task 2.1 Visualising Graphs with NetworkX
# 2.1.1 to 2.1.5 are all different graph visuals, in increasing order of difficulty

import matplotlib.pyplot as plt
import networkx as nx

G=nx.DiGraph()
G.add_nodes_from([1,2,3,4,5,6])
G.add_edges_from([(1,2),(2,1),(1,3),(2,4),(4,5),(3,5),(5,2),(3,6)])

nx.draw(G,with_labels=True,font_weight="bold")
plt.show()