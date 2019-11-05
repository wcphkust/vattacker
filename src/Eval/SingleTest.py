from Engine.SentimentIntensityAnalyzer import *
from Engine.FuzzAttacker import *
from Engine.Tagger import *
from copy import deepcopy


class SingleTest(object):
    """
    test single sentence or short paragraph
    """

    def __init__(self, text):
        self.text = deepcopy(text)
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
        fuzz_attacker = FuzzAttacker(self.text)
        return fuzz_attacker.mutation_history, fuzz_attacker.success_attack
