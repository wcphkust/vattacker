from Engine.SentimentIntensityAnalyzer import *


class AttackReportor(object):
    """
    Record the mutated text and the attack result
    """

    def __init__(self, text):
        """
        :param text: mutated text
        """
        self.text = text
        self.result, self.polarity = self.fetch_report()

    def fetch_report(self):
        """
        attach the sentiment analysis system
        :return: the sentiment syntax tree
        """
        # TODO
        #
        sas = SentimentIntensityAnalyzer()
        vs = sas.polarity_scores(self.text)

        """
        sentiment_dict = \
            {"neg": round(neg, 3),
             "neu": round(neu, 3),
             "pos": round(pos, 3),
             "compound": round(compound, 4)}
        """

        result = vs
        polarity = max(result, key=result.get)
        return result, polarity
