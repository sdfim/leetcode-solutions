# Find Peak Element
# Problem: https://leetcode.com/problems/find-peak-element/

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # Peak is in the left part (including mid)
                right = mid
            else:
                # Peak is in the right part
                left = mid + 1
                
        return left

if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([1,2,3,1]))  # Output: 2
    print(solution.findPeakElement([1,2,1,3,5,6,4]))  # Output: 1 or 5
