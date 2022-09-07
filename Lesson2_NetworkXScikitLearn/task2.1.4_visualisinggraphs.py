# Task 2.1 Visualising Graphs with NetworkX
# 2.1.1 to 2.1.5 are all different graph visuals, in increasing order of difficulty

import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(1,3),(1,5),(2,3),(3,4),(4,5)])

pos = {1:(0,0), 2:(-1,0.3), 3:(2,0.17), 4:(4,0.255), 5:(5,0.03)}
options = {"font_size":36, "node_size":3000, "node_color":"white", "edgecolors":"black", "linewidths":5, "width":5}
nx.draw_networkx(G,pos,**options)
ax=plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()