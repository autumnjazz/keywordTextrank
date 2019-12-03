import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph() #undirected
G.add_nodes_from([1,2,3,4,5])
elist = [(1, 2,3), (2, 3,1), (1, 4,0), (4, 2,2)]
G.add_weighted_edges_from(elist)

colors = [len(G[n]) for n in G] #인접 노드 개수에 따라 색깔 정도 조절
nx.draw(G,with_labels=True, node_color=colors, cmap=plt.cm.Blues) # default spring_layout
plt.show()

# print(G[2]) #{1: {'weight': 3}, 3: {'weight': 1}, 4: {'weight': 2}}
# print(G.edges[2,1]) #{'weight': 3}
# print(G[2][1]) #{'weight': 3}

# for n in G:
#     print(n)# 1 2 3 4 5
#     for nbr in G[n]:
#         print(nbr) 
