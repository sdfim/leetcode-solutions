# Maximum Width Ramp
# Problem: https://leetcode.com/problems/maximum-width-ramp/
# Solution:

from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = [] # Decreasing stack of indices
        
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
                
        res = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [6,0,8,2,1,5]
    print(f"Max width ramp {nums1}: {solution.maxWidthRamp(nums1)}")
    
    nums2 = [9,8,1,0,1,9,4,0,4,1]
    print(f"Max width ramp {nums2}: {solution.maxWidthRamp(nums2)}")
