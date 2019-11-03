from Engine.SentimentIntensityAnalyzer import *


class SingleTest(object):
    """
    test single sentence or short paragraph
    """

    def __init__(self, text):
        self.text = text
        # TODO
        self.mutationhistory, self.successfulattack = self.test()
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(text)
        print("{:-<65} {}".format(text, str(vs)))
        print("\n\n Single Test Done!")


    def test(self):
        # TODO
        return None, None
        # fuzzattacker = FuzzAttacker(self.text)
        # return fuzzattacker.mutationhistory, fuzzattacker.successfulattack