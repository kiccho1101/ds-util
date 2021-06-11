from dataclasses import dataclass
from typing import List, Optional

import MeCab


@dataclass
class Word:
    word: str
    hinshi: str


class MecabUtil:
    def __init__(self, dict_path: Optional[str] = None):
        if dict_path is not None:
            self.tagger = MeCab.Tagger(dict_path)
        else:
            self.tagger = MeCab.Tagger()

    def tokenize(self, s: str) -> List[Word]:
        node = self.tagger.parseToNode(s)
        words: List[Word] = []
        while node:
            word = node.surface
            hinshi = node.feature.split(",")[0]
            if hinshi != "BOS/EOS":
                words.append(Word(word, hinshi))
            node = node.next
        return words
