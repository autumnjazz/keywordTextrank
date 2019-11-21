import re
import string
from stopwords import stopwords

def get_data(path=None):    #원문 그대로
    if path != None:
        document_text = open(path, 'r')
        text_string = document_text.read()
    else:
        text_string = open('test_news.txt', 'r').read()
    return text_string

def split_to_sent(text_string): #원문 -> [ '문장1', '문장2', ... ]
    original_sent = re.split("[!?.]+", text_string)
    return original_sent

def split_to_word(sent_string): #문장 -> [ '단어1', '단어2', ... ]
    original_word = re.split(" ", sent_string)
    return original_word

def get_word_by_sent(text_string): 
    original_sent = split_to_sent(text_string)
    word_by_sent = []
    for sent in original_sent:
        sent = re.sub(r"[^a-z]+", " ", sent.lower())
        word_by_sent.append([word for word in split_to_word(sent) if word not in stopwords and word != ''])
    return word_by_sent

def idx_word(text_string): #원문 -> [ '단어1', '단어2', ... ]
    original_sent = split_to_sent(text_string)
    idx_to_word = []
    for sent in original_sent:
        sent = re.sub(r"[^a-z]+", " ", sent.lower())
        for word in split_to_word(sent):
            if word not in stopwords and word != '' and word not in idx_to_word: #중복 제거
                idx_to_word.append(word)
    return idx_to_word

def word_idx(text_string): #['단어1', '단어2', ... ] -> {'단어1':0, '단어2':1, ...}
    idx_to_word = idx_word(text_string)
    word_to_idx = {word:idx for idx, word in enumerate(idx_to_word)}
    return word_to_idx

# text_string = get_data()
# wordlist = idx_word(text_string)
# print(wordlist)
# print(word_idx(wordlist))
