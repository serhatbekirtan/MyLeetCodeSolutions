class Solution:
    def getLucky(self, s: str, k: int) -> int:
        arr = []

        for c in s:
            arr.append(str(ord(c) - ord("a") + 1))
        
        num = int("".join(arr))

        for _ in range(k):
            newNum = 0
            while num:
                digit = num % 10
                num //= 10
                newNum += digit
            num = newNum

        return num