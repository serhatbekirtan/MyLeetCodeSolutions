from collections import Counter, defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        substrings = defaultdict(int)

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                freq = Counter(substr)
                if len(freq) == 1:
                    substrings[substr] += 1

        res = -1

        for key in substrings:
            if substrings[key] > 2:
                res = max(res, len(key))

        return res