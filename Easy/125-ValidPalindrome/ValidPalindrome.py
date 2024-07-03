class Solution:
    def isPalindrome(self, s: str) -> bool:

        def remove_non_alphanumeric(s: str) -> str:
            return ''.join(filter(str.isalnum, s))

        clean_string = remove_non_alphanumeric(s).lower()

        i = 0
        j = len(clean_string) - 1

        while i < j:
            if clean_string[i] == clean_string[j]:
                i += 1
                j -= 1
                continue
            
            return False

        return True