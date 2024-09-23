from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False


class Trie:
    def __init__(self, words) -> None:
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True


class Solution:
    # DP Solution.
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1) # skip current char
            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)
    

    # Trie Solution.
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s): 0}
        trie = Trie(dictionary).root

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i + 1)
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.word:
                    res = min(res, dfs(j + 1))
            
            dp[i] = res
            return res

        return dfs(0)