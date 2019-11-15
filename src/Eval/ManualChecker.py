from Utils.IO import *
from copy import deepcopy


class ManualChecker(object):
    """
    check the adversarial manually
    """

    def __init__(self, input_filepath, output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath
        self.adversarial_result = load_adversarial_example(self.input_filepath)
        self.check_result = self.check()
        export_check_result(self.output_filepath, self.check_result)

    def check(self):
        """
        get the input from labeler
        :return: adversarial result with manual-labeled types
        """
        check_result = []
        for item in self.adversarial_result:
            new_item = {"original_text": item["original_text"], "adversarial_text": item["adversarial_text"]}

            print("-----------------------------------------------------------")
            print("original_text: " + item["original_text"])
            print("adversarial_text: " + item["adversarial_text"])
            print("-----------------------------------------------------------")
            print("Please input A or B or C or D")
            print("A: totally same")
            print("B: sentimental different")
            print("C: illegal grammar")
            print("D: Others")
            print("-----------------------------------------------------------")

            while True:
                item_type = input()
                if item_type in ["A", "B", "C", "D"]:
                    new_item["type"] = item_type
                    break
                else:
                    print("Invalid input. Please input A or B or C or D")
            check_result.append(deepcopy(new_item))
        return check_result
