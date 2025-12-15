# Search in Rotated Sorted Array II
# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid] == nums[right]:
                # Unable to determine which side is sorted, shrink
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([2,5,6,0,0,1,2], 0))  # Output: True
    print(solution.search([2,5,6,0,0,1,2], 3))  # Output: False
