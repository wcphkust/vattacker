import nltk

class Tagger(object):
    """
    Tag the text
    """

    def __init__(self, text):
        self.text = text
        self.tokens = nltk.pos_tag(text)
        self.pos_tag = None
        self.conjstructure_tag = None
        self.punctuation_tag = None

    def pos_tagging(self):
        if self.pos_tag is None:
            self.pos_tag = nltk.pos_tag(self.tokens)
        return self.pos_tag

    def conjstructure_tagging(self):
        # TODO
        return

    def punctuation_tagging(self):
        # TODO
        return