class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int10 = int(a, 2)
        b_int10 = int(b, 2)

        result_int10 = a_int10 + b_int10
        result_int2 = bin(result_int10)[2:]
        result = str(result_int2)

        return result
    

    def addBinary2(self, a: str, b: str) -> str:
        length_a = len(a) - 1
        length_b = len(b) - 1
        
        carry = 0
        result = ""

        while length_a >= 0 or length_b >= 0:
            sum = carry
            if length_a >= 0:
                value_a = int(a[length_a])
                length_a -= 1
            else:
                value_a = 0

            if length_b >= 0:
                value_b = int(b[length_b])
                length_b -= 1
            else:
                value_b = 0

            
            add = value_a + value_b + carry
            mod = add % 2
            result = str(mod) + result
            carry = add // 2

        if carry:
            result = "1" + result
        
        return result