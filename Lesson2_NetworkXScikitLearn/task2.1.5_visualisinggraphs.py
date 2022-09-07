# Task 2.1 Visualising Graphs with NetworkX
# 2.1.1 to 2.1.5 are all different graph visuals, in increasing order of difficulty

import matplotlib.pyplot as plt
import networkx as nx

G=nx.DiGraph()
G.add_nodes_from([0,1,2,3,4,5,6])
G.add_edges_from([(2,4),(1,3),(0,3),(4,6),(3,6),(3,5),(5,6)])

left_nodes   = [0,1,2]
middle_nodes = [3,4]
right_nodes  = [5,6]
pos = {n: (0,i) for i,n in enumerate(left_nodes)}
pos.update({n: (1,i+0.5) for i,n in enumerate(middle_nodes)})
pos.update({n: (2,i+0.5) for i,n in enumerate(right_nodes)})
options = {"font_size":36, "node_size":3000, "node_color":"white", "edgecolors":"black", "linewidths":5, "width":5}
nx.draw_networkx(G, pos, **options)
plt.show()