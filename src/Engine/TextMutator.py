from random import random
from math import floor
from itertools import groupby
import nltk

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
        original_reportor = self.mutationhistory[0]
        original_result, original_polarity = original_reportor.fetch_report()
        best_seed = original_reportor.text
        minpolarity = original_result[original_polarity]
        for mutation_reportor in self.mutationhistory:
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
        mutation_strategy = random.choice((0, 1))
        if mutation_strategy == 0:
            return self.mutate_universal_trigger()
        elif mutation_strategy == 1:
            return self.mutate_punctuation(random.choice((2, 3, 4)))

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
