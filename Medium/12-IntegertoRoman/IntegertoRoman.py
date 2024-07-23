class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: "I", 4: "VI", 5: "V", 9: "XI", 10: "X", 40: "LX", 50: "L", 90: "CX", 100: "C", 400: "DC",
                 500: "D", 900: "MC", 1000: "M"}
        result = []
        powerOfTen = 0

        while num:
            digit = num % 10
            tens = pow(10, powerOfTen)
            number = tens * digit

            if number in roman:
                result.append(roman[number])
            else:
                if digit < 4 and powerOfTen < 3:
                    for i in range(digit):
                        result.append(roman[tens])
                elif digit < 9 and powerOfTen < 3:
                    for i in range(digit - 5):
                        result.append(roman[tens])
                    result.append(roman[5 * tens])
                else:
                    for i in range(digit):
                        result.append(roman[tens])

            num = num // 10
            powerOfTen += 1

        result = "".join(result)
        return result[::-1]
    

    def intToRomanCleaner(self, num: int) -> str:
        roman = [[1, "I"], [4, "IV"], [5, "V"], [9, "IX"], [10, "X"], [40, "XL"], [50, "L"], [90, "XC"], [100, "C"], 
                 [400, "CD"], [500, "D"], [900, "CM"], [1000, "M"]]
        result = []

        for value, symbol in reversed(roman):
            if num // value:
                count = num // value
                result.append(count * symbol)
                num = num % value
        
        return "".join(result)