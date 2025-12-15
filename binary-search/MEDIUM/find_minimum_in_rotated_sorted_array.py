# Find Minimum in Rotated Sorted Array
# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # Minimum must be in the right part
                left = mid + 1
            else:
                # Minimum is at mid or in the left part
                right = mid
                
        return nums[left]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin([3,4,5,1,2]))  # Output: 1
    print(solution.findMin([4,5,6,7,0,1,2]))  # Output: 0
