from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class AttackReportor(object):
    """
    Record the mutated text and the attack result
    """

    def __init__(self, text, tool):
        """
        :param text: mutated text
        """
        self.text = text
        self.tool = tool
        self.result, self.polarity = self.fetch_report()

    def fetch_report(self):
        """
        attach the sentiment analysis system
        :return: the sentiment syntax tree
        """
        sentiment_result = None
        polarity = None
        if self.text is None or self.tool is None:
            return sentiment_result, polarity
        if self.tool == "vader":
            vader_sa = SentimentIntensityAnalyzer()
            score = vader_sa.polarity_scores(self.text)
            polarity = max(score, key=lambda s: score[s])
            sentiment_result = score[polarity]
        elif self.tool == "textblob":
            testimonial = TextBlob(self.text)
            sentiment_result = testimonial.sentiment.polarity
            if sentiment_result > 0:
                polarity = "pos"
            elif sentiment_result < 0:
                polarity = "neg"
            else:
                polarity = "neu"
        return sentiment_result, polarity
