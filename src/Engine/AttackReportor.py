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
        print(self.text)
        print(self.tool)
        # if self.text is None or self.tool is None:
        #     return sentiment_result, polarity
        print("----------------------------FUCK---BEGIN--------------------------------------")
        if self.tool == "vader":
            vader_sa = SentimentIntensityAnalyzer()
            score = vader_sa.polarity_scores(self.text)
            print("VADER result")
            print(score)
            polarity = max(score, key=lambda s: score[s])
            sentiment_result = score[polarity]
            print("polarity")
            print(polarity)
            print("result")
            print(sentiment_result)
        elif self.tool == "textblob":
            testimonial = TextBlob(self.text)
            sentiment_result = testimonial.sentiment.polarity
            print("TextBlob result")
            print(sentiment_result)
            if sentiment_result > 0:
                polarity = "pos"
            elif sentiment_result < 0:
                polarity = "neg"
            else:
                polarity = "neu"
        print("----------------------------FUCK---RETURN--------------------------------------")
        print(sentiment_result)
        print(polarity)
        print("----------------------------FUCK---END--------------------------------------")
        return sentiment_result, polarity
