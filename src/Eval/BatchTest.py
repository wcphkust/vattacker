from copy import deepcopy
from Eval.SingleTest import *

class BatchTest(object):
    """
    test on a testing dataset
    """

    def __init__(self, texts):
        self.texts = texts
        self.total = len(texts)
        self.successattack = []
        self.failedattack = []
        self.test()
        self.success = len(self.successattack)
        self.fail = len(self.failedattack)


    def test(self):
        """
        batch test
        """
        for text in self.texts:
            singletest = SingleTest(text)
            if singletest.successfulattack is not None:
                self.successattack.append([deepcopy(singletest.mutationhistory), deepcopy(singletest.successfulattack)])
            else:
                self.failedattack.append([deepcopy(singletest.mutationhistory), deepcopy(singletest.successfulattack)])
