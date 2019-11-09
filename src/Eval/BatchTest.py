from Utils.IO import *
from Eval.SingleTest import *

class BatchTest(object):
    """
    test on a testing dataset
    """

    def __init__(self, filepath, is_nonrandom_mutation):
        self.texts = import_data(filepath)
        self.total = len(self.texts)
        self.success_attack = []
        self.failed_attack = []
        self.success_result = []
        self.test()
        self.success = len(self.success_attack)
        self.fail = len(self.failed_attack)
        self.is_nonrandom_mutation = is_nonrandom_mutation
        export_success_attack(filepath, self.success_result)

    def test(self):
        """
        batch test
        """
        for text in self.texts:
            single_test = SingleTest(text, self.is_nonrandom_mutation, False)
            if single_test.successful_attack is not None:
                self.success_attack.append([deepcopy(single_test.mutation_history),
                                            deepcopy(single_test.successful_attack)])
                single_result = {"original_text": text, "adversarial text": single_test.successful_attack.text}
                self.success_result.append(single_result)
                print("successful attack")
            else:
                self.failed_attack.append([deepcopy(single_test.mutation_history), deepcopy(single_test.successful_attack)])
                print("failed attack")
            print(str(len(self.success_attack)) + " / " + str(len(self.success_attack) + len(self.failed_attack))
                  + " / " + str(self.total))
