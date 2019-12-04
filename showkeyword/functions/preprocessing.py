import re
import string
from stopwords import stopwords


def get_data(path=None):    
    if path != None:
        document_text = open(path, 'r')
        text_string = document_text.read()
    else:
        text_string = open('test_news.txt', 'r').read()
    return text_string

def split_to_sent(text_string): 
    original_sent = re.split("[!?.]+", text_string)
    return original_sent

def split_to_word(sent_string): 
    original_word = re.split(" ", sent_string)
    return original_word

def word_by_sent(text_string): 
    original_sent = split_to_sent(text_string)
    wbys = []
    for sent in original_sent:
        sent = re.sub(r"[^a-z]+", " ", sent.lower()) #only for eng
        wbys.append([word for word in split_to_word(sent) if word not in stopwords and word != ''])
    return wbys

def idx_by_sent(wbys, wtoi): #used for textrank
    ibys = []
    for sent in wbys:
        ibys.append([wtoi[word] for word in sent])
    return ibys

def word_to_idx(wordlist):
    wtoi = {}
    for idx, word in enumerate(wordlist):
        wtoi[word] = idx
    return wtoi

def text_to_word(text_string): 
    wbys = word_by_sent(text_string)
    wordlist = []
    for sent in wbys:
        for word in sent:
            if word not in wordlist:
                wordlist.append(word)
    return wordlist

def wbys_to_word(wbys): 
    wordlist = []
    for sent in wbys:
        for word in sent:
            if word not in wordlist:
                wordlist.append(word)
    return wordlist


def tokenizer(wordlist):
    token = {}
    #TODO: get tokens by parts of speech
    return token


