from django.shortcuts import render
from scipy.sparse import csr_matrix
import json
from django.http import JsonResponse, HttpResponseForbidden
from showkeyword.functions.preprocessing import word_by_sent, wbys_to_word, word_to_idx, idx_by_sent
from showkeyword.functions.textrank import count_window, adjacency_matrix, pagerank

# Create your views here.

def home(request):
	return render(request, 'showkeyword/home.html')

def count(request):
    if request.is_ajax():
        if request.method == 'POST':
            text = json.loads(request.body.decode('utf-8'))['text']
            wbys = word_by_sent(text)
            wordlist = wbys_to_word(wbys)
            wtoi = word_to_idx(wordlist)
            ibys = idx_by_sent(wbys, wtoi)
            counter = count_window(ibys)
            m = adjacency_matrix(counter, size=len(wordlist))

            return JsonResponse({"graph": m.toarray().tolist(), "words": wtoi})

    return HttpResponseForbidden()

def textrank(request):
    if request.is_ajax():
        if request.method == 'POST':
            graph = json.loads(request.body.decode('utf-8'))['graph']
            R = pagerank(csr_matrix(graph)).reshape(-1)
            idxs = list(map(lambda x: x.item(), reversed(R.argsort()[-5:])))
            return JsonResponse({"result": idxs})

    return HttpResponseForbidden()
