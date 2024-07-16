class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        string_digits = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
        i = len(num1) - 1
        j = len(num2) - 1
        int1 = 0
        int2 = 0
        result = ""

        multiply = 1
        while i >= 0:
            digit = digits[num1[i]]
            int1 += digit * multiply
            multiply = multiply * 10
            i -= 1

        multiply = 1
        while j >= 0:
            digit = digits[num2[j]]
            int2 += digit * multiply
            multiply = multiply * 10
            j -= 1

        total = int1 + int2
        if not total:
            return "0"

        while total > 0:
            digit = total % 10
            result += string_digits[digit]
            total = total // 10

        return result[::-1]


    def addStringsFunctionized(self, num1: str, num2: str) -> str:
        def buildInteger(num: str) -> int:
            digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
            i = len(num) - 1
            int_num = 0

            multiply = 1
            while i >= 0:
                digit = digits[num[i]]
                int_num += digit * multiply
                multiply = multiply * 10
                i -= 1
            
            return int_num

        def buildString(total: int) -> str:
            string_digits = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
            result = ""

            while total > 0:
                digit = total % 10
                result += string_digits[digit]
                total = total // 10
            
            return result[::-1]

        total = buildInteger(num=num1) + buildInteger(num=num2)

        if not total:
            return "0"

        return buildString(total=total)
    

    def addStringsASCII(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0:
            if i >= 0:
                digit_i = ord(num1[i]) - ord("0")
            else:
                digit_i = 0

            if j >= 0:
                digit_j = ord(num2[j]) - ord("0")
            else:
                digit_j = 0

            sum = digit_i + digit_j + carry
            # But this solution still uses built in str method.
            result.append(str(sum % 10))
            carry = sum // 10

            i -= 1
            j -= 1

        if carry:
            # And here too.
            result.append(str(carry))

        return "".join(reversed(result))