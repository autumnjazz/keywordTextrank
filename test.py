from preprocessing  import get_data, get_word_by_sent, idx_word, word_idx
from textrank import textrank_keyword, count_window

text = get_data()
wbs = get_word_by_sent(text)
word_to_idx = word_idx(text)
idx_to_word = idx_word(text)
counter = count_window(wbs,word_to_idx)
print(counter)
# keywords = textrank_keyword(text, 5)
# for value in keywords:
#     print(value[0],value[1], end="\t")