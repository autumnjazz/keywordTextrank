from preprocessing  import get_data, get_word_by_sent, idx_word, word_idx
from .textrank import textrank_keyword

text = get_data()
keywords = textrank_keyword(text, 5)
for value in keywords:
    print(value[0],value[1], end="\t")