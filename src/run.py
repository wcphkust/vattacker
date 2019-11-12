import sys
from Eval.SingleTest import *
from Eval.BatchTest import *

if __name__ == '__main__':
    is_nonrandom_mutation = True
    max_attack_num = 5
    if ("-max" in sys.argv):
        max_attack_num = sys.argv[sys.argv.index("-max") + 1]
    if ("-random" in sys.argv):
        is_nonrandom_mutation = False
    if ("-single" in sys.argv):
        single_test = SingleTest(sys.argv[sys.argv.index("-single") + 1], is_nonrandom_mutation, True, int(max_attack_num))
    elif ("-batch" in sys.argv):
        filepath = os.path.normpath(os.path.join(os.getcwd(), "../../../vattacker_data/" + sys.argv[sys.argv.index("-batch") + 1]))
        batch_test = BatchTest(filepath, is_nonrandom_mutation, int(max_attack_num))
