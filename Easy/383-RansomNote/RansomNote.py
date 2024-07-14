class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_magazine = {}

        for char in magazine:
            if char not in map_magazine:
                map_magazine[char] = 1
            else:
                map_magazine[char] += 1

        for char in ransomNote:
            if map_magazine.get(char, 0) > 0:
                map_magazine[char] -= 1
            else:
                return False

        return True