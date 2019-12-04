import networkx as nx
import matplotlib.pyplot as plt

from preprocessing  import wordlist #these are variables, not function
from textrank import counter #these are variables, not function

def counter_draw(counter, wordlist):
    cnt_draw = []
    for edge, weight in counter.items(): #counter.items() = ((1,2),3)
        cnt_draw.append((wordlist[edge[0]], wordlist[edge[1]], weight))
    return cnt_draw

def initialGraph(cnt_draw,wordlist):
    G = nx.Graph() #undirected
    G.add_weighted_edges_from(cnt_draw) #create nodes as words automatically. no overlapped edges.

    nx.draw_networkx(   
        G,
        pos = nx.spring_layout(G),
        with_labels = True,
        node_color=[len(G[n]) for n in G],  #
        cmap=plt.cm.Blues, 
        node_size =300,
        font_size = 6,
        width = 0.4 
    ) 
    plt.show()
    # plt.savefig('initgraph2',  bbox_inches ='tight', format='svg')

def textrankGraph(G, keywords):
    #TODO: choose textrank keyword and a draw graph
    return G


cnt_draw = counter_draw(counter,wordlist)
initialGraph(cnt_draw,wordlist)