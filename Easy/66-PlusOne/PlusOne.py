from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        str_form = ""
        
        for digit in digits:
            str_form += str(digit)

        inte = int(str_form)
        inte += 1

        str_plus = str(inte)
        plus_one = []

        for c in str_plus:
            plus_one.append(int(c))
        return plus_one
    

    def plusOne2(self, digits: List[int]) -> List[int]:
        last_index = len(digits) - 1

        while last_index >= 0:
            if digits[last_index] != 9:
                digits[last_index] += 1
                return digits
            else:
                if last_index == 0:
                    digits[last_index] = 0
                    digits.insert(0, 1)
                    return digits
                else:
                    digits[last_index] = 0
                    last_index -= 1
        
        return digits