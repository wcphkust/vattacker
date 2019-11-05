import random
import math
import nltk
from nltk.parse import CoreNLPParser
from nltk.corpus import wordnet   #Import wordnet from the NLTK


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
            for i in range(len(subsubtrees) - 1):
                if subsubtrees[i]._label in ['JJ', 'RB']:
                    word = subsubtrees[i].__getitem__(0)
                    print("word")
                    print(word)
                    candidates = wordnet.synsets(word)
                    syn = []
                    for candidate in candidates:
                        for lemma in candidate.lemmas():
                            syn.append(lemma.name())
                    if not syn:
                        continue
                    new_word = random.choice(syn)
                    subsubtrees[i].__setitem__(0, new_word)
        return self.syntax_tree.leaves()

    def antonyms_mutation(self):
        """
        replace the adverbs and adjectives by their synonyms in the negative forms
        :return: the text after antonyms mutation
        """
        return
