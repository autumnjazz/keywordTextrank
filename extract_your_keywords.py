from graph import Graph
from preprocesing import get_data, create_wordlist

def get_words(path=None):
    text_string = get_data(path)
    word_by_sent = create_wordlist(text_string)
    return word_by_sent

def create_graph_with_words(word_by_sent):
    graph = Graph()
    for sent in word_by_sent:
        for word in sent:
            graph.add_vertex(word)
    return graph

def make_edge(graph, word_by_sent, window = 3):
    if(window<2 or window > 10):
        return
    for word_list in word_by_sent: #문장별로 window 확인
        for i in range(len(word_list)-window):
            word_window = word_list[i:i+window]
            for j in range(window-1):
                graph.add_edge({word_window[j], word_window[j+1]})
            graph.add_edge({word_window[0], word_window[-1]})
    return graph


# word_by_sent = get_words()
# print(word_by_sent)
# graph = create_graph_with_words(word_by_sent)
# graph = make_edge(graph, word_by_sent)
# print(graph.vertices())
# print(graph.edges())


