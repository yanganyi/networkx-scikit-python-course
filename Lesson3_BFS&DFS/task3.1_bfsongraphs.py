# Task 3.1 - Write a BFS algorithm that works on graphs

import matplotlib.pyplot as plt
import networkx as nx

G=nx.gnp_random_graph(20,0.14) # 20 nodes, 0.14 probability for edge creation

visited={}
queue=[]
findNodeNamed=15
startNode=0
finalPath=[]
queue.append((startNode,[startNode]))
visited[startNode]=True
while len(queue)>0:
    nodeName,path=queue.pop()
    if nodeName==findNodeNamed:
        finalPath=path
        break
    successors=nx.neighbors(G,nodeName)
    for successor in successors:
        if successor not in visited:
            queue.append((successor,path+[successor]))
            visited[successor]=True

pos=nx.spring_layout(G)
color_coded_path=["red" if node in finalPath else "grey" for node in nx.nodes(G)]
nx.draw(G,pos,with_labels=True,node_color=color_coded_path)
plt.show()