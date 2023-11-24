from CKYParser import CKYParser


def print_cky_matrix_pretty(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print("\n ---------------------------------------- \n")

def test_dummy():
    grammar = [
        ("S", ["NP", "VP"]),
        ("NP", ["Det", "N"]),
        ("VP", ["V", "NP"]),
        ("PP", ["P", "NP"]),
        ("NP", ["NP", "PP"]),
        ("Det", ["a"]),
        ("Det", ["the"]),
        ("N", ["dog"]),
        ("N", ["cat"]),
        ("N", ["rug"]),
        ("V", ["chased"]),
        ("P", ["in"]),
        ("P", ["on"]),
        ("P", ["by"])
    ]

    parser = CKYParser(grammar)
    # print matrix in a pretty way
    matrix = parser.parse(["a", "dog", "chased", "a", "cat"])
    print_cky_matrix_pretty(matrix)

def test_jurafsky():
    phrase_1 = ["book", "the", "flight", "through", "Houston"]
    phrase_2 = ["does", "she", "prefer", "a", "morning", "flight"]

    # L1 Jurafsky grammar in CNF

    l1_grammar = [
        # Rules for S
        ("S", ["NP", "VP"]),
        ("S", ["X1", "VP"]),
        ("S", ["V", "NP"]),
        ("S", ["X2", "PP"]),
        ("S", ["V", "PP"]),
        ("S", ["VP", "PP"]),
        ("S", ["book"]),
        ("S", ["prefer"]),

        # Rules for X1
        ("X1", ["Aux", "NP"]),

        # Rules for NP
        ("NP", ["Det", "Nominal"]),
        ("NP", ["she"]),
        ("NP", ["Houston"]),

        # Rules for VP
        ("VP", ["V", "NP"]),
        ("VP", ["X2", "PP"]),
        ("VP", ["V", "PP"]),
        ("VP", ["VP", "PP"]),
        ("VP", ["book"]),
        ("VP", ["prefer"]),

        # Rules for V
        ("V", ["book"]),
        ("V", ["prefer"]),

        # Rules for PP
        ("PP", ["P", "NP"]),

        # Rules for X2
        ("X2", ["V", "NP"]),

        # Rules for Det
        ("Det", ["the"]),
        ("Det", ["a"]),

        # Rules for Nominal
        ("Nominal", ["Nominal", "Noun"]),
        ("Nominal", ["Nominal", "PP"]),
        ("Nominal", ["book"]),
        ("Nominal", ["flight"]),
        ("Nominal", ["morning"]),

        # Rules for Noun
        ("Noun", ["flight"]),
        ("Noun", ["book"]),
        ("Noun", ["morning"]),

        # Rules for P
        ("P", ["through"]),

        # Rules for PN
        ("PN", ["Houston"]),

        # Rules for Aux
        ("Aux", ["does"])
    ]

    parser = CKYParser(l1_grammar)

    matrix = parser.parse(phrase_1)
    print_cky_matrix_pretty(matrix)

    matrix = parser.parse(phrase_2)
    print_cky_matrix_pretty(matrix)


def test_klingon():
        pass


if __name__ == "__main__":
    test_dummy()
    test_jurafsky()
    test_klingon()
