from preprocessing  import get_data, get_word_by_sent, idx_word, word_idx
from textrank import count_window
import networkx as nx
import matplotlib.pyplot as plt

def counter_draw(counter, idx_to_word):
    cnt_draw = []
    for edge, weight in counter.items():
        tup = (idx_to_word[edge[0]], idx_to_word[edge[1]], weight)
        cnt_draw.append(tup)
    return cnt_draw

def initialGraph(idx_to_word,cnt_draw):
    G = nx.Graph() #undirected
    G.add_weighted_edges_from(cnt_draw) #노드 자동 생성,중복 엣지 없음, 단어가 노드

    nx.draw_networkx(G,
        pos=nx.spring_layout(G),
        with_labels = True,
        node_color=[len(G[n]) for n in G],  #인접 노드 개수에 따라 색깔 정도 조절
        cmap=plt.cm.Blues, 
        node_size =300,
        font_size = 6,
        width = 0.4
    ) 
    plt.show()
    # plt.savefig('initgraph2',  bbox_inches ='tight', format='svg')

def textrankGraph(G, keywords):

    return G

text = get_data()
wbs = get_word_by_sent(text)
word_to_idx = word_idx(text)
idx_to_word = idx_word(text)
counter = count_window(wbs,word_to_idx)
cnt_draw = counter_draw(counter,idx_to_word)

initialGraph(idx_to_word,cnt_draw)