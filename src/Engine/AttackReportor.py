from Engine.SentimentIntensityAnalyzer import *
from textblob import TextBlob

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
        testimonial = TextBlob(self.text)
        sentiment_result = testimonial.sentiment
        polarity = "pos" if sentiment_result.polarity > 0 else "neg"
        return sentiment_result, polarity
