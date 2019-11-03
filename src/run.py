import sys
from Eval.demotest import *
from Eval.SingleTest import *

if __name__ == '__main__':
    if ("-single" in sys.argv):
        singletest = SingleTest(sys.argv[sys.argv.index("-single") + 1])
        singletest.test()
    elif ("-demo" in sys.argv):
        demotest()