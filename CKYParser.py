from typing import List, Tuple


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
                                table[i][j].append(tag)
        return table
