from copy import deepcopy
from Engine.TextMutator import *
from Engine.AttackReportor import *

class FuzzAttacker(object):
    """
    The core engine of vattacker
    """

    def __init__(self, text):
        self.text = text
        self.mutationhistory = []
        self.successfulattack = None


    def attack(self):
        """
        attack sentiment analysis system by mutating the text
        :return: the successful adversarial example
        """
        ar = AttackReportor(self.text)
        self.mutationhistory.append(deepcopy(ar))

        while True:
            prear = deepcopy(ar)
            textmutator = TextMutator(self.text, self.mutationhistory)
            ar = AttackReportor(textmutator.newtext)
            self.mutationhistory.append(deepcopy(ar))
            if (ar.polarity != prear.polarity):
                self.successfulattack = deepcopy(ar)
                break