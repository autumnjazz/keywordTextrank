import networkx as nx
import matplotlib.pyplot as plt
import community

def counter_draw(counter, wordlist):
    cnt_draw = []
    for edge, weight in counter.items(): #counter.items() = ((1,2),3)
        cnt_draw.append((wordlist[edge[0]], wordlist[edge[1]], weight))
    return cnt_draw

def initialGraph(cnt_draw,wordlist):
    G = nx.Graph() #undirected
    G.add_weighted_edges_from(cnt_draw) #automatically create nodes as words. no overlapped edges.
    return G

def initialGraph_draw(G):
    nx.draw_networkx(   
        G,
        pos = nx.spring_layout(G),
        with_labels = True,
        node_color=[len(G[n]) for n in G], #color node by num. of neighbors
        cmap="Blues", 
        node_size =300,
        font_size = 6,
        width = 0.4 
    ) 
    plt.show()
    # plt.savefig('initgraph',  bbox_inches ='tight', format='svg')

def textrankGraph(mainkeywords):
    G = nx.Graph()
    for i,keyw in enumerate(mainkeywords):
        G.add_node(keyw[0], weight=keyw[1])
    return G

def textrankGraph_draw(G):
    nx.draw_networkx(   
        G,
        # pos = nx.get_node_attributes(G,'pos'),
        with_labels = True,
        node_color=[n[1] for n in G.nodes(data='weight')], 
        cmap="Reds", 
        node_size =[(n[1]%100)**2 * 100 for n in G.nodes(data='weight')],
        font_size = 6,
        width = 0.4 
    )
    plt.show()
    # plt.savefig('textrankgraph',  bbox_inches ='tight', format='svg')


def communityGraph(G):
    partition = community.best_partition(G) # dictionary {'word1': (int)community1, 'word2': community2, ... }
    colors = [partition.get(node) for node in G.nodes()]
    # mod = community.modularity(partition,G) #modularity of community
    return partition, colors

def communityGraph_draw(G, colors):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color=colors, cmap='Pastel1')
    nx.draw_networkx_edges(G, pos, width = 0.4)
    nx.draw_networkx_labels(G, pos, font_size=6, font_color="black")
    plt.show()