# Task 2.1 Visualising Graphs with NetworkX
# 2.1.1 to 2.1.5 are all different graph visuals, in increasing order of difficulty

# TODO: THIS CODE DOES NOT WORK YET
import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
l=[]
nodes=int(input("N: "))
for i in range(nodes):
    l.append(i)
    
for i in range(nodes**2):
    G.add_node(i)
    if i<20: G.add_edge(i,i+5)
    if i%5!=4 and i<24: G.add_edge(i,i+1)
    
pos = {i: (1,1) for i in enumerate(l)}
pos.update({0: (0,0)})
for i in range(nodes):
    for j in range(nodes):
        pos.update({nodes*i+j: (0.5*j,0.5*i)})



nx.draw(G,pos,with_labels=True,font_weight="bold")
# pos=nx.spiral_layout(G)
# read documentation ^^^
plt.show()