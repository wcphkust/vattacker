from copy import deepcopy
from Engine.TextMutator import *
from Engine.AttackReportor import *

class FuzzAttacker(object):
    """
    The core engine of vattacker
    """

    def __init__(self, text, max_attack_num = 10):
        self.text = text
        self.max_attack_num = max_attack_num
        self.mutationhistory = []
        self.successfulattack = None
        self.attack()

    def attack(self):
        """
        attack sentiment analysis system by mutating the text
        :return: the successful adversarial example
        """
        ar = AttackReportor(self.text)
        self.mutationhistory.append(deepcopy(ar))
        print("-----------------------------------------------------------------")
        print(str(len(self.mutationhistory)) + " " + str(ar.text))
        print(str(ar.polarity))
        print(str(ar.result))
        print("-----------------------------------------------------------------")

        while True:
            prear = deepcopy(ar)
            textmutator = TextMutator(self.text, self.mutationhistory)
            ar = AttackReportor(textmutator.newtext)
            self.mutationhistory.append(deepcopy(ar))
            print("-----------------------------------------------------------------")
            print(str(len(self.mutationhistory)) + " " + str(ar.text))
            print(str(ar.polarity))
            print(str(ar.result))
            print("-----------------------------------------------------------------")
            if ar.polarity != prear.polarity:
                self.successfulattack = deepcopy(ar)
                break
            if len(self.mutationhistory) > self.max_attack_num:
                break
