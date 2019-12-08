import networkx as nx
import matplotlib.pyplot as plt
import community

from textrank import textrank_graph, keywords_to_nodes

"""
to initialize a graph
"""
def counter_draw(counter, wordlist):
    cnt_draw = []
    for edge, weight in counter.items(): #counter.items() = ((1,2),3)
        cnt_draw.append((wordlist[edge[0]], wordlist[edge[1]], weight))
    return cnt_draw


def initialGraph(cnt_draw,wordlist):
    G = nx.Graph() #undirected
    G.add_weighted_edges_from(cnt_draw) #automatically create nodes as words. no overlapped edges.
    return G

"""
to transfom a graph
"""
def communityGraph(G): 
    CG = G
    partition = community.best_partition(CG) # dictionary {'word1': (int)community1, 'word2': community2, ... }
    nx.set_node_attributes(CG,partition,'comm')
    return CG


def textrankGraph(G, keyword, subgraph = False): #keyword: ('category', 1.882339313158134)
    TG = subCommunityGraph(G, keyword[0]) #after communityGraph() 
    nx.set_node_attributes(TG, 1, 'weight')

    subkeywords = textrank_graph(TG, keyword[0], topk = 5) #includes the center keyword
    subnodes = keywords_to_nodes(subkeywords)
    nx.set_node_attributes(TG, subnodes)

    if subgraph == True:
        STG = TG.subgraph(subnodes) #networkx library function
        return STG
    else:
        return TG


def subGraph(G,center):
    SG = G.subgraph(G[center]).copy()
    elist = []
    for n in SG.nodes():
        elist.append((n,center))
    SG.add_edges_from(elist)
    return SG


def subCommunityGraph(G, center): #after communityGraph()
    nodelist = []
    info =nx.get_node_attributes(G,'comm')
    commNumm = info[center]
    for n in G:
        if commNumm == info[n]:
            nodelist.append(n)
    SCG = G.subgraph(nodelist)
    return SCG



"""
drawing with matplotlib
"""
def drawgraph(G, cmap = "Blues", nodesize = 350, graphtype = None, savepath=None, show = False):

    if graphtype == "textrank":
        color = [n[1] for n in G.nodes(data='weight')]
        nodesize = [(n[1]%100)**2 * 200 for n in G.nodes(data='weight')]
    elif graphtype == "community": #after communityGraph()
        info =nx.get_node_attributes(G,'comm')
        color = list(info.values())
    else :
        color = [len(G[n]) for n in G] #color node by num. of neighbors
   
    nx.draw_networkx(   
        G,
        pos = nx.spring_layout(G),
        with_labels = True,
        node_color=color,
        cmap=cmap, 
        node_size =nodesize,
        font_size = 6,
        width = 0.4 
    ) 
    if show == True:
        plt.show()

    if savepath != None:
        plt.savefig(savepath,  bbox_inches ='tight')
        plt.close()
        