from collections import defaultdict
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
import numpy as np
from preprocessing  import get_word_by_sent, word_idx, idx_word

def count_window(word_by_sent, word_to_idx, window=3):
    counter = defaultdict(int)
    if(window<2 or window > 10):
        window = 3
    for word_list in word_by_sent: #문장별로 window 확인
        widx = [word_to_idx[w] for w in word_list] #인덱스로 변환
        for i in range(len(widx)-window):
            word_window = widx[i:i+window]
            for j in range(window-1):
                counter[(word_window[j], word_window[j+1])] += 1
                counter[(word_window[j+1], word_window[j])] += 1
            counter[(word_window[0], word_window[-1])] += 1
            counter[(word_window[-1], word_window[0])] += 1
    return counter # {(2, 3): 5, (3, 2): 5, ... }

def count_matrix(counter, size):
    rows, cols, data = [],[],[]
    for (i,j), d in counter.items():
        rows.append(i)
        cols.append(j)
        data.append(d)
    return csr_matrix((data, (rows, cols)), shape=(size, size))


def pagerank(x, df=0.85, max_iter=30):
    assert 0 < df < 1

    # initialize
    A = normalize(x, axis=0, norm='l1')
    R = np.ones(A.shape[0]).reshape(-1,1)
    bias = (1 - df) * np.ones(A.shape[0]).reshape(-1,1)

    # iteration
    for _ in range(max_iter):
        R = df * (A * R) + bias

    return R



def all_textrank_keyword(text, topk = 30):
    wbs = get_word_by_sent(text)
    word_to_idx = word_idx(text)
    idx_to_word = idx_word(text)
    counter = count_window(wbs,word_to_idx)
    m = count_matrix(counter, size=len(word_to_idx)) #중복 없는 단어 개수
    R = pagerank(m).reshape(-1)
    idxs = R.argsort()[-topk:]
    keywords = [(idx_to_word[idx], R[idx]) for idx in reversed(idxs)]
    return keywords

