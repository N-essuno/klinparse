from typing import List, Dict, Tuple


class CKYParser:
    def __init__(self, grammar: List[Tuple[str, List[str]]]):
        self._grammar = grammar

    def parse(self, words: List[str]) -> List[List[List[str]]]:
        """
        Parse the given words using the given grammar.
        :param words: The words to parse.
        :return: A matrix representing the possible parses of the given words.
        """
        n = len(words)
        # Initialize the matrix.
        table = [[[] for _ in range(n)] for _ in range(n)]
        # Fill the matrix.
        for j in range(0, n):
            # Fill the diagonal first. Contains the constituents for the various words.
            # We don't need to check if the derivation is only one word (terminal),
            #   because we know that the grammar is in CNF.
            table[j][j] = [tag for tag, derivation in self._grammar if derivation[0] == words[j]]

            # Fill the rest of the matrix. For each column j, we iterate over the rows i in reverse order.
            for i in range(j - 1, -1, -1):
                # Iterate over the possible splits.
                for k in range(i, j):
                    # Iterate over the possible derivations.
                    for tag, derivation in self._grammar:
                        # If the rule brings to a terminal (len(derivation) == 1), skip it.
                        if len(derivation) == 2:
                            left = derivation[0]
                            right = derivation[1]
                            # Check if the derivation rule has as left child the tag in matrix[i][k] and as right child
                            #   the tag in matrix[k][j]. If so, add the tag to matrix[i][j].
                            if left in table[i][k] and right in table[k+1][j]:
                                if tag == "VP":
                                    print(left, " - ", right)
                                table[i][j].append(tag)
        return table


def print_cky_matrix_pretty(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


if __name__ == "__main__":
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
        ("PN", ["Houston"])
    ]


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
    # parser = CKYParser(grammar)
    # # print matrix in a pretty way
    # matrix = parser.parse(["a", "dog", "chased", "a", "cat"])
    # print_cky_matrix_pretty(matrix)


    parser = CKYParser(l1_grammar)

    matrix = parser.parse(phrase_1)
    print_cky_matrix_pretty(matrix)

    # print("\n\n\n")
    #
    # matrix = parser.parse(phrase_2)
    # print_cky_matrix_pretty(matrix)


