# Smallest Subarrays With Maximum Bitwise OR
# Problem: https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        # Track next occurrence of each bit
        next_bit = [-1] * 32
        
        for i in range(n - 1, -1, -1):
            val = nums[i]
            max_idx = i
            
            # Update bit positions
            for b in range(32):
                if (val >> b) & 1:
                    next_bit[b] = i
                    
            # Check all bits to find furthest needed index
            for b in range(32):
                if next_bit[b] != -1:
                    max_idx = max(max_idx, next_bit[b])
                    
            ans[i] = max_idx - i + 1
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestSubarrays([1,0,2,1,3])) # [3,3,2,2,1]
