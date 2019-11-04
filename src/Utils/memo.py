from nltk.parse import CoreNLPParser

# Lexical Parser
# parser = CoreNLPParser(url='http://localhost:9000')
parser = CoreNLPParser(url='http://localhost:8999')

# Parse tokenized text.
list(parser.parse('What is the airspeed of an unladen swallow ?'.split()))

# Parse raw string.
list(parser.raw_parse('What is the airspeed of an unladen swallow ?'))

# Neural Dependency Parser
from nltk.parse.corenlp import CoreNLPDependencyParser
dep_parser = CoreNLPDependencyParser(url='http://localhost:8999')
parses = dep_parser.parse('What is the airspeed of an unladen swallow ?'.split())
[[(governor, dep, dependent) for governor, dep, dependent in parse.triples()] for parse in parses]

# Tokenizer
parser = CoreNLPParser(url='http://localhost:8999')
ls_token = list(parser.tokenize('What is the airspeed of an unladen swallow?'))
print(ls_token)

# POS Tagger
pos_tagger = CoreNLPParser(url='http://localhost:8999', tagtype='pos')
ls_pos = list(pos_tagger.tag('What is the airspeed of an unladen swallow ?'.split()))
print(ls_pos)

# NER Tagger
ner_tagger = CoreNLPParser(url='http://localhost:8999', tagtype='ner')
ls_ner = list(ner_tagger.tag(('Rami Eid is studying at Stony Brook University in NY'.
split())))
print(ls_ner)
