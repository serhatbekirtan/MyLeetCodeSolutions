from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0

        for word in words:
            isConsistent = True

            for c in word:
                if c not in allowed:
                    isConsistent = False
                    break

            res += 1 if isConsistent else 0

        return res