import networkx as nx

level = 3
numofkeys = 1 #the number of mainkeywords   #2**level -1 #sum of G.P. with common ratio = 2

from preprocessing import get_data, word_by_sent, wbys_to_word, word_to_idx, idx_by_sent
text = get_data()
wbys = word_by_sent(text)
wordlist = wbys_to_word(wbys)
wtoi = word_to_idx(wordlist)
ibys = idx_by_sent(wbys, wtoi)

from textrank import count_window, textrank_keyword
counter = count_window(ibys, 5)
mainkeywords = textrank_keyword(ibys, wordlist,numofkeys)

import visualization as vis
cnt_draw = vis.counter_draw(counter,wordlist)
IG = vis.initialGraph(cnt_draw,wordlist)
# vis.drawgraph(IG, cmap = "Blues", nodesize = 350, graphtype = None, savepath=None, show = True)

vis.communityGraph(IG) 
# vis.drawgraph(IG, cmap = "Pastel1", nodesize = 350, graphtype = "community", savepath="community.png", show = False)

# energy_SG = vis.subGraph(IG, "energy")
# vis.drawgraph(energy_SG, cmap = "Oranges", nodesize = 350, graphtype = None, savepath="subgraph.png", show = False)

# energy_SCG = vis.subCommunityGraph(IG, "energy") #only after communityGraph() method
# vis.drawgraph(energy_SCG, cmap = "Pastel1", nodesize = 350, graphtype = "community", savepath="subcommunity.png", show = False)

"""
The core of this project:
1. Method textrankGraph() must be implemented after communityGraph() method and textrank_keyword() method.
2. It takes one mainkeyword tuple which formed like: ('bars', 1.8823393131581336).
3. The parameter 'subgraph' determines wheter the result is 
   subgraph of community graph or just whole community graph, which includes given mainkeyword.
4. You can use any type for graphtype parameter("community", "textrank", None), but "textrank" shows the best visualization.
"""
TG = vis.textrankGraph(IG, mainkeywords[0], subgraph = False) #textrank graph with whole community
vis.drawgraph(TG, cmap = "YlGn", graphtype = "textrank", savepath="textrankgraph.png",show = False)
STG = vis.textrankGraph(IG, mainkeywords[0], subgraph = True) #sub textrank graph
vis.drawgraph(STG, cmap = "YlGn", graphtype = "textrank", savepath="subtextrankgraph.png",show = False)