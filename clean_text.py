import bs4 as bs
import requests
import re
import nltk
import json
import lxml

def clean_txt(link):

    with open("stopwords.json", "r+", encoding="utf-8") as s_words:
        stopwords = json.load(s_words)
    raw = requests.get(link)
    parsed_text = bs.BeautifulSoup(raw.text, 'lxml')
    paragraphs = parsed_text.find_all('p')
    raw_text = ""

    #czyszczenie tekstu
    for p in paragraphs:
        raw_text += p.text
    temp_text = raw_text.lower()
    temp_text = re.findall(
        '(\w+)',
        temp_text,
    )

    #przygotowanie danych
    #all_lines = nltk.sent_tokenize(temp_text)
    #nltk.download('punkt')
    all_words = [w for w in temp_text if w not in stopwords]
    all_words = [nltk.word_tokenize(sent) for sent in all_words]

    # Stop Words
    #for i in range(len(all_words)):

    return (all_words)
