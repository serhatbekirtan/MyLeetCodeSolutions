class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and ((n & (n - 1)) == 0)
    
    """ Alternate solutions:
        
        # Solution 1: 2^30 mod power of 2.
        return (n > 0) and (((1 << 30) % n) == 0)

        # Solution 2: Count number of 1 bits. Should be equal to 1.
        return (n > 0) and (n.bit_count() == 1)

        # Solution 3: Search for the number by taking powers of 2.
        def isPowerOfTwo(self, n: int) -> bool:
            for i in range(31):
                ans = 2 ** i
                if ans == n:
                    return True
            return False

    """