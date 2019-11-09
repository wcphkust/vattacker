from random import random, choice
from math import floor
from itertools import groupby
import nltk
import numpy as np
import pandas as pd
from Engine.Tagger import *
from Engine.Parser import *
from Engine.Replacer import *


class TextMutator(object):
    """
    Mutate the text to change the sentiment valence to the opposite polarity
    """

    def __init__(self, mutator_weight, original_text, mutate_history, history_pool, mode="nonrandom"):
        """
        :param original_text: original sentence or short paragraph
        :param mutate_history: a sequence of mutator
        :param history_pool: the set of the text for attack in history
        """
        if not isinstance(original_text, str):
            text = str(original_text).encode('utf-8')
        self.mutator_weight = mutator_weight
        self.original_text = original_text
        self.mutate_history = mutate_history
        self.history_pool = history_pool
        self.mode = mode
        self.new_text, self.mutator_strategy = self.mutate()

    def select_best_seed(self):
        original_reportor = self.mutate_history[0]
        original_result, original_polarity = original_reportor.fetch_report()
        best_seed = original_reportor.text
        min_polarity = original_result.polarity
        for mutation_reportor in self.mutate_history:
            result, polarity = mutation_reportor.fetch_report()
            if abs(result.polarity) < abs(min_polarity):
                min_polarity = result.polarity
                best_seed = mutation_reportor.text
        return best_seed

    def mutate(self):
        """
        :return: return the text after mutation
        """
        # TODO
        new_text = None
        try_num = 0
        mutation_strategy = -1
        while new_text is None and try_num < 20:
            try_num += 1
            mutation_strategy = -1
            if self.mode == "nonrandom":
                mutation_strategy = \
                    np.random.choice([0, 1, 2, 3, 4, 5], replace=True, p=[(weight/sum(self.mutator_weight)) for weight in self.mutator_weight])
            elif self.node == "random":
                mutation_strategy = random.choice([0, 1, 2, 3, 4, 5])
            if mutation_strategy == 0:
                new_text = self.mutate_delete_adverb()
            elif mutation_strategy == 1:
                new_text = self.mutate_capitalization()
            elif mutation_strategy == 2:
                new_text = self.mutate_conjunctions()
            elif mutation_strategy == 3:
                new_text = self.mutate_synonyms()
            elif mutation_strategy == 4:
                new_text = self.mutate_add_whitespace()
            elif mutation_strategy == 5:
                new_text = self.mutate_punctuation(random.choice([2, 3, 4]))
        if new_text is None:
            new_text = self.original_text
        return new_text, mutation_strategy

    def mutate_universal_trigger(self):
        """
        universal trigger
        :return: the text after universal trigger
        """
        tokens = nltk.word_tokenize(self.original_text)
        return str(self.original_text) + " " + tokens[(floor(random() * 1000)) % len(tokens)]

    def mutate_add_whitespace(self):
        """
        add whitespace to trigger
        :return: the text after add whitespace
        """
        tokens = nltk.word_tokenize(self.original_text)
        new_text = ""
        for token in tokens:
            new_text += token
            whitespace = " " * random.choice((1, 2))
            new_text += whitespace
        return new_text

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

    def mutate_synonyms(self):
        """
        replace the adverbs and adjectives in the text
        :return: the text after the replacement
        """
        seed = self.select_best_seed()
        replacer = Replacer(seed)
        return replacer.synonyms_mutation()
