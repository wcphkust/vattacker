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
        self.test()
        self.success = len(self.success_attack)
        self.fail = len(self.failed_attack)

    def test(self):
        """
        batch test
        """
        for text in self.texts:
            single_test = SingleTest(text, False)
            if single_test.successfulattack is not None:
                self.success_attack.append([deepcopy(single_test.mutationhistory), deepcopy(single_test.successfulattack)])
                print("successful attack")
            else:
                self.failed_attack.append([deepcopy(single_test.mutationhistory), deepcopy(single_test.successfulattack)])
                print("failed attack")
            print(str(len(self.success_attack)) + " / " + str(len(self.success_attack) + len(self.failed_attack))
                  + " / " + str(len(self.total)))
