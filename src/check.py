import sys
import os
from Eval.ManualChecker import *

if __name__ == '__main__':
    input_filepath = os.path.normpath(os.path.join(os.getcwd() + "../../../vattacker_data/result/",
                                                   sys.argv[sys.argv.index("-resid") + 1]))
    output_filepath = input_filepath
    manual_checker = ManualChecker(input_filepath, output_filepath)


