class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        resArr = []

        for i, c in enumerate(reversed(s)):
            if i and i % k == 0:
                resArr.append("-")
            resArr.append(c)

        return "".join(resArr)[::-1]