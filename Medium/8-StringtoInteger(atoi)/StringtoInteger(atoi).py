class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        s = s.lstrip()
        sign = 1

        if s.startswith("-"):
            sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        s = s.lstrip("0")

        value = 0
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            value = (value * 10) + int(s[i])

        value = sign * value

        if value < -2 ** 31:
            return -2 ** 31
        elif value > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return value
        

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1

        if s.startswith("-"):
            sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        n = len(s)
        current = 0
        for i in range(n):
            if not s[i].isdigit():
                break
            current = 10 * current + int(s[i])
        
        current = current * sign

        current = min(current, 2 ** 31 - 1)
        current = max(current, -2 **31)
        return current