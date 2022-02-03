from gensim.models import Word2Vec, KeyedVectors


def sim_word(clean_text):

    #model = Word2Vec(sentences = clean_text, vector_size = 100, min_count = 1)
    #input_text_vec = model.wv

    #input_text_vec.save('keyed.kv')
    in_txt_vec = KeyedVectors.load('keyed.kv')
    result = in_txt_vec.closer_than('wału', 'skręcanie')

    print(result)

    return 0
