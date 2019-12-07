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
IG = vis.initialGraph(cnt_draw,wordlist)
vis.drawgraph(IG, cmap = "Blues", nodesize = 350, graphtype = None, savepath="initial.png", show = False)

TG = vis.textrankGraph(mainkeywords) 
vis.drawgraph(TG, cmap = "Reds", nodesize = 350, graphtype = "textrank", savepath="textrank.png", show = False)

vis.communityGraph(IG) 
vis.drawgraph(IG, cmap = "Pastel1", nodesize = 350, graphtype = "community", savepath="community.png", show = False)

energy_SG = vis.subGraph(IG, "energy")
vis.drawgraph(energy_SG, cmap = "Oranges", nodesize = 350, graphtype = None, savepath="subgraph.png", show = False)

energy_SCG = vis.subCommunityGraph(IG, "energy") #only after communityGraph() method
vis.drawgraph(energy_SCG, cmap = "Pastel1", nodesize = 350, graphtype = "community", savepath="subcommunity.png", show = False)