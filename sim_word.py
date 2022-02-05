from gensim.models import Word2Vec, KeyedVectors, Phrases
#import LDA2Vec

def sim_word(clean_text):
    num_top = 2
    model = Word2Vec(sentences = clean_text,
                     window = 2,
                     vector_size = 100,
                     min_count = 1)
    #input_text_vec = model.wv

    #input_text_vec.save('keyed.kv')
    #in_txt_vec = Word2Vec.load('keyed.kv')



    #bigram_transformer = Phrases(clean_text)
    #model = Word2Vec(bigram_transformer[clean_text], min_count = 1)
    result = model.wv.index_to_key[:5]
    print(result)

    return result
