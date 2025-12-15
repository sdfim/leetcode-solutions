# Maximum Number That Sum of the Prices Is Less Than or Equal to K
# Problem: https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

from typing import List

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        
        def count_bits(num, x):
            # Count sum of i-th bits (1-based) where i % x == 0 for numbers 1 to num.
            # Total sum.
            
            res = 0
            # Iterate bit positions i = x, 2x, 3x ...
            # up to approx 60 (since num can be large, k=10^15).
            
            curr = x
            while (1 << (curr - 1)) <= num:
                # Bit position `curr` (1-based).
                # 0-based index is `curr - 1`.
                bit_idx = curr - 1
                
                block_size = 1 << (bit_idx + 1)
                full_blocks = (num + 1) // block_size
                res += full_blocks * (1 << bit_idx)
                
                remainder = (num + 1) % block_size
                res += max(0, remainder - (1 << bit_idx))
                
                curr += x
                
            return res
            
        left, right = 1, 10**16 
        ans = 1
        
        while left <= right:
            mid = (left + right) // 2
            if count_bits(mid, x) <= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaximumNumber(9, 1)) # 6
