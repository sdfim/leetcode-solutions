# Minimum Array Length After Pair Removals
# Problem: https://leetcode.com/problems/minimum-array-length-after-pair-removals/
# Solution:

from typing import List
from collections import Counter

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        c = Counter(nums)
        max_freq = max(c.values())
        
        if max_freq <= n // 2:
            return n % 2
        else:
            return 2 * max_freq - n

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,3,4]
    print(f"Min length after removals {nums1}: {solution.minLengthAfterRemovals(nums1)}")
    
    nums2 = [1,1,2,3]
    print(f"Min length after removals {nums2}: {solution.minLengthAfterRemovals(nums2)}")
