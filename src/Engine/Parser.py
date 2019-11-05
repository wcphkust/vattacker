import nltk
from nltk.parse import CoreNLPParser
from itertools import permutations
import random
import math
import copy


class Parser(object):
    """
    Parse the text to obtain syntax tree and other intermediate representations
    Support conjunction based mutation
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
            # print("subtree")
            # print(subtree)
            subsubtrees = list(subtree.subtrees())
            # print("subsubtree")
            # print(subsubtrees)
            subsubtrees_after_group = {}
            for i in range(len(subsubtrees) - 1):
                if not subsubtrees[i + 1]._label in subsubtrees_after_group.keys():
                    subsubtrees_after_group[subsubtrees[i + 1]._label] = {}
                subsubtrees_after_group[subsubtrees[i + 1]._label][i + 1] = subsubtrees[i + 1]
            for label in subsubtrees_after_group.keys():
                index_list = list(subsubtrees_after_group[label].keys())
                if len(index_list) < 2:
                    continue
                permutation_list = list(permutations(index_list))
                n = len(permutation_list) - 1
                # print(len(permutation_list))
                selected_index = math.ceil(random.uniform(1, n))
                # print(selected_index)
                selected_permutation = list(permutation_list[selected_index])
                # selected_permutation = permutation_list[1]
                tmp_subsubtrees = copy.deepcopy(subsubtrees)
                # print("index_list")
                # print(index_list)
                # print("selected permutation")
                # print(selected_permutation)
                # print("length of subtrees without root")
                # print(len(subsubtrees) - 1)
                for j in range(len(index_list)):
                    subtree.__setitem__(index_list[j] - 1, tmp_subsubtrees[selected_permutation[j]])
        return " ".join(self.syntax_tree.leaves())
