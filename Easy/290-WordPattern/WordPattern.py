class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        words = s.split()
        result = ""

        if len(pattern) != len(words):
            return False

        for i, char in enumerate(pattern):
            if words[i] not in map.values():
                map[char] = words[i]

        for char in pattern:
            if char not in map:
                return False
            result += map[char]

        clean_s = s.replace(" ", "")

        return result == clean_s
    

    def wordPatternNeetCode(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        charToWord = {}
        wordToChar = {}

        for char, word in zip(pattern, words):
            if char in charToWord and charToWord[char] != word:
                return False
            if word in wordToChar and wordToChar[word] != char:
                return False
            
            charToWord[char] = word
            wordToChar[word] = char

        return True