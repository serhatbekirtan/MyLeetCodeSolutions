class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        thousands = ["", " Thousand", " Million", " Billion"]

        tens = {9: "Ninety",
                8: "Eighty",
                7: "Seventy",
                6: "Sixty",
                5: "Fifty",
                4: "Forty",
                3: "Thirty",
                2: "Twenty"}

        ones = {19: "Nineteen",
                18: "Eighteen",
                17: "Seventeen",
                16: "Sixteen",
                15: "Fifteen",
                14: "Fourteen",
                13: "Thirteen",
                12: "Twelve",
                11: "Eleven",
                10: "Ten",
                9: "Nine",
                8: "Eight",
                7: "Seven",
                6: "Six",
                5: "Five",
                4: "Four",
                3: "Three",
                2: "Two",
                1: "One"}
        
        def get_hundred(n):
            res = []
            hundred = n // 100

            if hundred:
                res.append(ones[hundred] + " Hundred")
            
            ten = n % 100
            if ten >= 20:
                res.append(tens[ten // 10])
                if ten % 10:
                    res.append(ones[ten % 10])

            elif ten:
                res.append(ones[ten])

            return " ".join(res)

        thousand = 0
        res = []
        while num:
            number = num % 1000
            num //= 1000
            s = get_hundred(number)

            if s:
                res.append(s + thousands[thousand])

            thousand += 1
        
        return " ".join(res[::-1])