from copy import deepcopy
from Engine.TextMutator import *
from Engine.AttackReportor import *


class FuzzAttacker(object):
    """
    The core engine of vattacker
    """

    def __init__(self, tool, text, mode=True, is_print=True, max_attack_num=5):
        self.tool = tool
        self.text = text
        self.max_attack_num = max_attack_num
        self.mutation_history = []
        self.history_pool = set([])
        self.success_attack = None
        self.is_print = is_print
        self.mode = mode
        self.attack()

    def attack(self):
        """
        attack sentiment analysis system by mutating the text
        :return: the successful adversarial example
        """
        ar = AttackReportor(self.text, self.tool)
        mutator_weight = [1, 1, 1, 1, 1, 1]
        self.mutation_history.append(deepcopy(ar))
        if self.is_print:
            print("-----------------------------------------------------------------")
            print(str(len(self.mutation_history)) + " " + str(ar.text))
            print(str(ar.polarity))
            print(str(ar.result))
            print("-----------------------------------------------------------------")

        while True:
            prear = deepcopy(ar)
            text_mutator = TextMutator(mutator_weight, self.text, self.mutation_history, self.history_pool, "nonrandom")
            ar = AttackReportor(text_mutator.new_text, self.tool)
            self.mutation_history.append(deepcopy(ar))
            self.history_pool.add(text_mutator.new_text)
            if self.is_print:
                print("-----------------------------------------------------------------")
                print(str(len(self.mutation_history)) + " " + str(ar.text))
                print(str(ar.polarity))
                print(str(ar.result))
                print("-----------------------------------------------------------------")
            if abs(ar.result.polarity) < abs(prear.result.polarity):
                mutator_weight[text_mutator.mutator_strategy] += 1
            if ar.polarity != prear.polarity:
                self.success_attack = deepcopy(ar)
                break
            if len(self.mutation_history) > self.max_attack_num:
                break
