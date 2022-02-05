import gensim
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.models import Word2Vec, LdaModel
from gensim.models import KeyedVectors
from gensim.test.utils import datapath, get_tmpfile

def vocabulary(most_fr):

    #model = Word2Vec(sentences = clean_txt, vector_size = 100, window = 5, min_count = 2, workers = 4)
    #model.save("tematy.model")
    model = KeyedVectors.load("keyed.kv")

    for mf in most_fr:
    #vector = model.wv['zawodnik']
        sims = model.most_similar(mf, topn = 4)
        print('podobne do '+mf+' :')
    # print(vector)
        for sim in sims:
          print(sim)
    # ------^tu dziala, mozna cos kminic z wykrywaniem tematu^----

    # print('dzialam')
    # path_to_wiki_dump = datapath("plwiki-latest-flow.xml.bz2")
    # corpus_path = get_tmpfile("wiki-corpus.mm")
    #
    # wiki = WikiCorpus(path_to_wiki_dump)
    # MmCorpus.serialize(corpus_path, wiki)
    #
    # print('skonczylem')
