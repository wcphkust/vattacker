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
        # TODO
        self.mutationhistory, self.successfulattack = self.test()
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(self.text)
        print("{:-<65} {}".format(text, str(vs)))

        tagger = Tagger(self.text)
        print(tagger.pos_tagging())
        print(tagger.punctuation_tagging())
        print("\n\n Initial Single Analysis Done!")

    def test(self):
        # TODO
        fuzz_attacker = FuzzAttacker(self.text, self.is_print)
        return fuzz_attacker.mutation_history, fuzz_attacker.success_attack
