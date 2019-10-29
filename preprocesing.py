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

def create_wordlist(text_string):
    original_sent = split_to_sent(text_string)
    word_by_sent = []
    for sent in original_sent:
        sent = re.sub(r"[^a-z]+", " ", sent.lower())
        word_by_sent.append([word for word in split_to_word(sent) if word not in stopwords and word != ''])
    return word_by_sent

# text_string = get_data()
# original_sent = split_to_sent(text_string)
# print(create_wordlist(text_string))