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
        self.polarity = None


    def fetch_report(self):
        """
        attach the sentiment analysis system
        :return: the sentiment syntax tree
        """
        # TODO
        result = None
        polarity = None
        return result, polarity
