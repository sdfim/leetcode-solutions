# Minimum Size Subarray Sum
# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/
# Solution:

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        total = 0
        
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
                
        return res if res != float('inf') else 0

if __name__ == "__main__":
    solution = Solution()
    
    target1 = 7
    nums1 = [2,3,1,2,4,3]
    print(f"Min subarray len for {nums1}, target {target1}: {solution.minSubArrayLen(target1, nums1)}")
