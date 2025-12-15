# Nth Magical Number
# Problem: https://leetcode.com/problems/nth-magical-number/

import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate LCM
        l = (a * b) // math.gcd(a, b)
        
        def count(x):
            return x // a + x // b - x // l
            
        left, right = min(a, b), min(a, b) * n
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= n:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res % MOD

if __name__ == "__main__":
    solution = Solution()
    print(solution.nthMagicalNumber(1, 2, 3)) # Output: 2
    print(solution.nthMagicalNumber(4, 2, 3)) # Output: 6
