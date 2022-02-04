import bs4 as bs
import requests
import re
import nltk
import json
import zipfile
import lxml
import textract

def clean_txt(input_text):

    with open("stopwords.json", "r+", encoding="utf-8") as s_words:
        stopwords = json.load(s_words)

    #ekstrakcja tekstu z plików o różnych rozszerzeniach
    if input_text.endswith('.odt'):
        with zipfile.ZipFile(input_text, 'r') as zfp:
            with zfp.open('content.xml') as fp:
                raw = bs.BeautifulSoup(fp.read(), 'xml')

    elif input_text.endswith('.docx'):
        with zipfile.ZipFile(input_text, 'r') as zfp:
            with zfp.open('word/document.xml') as fp:
                raw = bs.BeautifulSoup(fp.read(), 'xml')
    # elif input_text.endswith('.doc'):
    #     with zipfile.ZipFile(input_text, 'r') as zfp:
    #         with zfp.open('[Content_Types].xml') as fp:
    #             raw = bs.BeautifulSoup(fp.read(), 'xml')

    #elif input_text.endswith('.pdf'):
    #    raw = textract.process(input_text)
    elif input_text.startswith('http'):
        raw = requests.get(input_text)

    parsed_text = bs.BeautifulSoup(raw.text, 'lxml')
    paragraphs = parsed_text.find_all('p')
    raw_text = ""

    #czyszczenie tekstu
    for p in paragraphs:
        raw_text += p.text
    temp_text = raw_text.lower()
    temp_text = re.sub('[^a-zżźćńęółśą.]', ' ', temp_text)
    #temp_text = re.sub(r'\s+', ' ', temp_text)

    #przygotowanie danych
    all_lines = nltk.sent_tokenize(temp_text)
    #nltk.download('punkt')
    #all_words = [w for w in temp_text if w not in stopwords]
    #all_words = [nltk.word_tokenize(sent) for sent in all_words]

    all_words = [nltk.word_tokenize(sent) for sent in all_lines]
    for i in range(len(all_words)):
        all_words[i] = [w for w in all_words[i] if w not in stopwords]
        all_words[i] = [w for w in all_words[i] if len(w)>2]

    print(all_words)

    return all_words
