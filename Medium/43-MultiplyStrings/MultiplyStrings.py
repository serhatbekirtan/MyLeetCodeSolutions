class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digitMap = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        result = 0
        # O(M * N)
        for index, i in enumerate(reversed(num1)):
            digit1 = digitMap[i]
            power = index
            for j in reversed(num2):
                digit2 = digitMap[j]
                result += (digit1 * digit2) * (10 ** power)
                power += 1

        return str(result)
    

    # Faster way. O(M + N)
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        first = 0
        
        for num in num1:
            digit = ord(num) - ord("0")
            print(digit)
            first *= 10
            first += digit

        for index, num in enumerate(reversed(num2)):
            second = ord(num) - ord("0")
            power = index
            result += (first * (second * (10 ** power)))

        return str(result)
    
    # 32-Bit solution.
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                result[i + j] += digit
                result[i + j + 1] += result[i + j] // 10
                result[i + j] = result[i + j] % 10

        result = result[::-1]
        beginning = 0

        while beginning < len(result) and result[beginning] == 0:
            beginning += 1

        result = map(str, result[beginning:])
        return "".join(result)