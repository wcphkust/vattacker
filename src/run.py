import sys
from Eval.demotest import *
from Eval.SingleTest import *
from Eval.BatchTest import *

if __name__ == '__main__':
    if ("-single" in sys.argv):
        single_test = SingleTest(sys.argv[sys.argv.index("-single") + 1])
    elif ("-demo" in sys.argv):
        demotest()
    elif ("-batch" in sys.argv):
        filepath = os.path.normpath(os.path.join(os.getcwd(), "../../../vattacker_data/" + sys.argv[sys.argv.index("-batch") + 1]))
        batch_test = BatchTest(filepath)