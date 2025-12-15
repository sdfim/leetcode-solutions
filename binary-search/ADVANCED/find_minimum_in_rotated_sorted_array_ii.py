# Find Minimum in Rotated Sorted Array II
# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # When nums[mid] == nums[right], we can't discard the right half
                # because the minimum could be there. But we can safely discard right.
                right -= 1
        return nums[left]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin([1,3,5]))  # Output: 1
    print(solution.findMin([2,2,2,0,1]))  # Output: 0
