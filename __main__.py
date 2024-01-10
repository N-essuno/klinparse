import sys

from CKYParser import CKYParser
from resources import L1_GRAMMAR, L1_PHRASES, TOY_GRAMMAR, TOY_PHRASES, KLINGON_GRAMMAR, KLINGON_PHRASES, KLINGON_PHRASES_SEM
from nltk import load_parser


def print_cky_matrix_pretty(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("\n ---------------------------------------- \n")


def test_dummy(print_matrix: bool):
    parser = CKYParser(TOY_GRAMMAR)
    # print matrix in a pretty way
    matrix = parser.parse(TOY_PHRASES[0], print_matrix)
    print_cky_matrix_pretty(matrix)


def test_jurafsky(print_matrix: bool):
    parser = CKYParser(L1_GRAMMAR)

    matrix = parser.parse(L1_PHRASES[0], print_matrix)
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(L1_PHRASES[1], print_matrix)
    print_cky_matrix_pretty(matrix)


def test_klingon(print_matrix: bool):
    parser = CKYParser(KLINGON_GRAMMAR)

    matrix = parser.parse(KLINGON_PHRASES[0], print_matrix)
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(KLINGON_PHRASES[1], print_matrix)
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(KLINGON_PHRASES[2], print_matrix)
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(KLINGON_PHRASES[3], print_matrix)
    print_cky_matrix_pretty(matrix)

def test_simple_sem():
    sentence = "a dog chases a girl"
    parse_with_semantics('file:simple-sem.fcfg', sentence)

def test_klingon_sem():
    parse_with_semantics('file:klingon-sem.fcfg', KLINGON_PHRASES_SEM[0])
    parse_with_semantics('file:klingon-sem.fcfg', KLINGON_PHRASES_SEM[1])
    parse_with_semantics('file:klingon-sem.fcfg', KLINGON_PHRASES_SEM[2])
    parse_with_semantics('file:klingon-sem.fcfg', KLINGON_PHRASES_SEM[3])

def parse_with_semantics(grammar_url, sentence):
    parser = load_parser(grammar_url, trace=0)
    tokens = sentence.split()
    for tree in parser.parse(tokens):
        print(tree.label()['SEM'])
    print()

if __name__ == "__main__":
    # get arg for printing matrix
    try:
        print_matrix = bool(int((sys.argv[1])))
    except:
        print("Invalid or missing argument for printing matrix: (should be 1=True or 0=False) defaulting to False\n")
        print_matrix = False

    test_dummy(print_matrix)
    test_jurafsky(print_matrix)
    test_klingon(print_matrix)
    test_simple_sem()
    test_klingon_sem()