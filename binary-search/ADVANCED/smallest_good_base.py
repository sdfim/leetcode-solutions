# Smallest Good Base
# Problem: https://leetcode.com/problems/smallest-good-base/

import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # We want n = 1 + k + k^2 + ... + k^(m-1)
        # n = (k^m - 1) / (k - 1)
        # k can range from 2 to n-1.
        # m can range from 2 to log2(n) + 1.
        # Since we want smallest k, we should iterate m from max possible down to 2.
        
        max_m = int(math.log2(num)) + 1
        
        for m in range(max_m, 1, -1):
            # We want to find integer k such that sum(k^i for i in 0..m-1) == num
            # Geometric series sum is roughly k^(m-1).
            # So k is roughly num^(1/(m-1)).
            k = int(num ** (1 / (m - 1)))
            
            if k <= 1: 
                continue
            
            # Check if this k works
            # We can use direct formula or manual summation to avoid overflow issues if careful, 
            # though python handles large ints.
            
            current = 1
            val = 1
            for _ in range(m - 1):
                current *= k
                val += current
                if val > num:
                    break
            
            if val == num:
                return str(k)
                
        return str(num - 1)

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestGoodBase("13")) # Output: "3" (1 + 3 + 9 = 13)
