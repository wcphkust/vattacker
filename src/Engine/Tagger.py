import nltk


class Tagger(object):
    """
    Tag the text
    """

    def __init__(self, text):
        self.text = text
        self.tokens = nltk.word_tokenize(text)
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
        if self.punctuation_tag is None:
            if self.pos_tag is None:
                self.pos_tagging()
            self.punctuation_tag = []
            for (token, tag) in self.pos_tag:
                if tag != '.':
                    self.punctuation_tag.append((token, "word"))
                elif token == "!":
                    self.punctuation_tag.append((token, "am punc"))
                elif token == "?":
                    self.punctuation_tag.append((token, "ne punc"))
        return self.punctuation_tag
