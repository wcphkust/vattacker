import sys
from Utils.IO import *
from Eval.SingleTest import *


class BatchTest(object):
    """
    test on a testing dataset
    """

    def __init__(self, tool, test_root, test_id, is_nonrandom_mutation, max_attack_num=5):
        self.tool = tool
        self.test_root = test_root
        self.test_id = test_id
        self.test_filepath = os.path.normpath(self.test_root + "/test/" + self.test_id)
        self.texts = import_data(self.test_filepath)
        self.total = len(self.texts)
        self.max_attack_num = max_attack_num
        self.success_attack = []
        self.failed_attack = []
        self.success_result = []
        self.is_nonrandom_mutation = is_nonrandom_mutation
        self.test()
        self.success = len(self.success_attack)
        self.fail = len(self.failed_attack)
        self.test_result_filepath = os.path.normpath(self.test_root + "/result/" + self.tool + "_" + self.test_id)
        export_success_attack(self.test_result_filepath, self.success_result)

    def test(self):
        """
        batch test
        """
        attack_num = 0
        for text in self.texts:
            single_test = SingleTest(self.tool, text, self.is_nonrandom_mutation, False, self.max_attack_num)
            if single_test.successful_attack is not None:
                self.success_attack.append([deepcopy(single_test.mutation_history),
                                            deepcopy(single_test.successful_attack)])
                single_result = {"original_text": text, "adversarial_text": single_test.successful_attack.text}
                self.success_result.append(single_result)
                print("successful attack")
                attack_num += len(single_test.mutation_history)
            else:
                self.failed_attack.append([deepcopy(single_test.mutation_history), deepcopy(single_test.successful_attack)])
                print("failed attack")
                attack_num += len(single_test.mutation_history)
            print(str(len(self.success_attack)) + " / " + str(len(self.success_attack) + len(self.failed_attack))
                  + " / " + str(self.total))
            print("total attacks: " + str(attack_num))
