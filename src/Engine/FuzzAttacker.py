import os
import math
import codecs
from inspect import getsourcefile
from Utils.SentiText import *
from Utils.setting import *
from Engine.TextMutator import *

class FuzzAttacker(object):
    """
    The core engine of vattacker
    """

    def __init__(self, text):
        self.text = text


