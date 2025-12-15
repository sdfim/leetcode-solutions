# Ugly Number III
# Problem: https://leetcode.com/problems/ugly-number-iii/

import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
            
        def lcm(x, y):
            return (x * y) // gcd(x, y)
            
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(a, bc)
        
        def count(num):
            return (num // a) + (num // b) + (num // c) \
                   - (num // ab) - (num // ac) - (num // bc) \
                   + (num // abc)
                   
        left, right = 1, 2 * 10**9
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= n:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.nthUglyNumber(3, 2, 3, 5)) # Output: 4
