from sklearn.datasets import fetch_20newsgroups
from bs4 import BeautifulSoup
import nltk, re
from gensim.models import Word2Vec
from nltk.corpus import wordnet as wn
import heapq
import os

news = fetch_20newsgroups(subset='all')
X, y = news.data, news.target


def news_to_sentences(news):
    # Preprocess the corpus
    news_text = BeautifulSoup(news, 'lxml').get_text()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(news_text)
    sentences = []
    for sent in raw_sentences:
        sentences.append(re.sub('[^a-zA-Z]', ' ', sent.lower().strip()).split())
    return sentences


def model_w2v():
    # train a w2v vector
    model_file_name = "word2vec.model"
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
        num_features = 300
        min_word_count = 20
        num_workers = 10
        context = 5
        down_sampling = 1e-3
        model = Word2Vec(sentences, workers=num_workers, size=num_features,
                         min_count=min_word_count, window=context, sample=down_sampling)
        model.init_sims(replace=True)
        print('OK')
        model.save(model_file_name)
        print('MODEL SAVED')
    return model


def query_synset(word_input):
    syn = list()
    ant = list()
    for syn_set in wn.synsets(word_input):
       for lemma in syn_set.lemmas():
            syn.append(lemma.name())
            if lemma.antonyms():
                ant.append(lemma.antonyms()[0].name())
    print('Synonyms: ' + str(syn))
    return syn


def cal_sim(syn, model, word_input):
    syn_sim = list()
    for syn in syn:
        # print(syn)
        try:
            syn_sim = model.n_similarity(word_input,str(syn))
            syn_sim.append(syn_sim)
            print(syn, syn_sim)
        except KeyError:
            print ("one word not in vocabulary: ", syn)
            syn_sim = 0
            syn_sim.append(syn_sim)
            print(syn, syn_sim)
    return syn_sim


def get_top_k(syn2, syn_sim2, k):
    # solve the problem of non-enough values
    if k > len(syn_sim2):
        k = len(syn_sim2)
        print('k>=length, parts of results will be shown')
    else:
        pass
    max_val_index_list = map(syn2.index, heapq.nlargest(k, syn2))
    syn_top_k = list()
    syn_sim_top_k = list()
    for index in max_val_index_list:
        print(syn2[index], syn_sim2[index])
        syn_top_k.append(syn2[index])
        syn_sim_top_k.append(syn_sim2[index])
    print(syn_top_k, syn_sim_top_k)
    return syn_top_k, syn_sim_top_k


def duplicate_remove(syn, word_input):
    syn1 = list(set(syn))
    syn2 = syn1
    syn2.remove(word_input)
    return syn2


def syn(word_input, k):
    model = model_w2v()
    syn = query_synset(word_input)
    syn2 = duplicate_remove(syn, word_input)
    syn_sim2 = cal_sim(syn2, model, word_input)
    print(syn_sim2)
    syn_top_k, syn_sim_top_k = get_top_k(syn2, syn_sim2, k)
    return syn_top_k, syn_sim_top_k
