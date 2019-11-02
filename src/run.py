import sys
from Eval.demotest import *
from Eval.singletest import *

if __name__ == '__main__':
    if ("-single" in sys.argv):
        singletest(sys.argv[sys.argv.index("-single") + 1])
    elif ("-demo" in sys.argv):
        demotest()