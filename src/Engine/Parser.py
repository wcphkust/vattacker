import nltk
from nltk.parse import CoreNLPParser
from itertools import permutations
import random
import math
import copy

class Parser(object):
    """
    Parse the text to obtain syntax tree and other intermediate representations
    """

    def __init__(self, text):
        self.text = text
        self.tokens = nltk.word_tokenize(text)
        self.syntax_tree = None

    def syntax_tree_parser(self):
        """
        get syntax tree
        :return: syntax tree
        """
        if self.syntax_tree is not None:
            return self.syntax_tree
        parser = CoreNLPParser(url='http://localhost:8999')
        self.syntax_tree = list(parser.parse(nltk.word_tokenize(self.text)))[0]
        return self.syntax_tree

    def mutate_conjunction(self, height = 3):
        if self.syntax_tree is None:
            self.syntax_tree_parser()
        subtrees = self.syntax_tree.subtrees(lambda t: t.height() == height)
        for subtree in subtrees:
            if len(list(subtree.subtrees())) < 3:
                continue
            subsubtrees = list(subtree.subtrees())
            subsubtrees_after_group = {}
            for i in range(len(subsubtrees)):
                if not subsubtrees[i]._label in subsubtrees_after_group.keys():
                    subsubtrees_after_group[subsubtrees[i]._label] = {}
                subsubtrees_after_group[subsubtrees[i]._label][i] = subsubtrees[i]
            for label in subsubtrees_after_group.keys():
                index_list = list(subsubtrees_after_group[label].keys())
                permutation_list = []
                if len(index_list) > 1:
                    permutation_list = permutations(index_list)
                n = len(permutation_list) - 1
                selected_index = math.ceil(random.uniform(1, n))
                selected_permutation = permutations[selected_index]
                tmp_subsubtrees = copy.deepcopy(subsubtrees)
                for j in index_list:
                    subtree.__setitem__(j, tmp_subsubtrees[selected_index[j]])
        return " ".join(self.syntax_tree.leaves)





