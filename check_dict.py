from gensim.models import Word2Vec, KeyedVectors, Phrases
#import LDA2Vec
import numpy as np

def check_dict(clean_text):

    model = Word2Vec.load('wiki.word2vec.model')
    result = []
    skipped = 0
    for sentence in clean_text:
        for word in sentence:
            try:
                model.wv[word]
                result.append(word)
            except KeyError:
                skipped +=1
                pass

    #print(skipped, " słów nie ma w słowniku")
    return result, skipped
