# Search in Rotated Sorted Array
# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Check which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4,5,6,7,0,1,2], 0))  # Output: 4
    print(solution.search([4,5,6,7,0,1,2], 3))  # Output: -1
