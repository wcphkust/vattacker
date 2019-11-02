import requests
import json
from Utils.IO import *
from Utils.setting import *
from Utils.SentiText import *
from Engine.SentimentIntensityAnalyzer import *

def singletest(sentence):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
    print("\n\n Single Test Done!")