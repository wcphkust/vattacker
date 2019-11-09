from Engine.SentimentIntensityAnalyzer import *
from Engine.FuzzAttacker import *
from Engine.Tagger import *
from copy import deepcopy


class SingleTest(object):
    """
    test single sentence or short paragraph
    """

    def __init__(self, text, is_print = True):
        self.text = deepcopy(text)
        self.is_print = is_print
        self.mutation_history, self.successful_attack = self.test()
        print("\n\n Initial Single Analysis Done!")

    def test(self):
        # TODO
        fuzz_attacker = FuzzAttacker(self.text, self.is_print)
        return fuzz_attacker.mutation_history, fuzz_attacker.success_attack
