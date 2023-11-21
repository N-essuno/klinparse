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
        raise NotImplementedError

