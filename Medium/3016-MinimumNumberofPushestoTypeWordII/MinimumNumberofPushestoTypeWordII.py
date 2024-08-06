from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap = Counter(word)
        result = 0
        arr = [(hashmap[char]) for char in hashmap]
        arr.sort(reverse=True)

        for i, count in enumerate(arr):
            times = (i // 8) + 1
            result +=  times * count

        return result


    def minimumPushes(self, word: str) -> int:
        letter_counts = [0] * 26

        for char in word:
            letter_counts[ord(char) - ord('a')] += 1
        
        letter_counts.sort(reverse=True)
        res = 0
        
        for i, count in enumerate(letter_counts):
            if count == 0:
                break
            res += (i // 8 + 1) * count
        
        return res