from Engine.FuzzAttacker import *
from Engine.Tagger import *
from copy import deepcopy


class SingleTest(object):
    """
    test single sentence or short paragraph
    """

    def __init__(self, tool, text, is_nonrandom_mutation=True, is_print=True, max_attack_num=5):
        self.tool = tool
        self.is_nonrandom_mutation = is_nonrandom_mutation
        self.is_print = is_print
        self.text = deepcopy(text)
        self.max_attack_num = max_attack_num
        self.mutation_history, self.successful_attack = self.test()
        print("\n\n Initial Single Analysis Done!")

    def test(self):
        # TODO
        fuzz_attacker = FuzzAttacker(self.tool, self.text, self.is_nonrandom_mutation, self.is_print, self.max_attack_num)
        return fuzz_attacker.mutation_history, fuzz_attacker.success_attack
