from typing import List, Dict


class CKYParser:
    def __init__(self, grammar: Dict[str, List[str]]):
        self._grammar = grammar

    def parse(self, words: List[str]) -> List[List[List[str]]]:
        """
        Parse the given words using the given grammar.
        :param words: The words to parse.
        :return: A matrix representing the possible parses of the given words.
        """
        n = len(words)
        # Initialize the matrix.
        matrix = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        # Fill the matrix.
        for j in range(1, n + 1):
            matrix[j - 1][j] = [tag for tag, words in self._grammar.items() if words[0] == words[j - 1]]
            for i in range(j - 2, -1, -1):
                for k in range(i + 1, j):
                    for tag, words in self._grammar.items():
                        if words[0] == words[j - 1]:
                            for left in matrix[i][k]:
                                for right in matrix[k][j]:
                                    matrix[i][j].append(tag)
        return matrix

