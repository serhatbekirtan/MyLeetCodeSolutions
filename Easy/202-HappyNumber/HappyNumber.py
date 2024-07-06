class Solution:
    def isHappy(self, n: int) -> bool:
        arr = []
        arr.append(n)
        number = 0

        while arr.count(number) < 2:
            number = self.divide_digitsNsquareAdd(arr[len(arr) - 1])

            if number == 1:
                return True
            
            arr.append(number)

        return False
    

    def divide_digitsNsquareAdd(self, n: int) -> int:
            digit_array = []
            result = 0

            while n > 0:
                digit = n % 10
                digit_array.append(digit)
                n = n // 10
                
            for digit in digit_array:
                result += pow(digit, 2)

            return result