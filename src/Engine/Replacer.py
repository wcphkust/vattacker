import random
import math
import nltk
from nltk.parse import CoreNLPParser
from nltk.corpus import wordnet
from Utils.synonyms import *


class Replacer(object):
    """
    Replace by synonyms or antonyms in the negative form
    """

    def __init__(self, text):
        self.text = text
        self.tokens = nltk.word_tokenize(text)
        parser = CoreNLPParser(url='http://localhost:8999')
        self.syntax_tree = list(parser.parse(nltk.word_tokenize(self.text)))[0]

    def synonyms_mutation(self):
        """
        replace the adverbs and adjectives by their synonyms
        :return: the text after synonyms mutation
        """
        subtrees = self.syntax_tree.subtrees(lambda t: t.height() == 3)
        for subtree in subtrees:
            subsubtrees = list(subtree.subtrees())
            for subsubtree in subsubtrees:
                if subsubtree._label in ['JJ', 'RB']:
                    word = subsubtree.__getitem__(0)
                    candidates_with_sim = syn(word, 10)
                    candidates = set(candidates_with_sim.keys())
                    if not candidates:
                        continue
                    new_word = max(candidates_with_sim, key=lambda s: candidates_with_sim[s])
                    subsubtree.__setitem__(0, new_word)
        return " ".join(self.syntax_tree.leaves())

    def antonyms_mutation(self):
        """
        replace the adverbs and adjectives by their synonyms in the negative forms
        :return: the text after antonyms mutation
        """
        return
