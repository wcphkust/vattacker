from Utils.IO import *
from Eval.SingleTest import *

class BatchTest(object):
    """
    test on a testing dataset
    """

    def __init__(self, filepath):
        self.texts = import_data(filepath)
        self.total = len(self.texts)
        self.success_attack = []
        self.failed_attack = []
        self.success_result = []
        self.test()
        self.success = len(self.success_attack)
        self.fail = len(self.failed_attack)
        export_success_attack(filepath, self.success_result)

    def test(self):
        """
        batch test
        """
        trys = self.texts[:30]
        self.texts = trys
        for text in self.texts:
            single_test = SingleTest(text, False)
            if single_test.successfulattack is not None:
                self.success_attack.append([deepcopy(single_test.mutationhistory), deepcopy(single_test.successfulattack)])
                single_result = {"original_text": text, "adversarial text": single_test.successfulattack}
                self.success_result.append(single_result)
                print("successful attack")
            else:
                self.failed_attack.append([deepcopy(single_test.mutationhistory), deepcopy(single_test.successfulattack)])
                print("failed attack")
            print(str(len(self.success_attack)) + " / " + str(len(self.success_attack) + len(self.failed_attack))
                  + " / " + str(self.total))


