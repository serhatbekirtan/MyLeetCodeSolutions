from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.count += 1

    def get_score(self, word):
        res = 0
        curr = self
        for c in word:
            curr = curr.children[c]
            res += curr.count
        return res


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefixes = defaultdict(int)

        for word in words:
            for i in range(len(word)):
                prefixes[word[:i + 1]] += 1

        for word in words:
            score = 0
            for i in range(len(word)):
                score += prefixes[word[:i + 1]]
            res.append(score)

        return res
    

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        res = []

        for word in words:
            root.insert(word)

        for word in words:
            res.append(root.get_score(word))

        return res