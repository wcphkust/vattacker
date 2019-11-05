from random import random, choice
from math import floor
from itertools import groupby
import nltk
from Engine.Tagger import *
from Engine.Parser import *


class TextMutator(object):
    """
    Mutate the text to change the sentiment valence to the opposite polarity
    """

    def __init__(self, originaltext, mutatehistory):
        """
        :param originaltext: original sentence or short paragraph
        :param mutatehistory: a sequence of mutator
        """
        if not isinstance(originaltext, str):
            text = str(originaltext).encode('utf-8')
        self.originaltext = originaltext
        self.mutatehistory = mutatehistory
        self.newtext = self.mutate()

    def select_best_seed(self):
        original_reportor = self.mutatehistory[0]
        original_result, original_polarity = original_reportor.fetch_report()
        best_seed = original_reportor.text
        minpolarity = original_result[original_polarity]
        for mutation_reportor in self.mutatehistory:
            result, polarity = mutation_reportor.fetch_report()
            if result[polarity] < minpolarity:
                minpolarity = result[polarity]
                best_seed = mutation_reportor.text
        return best_seed

    def mutate(self):
        """
        :return: return the text after mutation
        """
        # TODO
        mutation_strategy = choice((0, 1, 2))
        if mutation_strategy == 0:
            return self.mutate_delete_adverb()
        elif mutation_strategy == 1:
            return self.mutate_capitalization()
        elif mutation_strategy == 2:
            return self.mutate_conjunctions()

    def mutate_universal_trigger(self):
        """
        universal trigger
        :return: the text after universal trigger
        """
        tokens = nltk.word_tokenize(self.originaltext)
        return str(self.originaltext) + " " + tokens[(floor(random() * 1000)) % len(tokens)]

    def mutate_punctuation(self, k):
        """
        change the occurrence number of some punctuations, including ? and !
        :param k: occurrence number
        :return: the text after punctuation mutation
        """
        seed = self.select_best_seed()
        seed_tokens = nltk.word_tokenize(seed)
        tokens = [x[0] for x in groupby(seed_tokens)]
        new_text = " ".join(tokens).replace(" !", "!"*k).replace(" ?", "?"*k)
        return new_text

    def mutate_delete_adverb(self):
        """
        remove adverbs in the text
        :return: the text after removing adverbs
        """
        seed = self.select_best_seed()
        tagger = Tagger(seed)
        pos_tag = tagger.pos_tagging()
        new_pos_tag = [(token, tag) for (token, tag) in pos_tag if tag != "RB"]
        tokens = [token for (token, tag) in new_pos_tag]
        new_text = " ".join(tokens)
        return new_text

    def mutate_capitalization(self):
        """
        capitalize the adverbs and adjectives
        :return: the text after capitalization
        """
        seed = self.select_best_seed()
        tagger = Tagger(seed)
        pos_tag = tagger.pos_tagging()
        new_pos_tag = []
        for (token, tag) in pos_tag:
            if tag in ["RB", "RBR", "RBS", "JJ", "JJR", "JJS"]:
                new_pos_tag.append((token.upper(), tag))
            else:
                new_pos_tag.append((token, tag))
        tokens = [token for (token, tag) in new_pos_tag]
        new_text = " ".join(tokens)
        return new_text

    def mutate_conjunctions(self):
        """
        mutate the conjunctions in the text
        :return: the text after conjunction mutation
        """
        seed = self.select_best_seed()
        parser = Parser(seed)
        return parser.mutate_conjunction()
