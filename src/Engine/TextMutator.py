from random import random

class TextMutator(object):
    """
    Mutate the text to change the sentiment valence to the opposite polarity
    """

    def __init__(self, originaltext, mutatehistory):
        """
        :param originaltext: original sentence or short paragraph
        :param mutatehistory: a sequence of mutator
        """
        if not isinstance(originaltext, str):
            text = str(originaltext).encode('utf-8')
        self.originaltext = originaltext
        self.mutatehistory = mutatehistory
        self.newtext = self.mutate()

    def mutate(self):
        """
        :return: return the text after mutation
        """
        # TODO
        return str(self.originaltext) + " " + str(random.random())
