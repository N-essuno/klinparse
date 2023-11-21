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
            for i in range(j - 2, -1, -1):
                # Iterate over the possible splits.
                for k in range(i+1, j+1):
                    # Iterate over the possible derivations.
                    for tag, derivation in self._grammar:
                        # If the rule brings to a terminal (len(derivation) == 1), skip it.
                        if len(derivation) == 2:
                            left = derivation[0]
                            right = derivation[1]
                            # Check if the derivation rule has as left child the tag in matrix[i][k] and as right child
                            #   the tag in matrix[k][j]. If so, add the tag to matrix[i][j].
                            if left in table[i][k] and right in table[k][j]:
                                table[i][j].append(tag)
        return table


def print_cky_matrix_pretty():
    # each element on the left of the diagonal must be ignored in the print. They are
    # always empty lists
    pass


if __name__ == "__main__":
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
    for row in matrix:
        print(row)

