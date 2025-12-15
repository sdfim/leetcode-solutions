# Subarrays with K Different Integers
# Problem: https://leetcode.com/problems/subarrays-with-k-different-integers/
# Solution:

from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
    
    def atMostK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        l = 0
        res = 0
        
        for r in range(len(nums)):
            if count[nums[r]] == 0:
                k -= 1
            count[nums[r]] += 1
            
            while k < 0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1
            
            res += r - l + 1
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,1,2,3]
    k1 = 2
    print(f"Subarrays with {k1} different integers in {nums1}: {solution.subarraysWithKDistinct(nums1, k1)}")
