import networkx as nx

level = 3
numofkeys = 2**level -1 #sum of G.P. with common ratio = 2

from preprocessing import get_data, word_by_sent, wbys_to_word, word_to_idx, idx_by_sent
text = get_data()
wbys = word_by_sent(text)
wordlist = wbys_to_word(wbys)
wtoi = word_to_idx(wordlist)
ibys = idx_by_sent(wbys, wtoi)

from textrank import count_window, textrank_keyword
counter = count_window(ibys, 5)
mainkeywords = textrank_keyword(text, ibys, wordlist,numofkeys)

import visualization as vis
cnt_draw = vis.counter_draw(counter,wordlist)
IG = vis.initialGraph(cnt_draw,wordlist) # returns a graph
# vis.initialGraph_draw(IG)
# TG = vis.textrankGraph(mainkeywords) # returns a graph
# vis.textrankGraph_draw(TG)
partition, color = vis.communityGraph(IG) # returns dictionary and list
vis.communityGraph_draw(IG, color) # the variable 'color' has 'partiton' variable, which can color the nodes by community

