from sklearn.datasets import fetch_20newsgroups
from bs4 import BeautifulSoup
import nltk, re
from gensim.models import Word2Vec
from nltk.corpus import wordnet as wn #Import wordnet from the NLTK
import heapq # for top-K problems
import os

news = fetch_20newsgroups(subset='all')
X, y = news.data, news.target
# nltk.download('punkt')

# Preprocess the corpus
def news_to_sentences(news):
    news_text = BeautifulSoup(news, 'lxml').get_text()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(news_text)

    sentences = []
    for sent in raw_sentences:
        sentences.append(re.sub('[^a-zA-Z]', ' ', sent.lower().strip()).split())
    return sentences

#train a w2v vector
def model_w2v():
    model_file_name = "word2vec.model"# the name of the model
    if os.path.isfile(model_file_name):
        print("model exist. Loading the model now")
        model = Word2Vec.load("word2vec.model")
        print('OK')
    else:
        print("model not exist. Training the model now")
        sentences = []
        for x in X:
            sentences += news_to_sentences(x)
        # parameters
        num_features = 300  #
        min_word_count = 20  #
        num_workers = 10  #
        context = 5  #
        downsampling = 1e-3  #

        model = Word2Vec(sentences, workers=num_workers, size=num_features,
                         min_count=min_word_count, window=context, sample=downsampling)
        model.init_sims(replace=True)
        print('OK')
        model.save(model_file_name)
        print('MODEL SAVED')
    return model

def query_synset(word_input):
    SYN = list()
    ANT = list()
    for synset in wn.synsets(word_input):
       for lemma in synset.lemmas():
          SYN.append(lemma.name())    #add the synonyms
          if lemma.antonyms():    #When antonyms are available, add them into the list
            ANT.append(lemma.antonyms()[0].name())
    print('Synonyms: ' + str(SYN))
    return SYN

def cal_sim(SYN, model, word_input):
    SYN_SIM = list()
    for syn in SYN:
        # print(syn)
        try:
            syn_sim = model.n_similarity(word_input,str(syn))
            SYN_SIM.append(syn_sim)
            print(syn, syn_sim)
        except KeyError:
            print ("one word not in vocabulary: ", syn)
            syn_sim = 0
            SYN_SIM.append(syn_sim)
            print(syn, syn_sim)
    return SYN_SIM

def get_top_k(SYN2,SYN_SIM2, k):
    # solve the problem of non-enough values
    if k > len(SYN_SIM2):
        k = len(SYN_SIM2)
        print('k>=length, parts of results will be shown')
    else:
        pass
    max_val_index_list = map(SYN2.index, heapq.nlargest(k, SYN2))
    SYN_top_k = list()
    SYN_SIM_top_k = list()
    for index in max_val_index_list:
        print(SYN2[index], SYN_SIM2[index])
        SYN_top_k.append(SYN2[index])
        SYN_SIM_top_k.append(SYN_SIM2[index])
    print(SYN_top_k, SYN_SIM_top_k)
    return SYN_top_k, SYN_SIM_top_k

def duplicate_remove(SYN, word_input):
    SYN1 = list(set(SYN))  # remove duplicated items SYN->SYN1
    # print(SYN1)
    SYN2 = SYN1
    SYN2.remove(word_input)
    return SYN2

def syn(word_input, k):
    model = model_w2v()
    SYN = query_synset(word_input)
    SYN2 = duplicate_remove(SYN, word_input)
    SYN_SIM2 = cal_sim(SYN2, model, word_input)
    print(SYN_SIM2)
    SYN_top_k, SYN_SIM_top_k = get_top_k(SYN2, SYN_SIM2, k)
    return SYN_top_k, SYN_SIM_top_k