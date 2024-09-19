from typing import List


class Solution:
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y
    }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []

        for i in range(len(expression)):
            op = expression[i]

            if op in self.operations:
                arr1 = self.diffWaysToCompute(expression[:i])
                arr2 = self.diffWaysToCompute(expression[i + 1:])

                for num1 in arr1:
                    for num2 in arr2:
                        res.append(self.operations[op](num1, num2))
        
        if not res:
            res.append(int(expression))

        return res