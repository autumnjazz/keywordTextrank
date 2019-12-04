
from preprocessing import get_data, word_by_sent, wbys_to_word, word_to_idx, idx_by_sent
text = get_data()
wbys = word_by_sent(text)
wordlist = wbys_to_word(wbys)
wtoi = word_to_idx(wordlist)
ibys = idx_by_sent(wbys, wtoi)

from textrank import count_window, textrank_keyword
counter = count_window(ibys)
mainkeyword = textrank_keyword(text, ibys, wordlist,5)

from visualization import counter_draw, initialGraph
cnt_draw = counter_draw(counter,wordlist)
initialGraph(cnt_draw,wordlist)