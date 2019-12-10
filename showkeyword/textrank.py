from collections import defaultdict
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
import numpy as np
import networkx as nx
"""
based on https://github.com/lovit/textrank
"""

def count_window(ibys, window=3): #only one directed edge and weight    #by index not word
    counter = defaultdict(int)
    if(window<2 or window > 10):
        window = 3

    for sent in ibys:
        for i in range(len(sent)-window+1):
            word_window = sent[i:i+window]
            for j in range(window-1):
                counter[(word_window[j], word_window[j+1])] += 1
            counter[(word_window[0], word_window[-1])] += 1
        if len(sent)!=0 and len(sent) < window: 
            for i in range(len(sent)-1):
                counter[(sent[i], sent[i+1])] += 1
            counter[(sent[0], sent[-1])] += 1
    return counter

def adjacency_matrix(counter, size):
    rows, cols, data = [],[],[]
    for (i,j), d in counter.items():
        rows.append(i)
        cols.append(j)
        data.append(d)
        #inverse order of row and col
        rows.append(j)
        cols.append(i)
        data.append(d)
    return csr_matrix((data, (rows, cols)), shape=(size, size))

def pagerank(matrix, df=0.85, max_iter=30):
    assert 0 < df < 1
    # initialize
    A = normalize(matrix, axis=0, norm='l1')
    R = np.ones(A.shape[0]).reshape(-1,1)
    bias = (1 - df) * R
    # iteration
    for _ in range(max_iter):
        R = df * (A * R) + bias
    return R


def textrank_keyword(ibys, wordlist, topk = 30):
    counter = count_window(ibys)
    m = adjacency_matrix(counter, size=len(wordlist))
    R = pagerank(m).reshape(-1)
    idxs = R.argsort()[-topk:]
    keywords = [(wordlist[idx], R[idx]) for idx in reversed(idxs)]
    return keywords

def textrank_graph(G, center, topk = 5):
    tmpG = G.copy()
    tmpG.remove_node(center)

    indextoword = []
    setindex = dict() #{'fooled': {'index': 0},  ...
    for idx, node in enumerate(tmpG.nodes()):
        setindex[node] = {'index':idx}
        indextoword.append(node)
    nx.set_node_attributes(tmpG, setindex)
    wordtoindex = nx.get_node_attributes(tmpG, 'index') #{'fooled': 0, 'word': 1, ...
    counter = dict()
    for i,j,d in tmpG.edges.data('weight', default=1):
        counter[(wordtoindex[i],wordtoindex[j])] = d
    
    m = adjacency_matrix(counter, size = len(tmpG.nodes()))
    R = pagerank(m).reshape(-1)
    idxs = R.argsort()[-topk:]
    subkeywords = [(indextoword[idx], R[idx]) for idx in reversed(idxs)]
    subkeywords.append((center, R[idxs[-1]] * 1.2))
    return subkeywords

def keywords_to_nodes(keywordslist): # parameter:  [('category', 1.8823393131581336), ...
    textrank = dict()
    for kwd in keywordslist:
        textrank[kwd[0]] = {'weight': kwd[1]}
    return textrank #{'category': {'weight': 1.8823393131581336}, ...