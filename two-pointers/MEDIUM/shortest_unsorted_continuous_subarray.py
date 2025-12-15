# Shortest Unsorted Continuous Subarray
# Problem: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Solution:

from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        # Find first out of order from left
        l = 0
        while l < n - 1 and nums[l] <= nums[l+1]:
            l += 1
            
        if l == n - 1:
            return 0
            
        # Find first out of order from right
        r = n - 1
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
            
        # Find min and max in the subarray
        sub_min = min(nums[l:r+1])
        sub_max = max(nums[l:r+1])
        
        # Expand subarray
        while l > 0 and nums[l-1] > sub_min:
            l -= 1
        while r < n - 1 and nums[r+1] < sub_max:
            r += 1
            
        return r - l + 1

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [2,6,4,8,10,9,15]
    print(f"Shortest unsorted subarray {nums1}: {solution.findUnsortedSubarray(nums1)}")
