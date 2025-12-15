# Single Element in a Sorted Array
# Problem: https://leetcode.com/problems/single-element-in-a-sorted-array/

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
                
        return nums[left]

if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))  # Output: 2
