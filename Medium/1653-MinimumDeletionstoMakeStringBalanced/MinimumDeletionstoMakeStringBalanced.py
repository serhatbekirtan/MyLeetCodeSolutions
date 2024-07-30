class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a = count_b = 0
        hashmap = {}
        result = len(s)

        i = 0
        while i < len(s):
            hashmap[i] = [count_b, count_a]
            if s[i] == "b":
                count_b += 1
            i += 1
        
        j = len(s) - 1
        while j >= 0:
            hashmap[j][1] = count_a
            if s[j] == "a":
                count_a += 1
            j -= 1

        for key in hashmap:
            b, a = hashmap[key]
            result = min(result, a + b)

        return result
    

    # One Pass solution.
    def minimumDeletions(self, s: str) -> int:
        stack = []
        result = 0

        for char in s:
            if stack and char == "a" and stack[-1] == "b":
                stack.pop()
                result += 1
            else:
                stack.append(char)
            
        return result
    

    # O(1) Space.
    def minimumDeletions(self, s: str) -> int:
        count_a = count_b = 0
        result = len(s)

        for char in s:
            count_a += 1 if char == "a" else 0

        for i, char in enumerate(s):
            if char == "a":
                count_a -= 1

            result = min(result, count_a + count_b)

            if char == "b":
                count_b += 1
        
        return result