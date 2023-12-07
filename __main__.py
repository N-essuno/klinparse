from CKYParser import CKYParser
from resources import L1_GRAMMAR, L1_PHRASES, TOY_GRAMMAR, TOY_PHRASES, KLINGON_GRAMMAR, KLINGON_PHRASES


def print_cky_matrix_pretty(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("\n ---------------------------------------- \n")

def test_dummy():
    parser = CKYParser(TOY_GRAMMAR)
    # print matrix in a pretty way
    matrix = parser.parse(TOY_PHRASES[0])
    print_cky_matrix_pretty(matrix)

def test_jurafsky():
    parser = CKYParser(L1_GRAMMAR)

    matrix = parser.parse(L1_PHRASES[0])
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(L1_PHRASES[1])
    print_cky_matrix_pretty(matrix)


def test_klingon():
    parser = CKYParser(KLINGON_GRAMMAR)

    matrix = parser.parse(KLINGON_PHRASES[0])
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(KLINGON_PHRASES[1])
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(KLINGON_PHRASES[2])
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(KLINGON_PHRASES[3])
    print_cky_matrix_pretty(matrix)


if __name__ == "__main__":
    # test_dummy()
    # test_jurafsky()
    test_klingon()
