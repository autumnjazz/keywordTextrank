from collections import defaultdict
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
import numpy as np

from preprocessing  import text, ibys, wordlist #these are variables, not function


def count_window(ibys, window=3): #only one directed edge and weight    #by index not word
    counter = defaultdict(int)
    if(window<2 or window > 10):
        window = 3
    for sent in ibys:
        for i in range(len(sent)-window):
            word_window = sent[i:i+window]
            for j in range(window-1):
                counter[(word_window[j], word_window[j+1])] += 1
            counter[(word_window[0], word_window[-1])] += 1
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

def pagerank(matrix, df=0.85, max_iter=30): #TODO: change to exact textrank algorithm (using weights)
    assert 0 < df < 1
    # initialize
    A = normalize(matrix, axis=0, norm='l1')
    R = np.ones(A.shape[0]).reshape(-1,1)
    bias = (1 - df) * np.ones(A.shape[0]).reshape(-1,1)
    # iteration
    for _ in range(max_iter):
        R = df * (A * R) + bias
    return R


def textrank_keyword(text, ibys, wordlist, topk = 30):
    counter = count_window(ibys)
    m = adjacency_matrix(counter, size=len(wordlist))
    R = pagerank(m).reshape(-1)
    idxs = R.argsort()[-topk:]
    keywords = [(wordlist[idx], R[idx]) for idx in reversed(idxs)]
    return keywords

counter = count_window(ibys)
print(textrank_keyword(text, ibys, wordlist,5))

