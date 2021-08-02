import bs4 as bs
import requests
import re
import nltk
import json

def clean_txt(link):

    with open("stopwords.json", "r+", encoding="utf-8") as s_words:
        stopwords = json.load(s_words)
    raw = requests.get(link)
    parsed_text = bs.BeautifulSoup(raw.text,'lxml')
    paragraphs = parsed_text.find_all('p')
    raw_text = ""

    #czyszczenie tekstu
    for p in paragraphs:
        raw_text += p.text
    temp_text = raw_text.lower()
    temp_text = re.sub(
        '(?:\[.*\]|\(|\)|[0-9]+|[(){}.,;•–%:])', ' ',
        temp_text,
        # re.UNICODE,
    )
    temp_text = re.sub(
        r'\s+',
        ' ',
        temp_text,
        # re.UNICODE,
    )
    # przygotowanie danych
    all_lines = nltk.sent_tokenize(temp_text)

    all_words = [nltk.word_tokenize(sent) for sent in temp_text]

    # Stop Words
    for i in range(len(all_words)):
        all_words[i] = [w for w in all_words[i] if w not in stopwords]

    return type(all_words)
