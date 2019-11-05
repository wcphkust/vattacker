from copy import deepcopy
from Engine.TextMutator import *
from Engine.AttackReportor import *

class FuzzAttacker(object):
    """
    The core engine of vattacker
    """

    def __init__(self, text, max_attack_num = 20):
        self.text = text
        self.max_attack_num = max_attack_num
        self.mutation_history = []
        self.history_pool = set([])
        self.success_attack = None
        self.attack()

    def attack(self):
        """
        attack sentiment analysis system by mutating the text
        :return: the successful adversarial example
        """
        ar = AttackReportor(self.text)
        self.mutation_history.append(deepcopy(ar))
        print("-----------------------------------------------------------------")
        print(str(len(self.mutation_history)) + " " + str(ar.text))
        print(str(ar.polarity))
        print(str(ar.result))
        print("-----------------------------------------------------------------")

        while True:
            prear = deepcopy(ar)
            textmutator = TextMutator(self.text, self.mutation_history, self.history_pool)
            ar = AttackReportor(textmutator.new_text)
            self.mutation_history.append(deepcopy(ar))
            self.history_pool.add(textmutator.new_text)
            print("-----------------------------------------------------------------")
            print(str(len(self.mutation_history)) + " " + str(ar.text))
            print(str(ar.polarity))
            print(str(ar.result))
            print("-----------------------------------------------------------------")
            if ar.polarity != prear.polarity:
                self.success_attack = deepcopy(ar)
                break
            if len(self.mutation_history) > self.max_attack_num:
                break
