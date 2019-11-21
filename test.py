from preprocessing  import get_data, get_word_by_sent, idx_word, word_idx
from textrank import textrank_keyword

text = get_data()
keywords = textrank_keyword(text, 5)

for kw in keywords:
    print(kw[0], end=" ")