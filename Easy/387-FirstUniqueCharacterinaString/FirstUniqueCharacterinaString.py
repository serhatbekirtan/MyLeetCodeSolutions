class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for i, char in enumerate(s):
            if hashmap.get(char) == 1:
                return i

        return -1