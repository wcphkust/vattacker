import sys
from Eval.SingleTest import *
from Eval.BatchTest import *

if __name__ == '__main__':
    is_nonrandom_mutation = True
    if ("-random" in sys.argv):
        is_nonrandom_mutation = False
    if ("-single" in sys.argv):
        single_test = SingleTest(sys.argv[sys.argv.index("-single") + 1], is_nonrandom_mutation)
    elif ("-batch" in sys.argv):
        filepath = os.path.normpath(os.path.join(os.getcwd(), "../../../vattacker_data/" + sys.argv[sys.argv.index("-batch") + 1]))
        batch_test = BatchTest(filepath, is_nonrandom_mutation)