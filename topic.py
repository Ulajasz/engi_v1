from gensim.models import Word2Vec
import pickle

def topic(input_words):

    model = Word2Vec.load('wiki.word2vec.model')

    base_path = r"F:\Inżynierka\engi_v1\topics"
    bs = "\\"
    temp = ".pkl"
    topic_list = ["gotowanie", "historia", "motoryzacja", "nauka", "polityka", "popkultura", "sport", "technologia", "zdrowie", "środowisko"]
    similarity = []
    for top in topic_list:
        with open(base_path+bs+top+temp, "rb") as f:
            topic = pickle.load(f)
            sim_topic = model.wv.n_similarity(input_words, topic)
            if sim_topic < 0:
                sim_topic = 0
            similarity.append([top, (round(sim_topic*100))])

    return similarity