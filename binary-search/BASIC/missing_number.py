# Missing Number
# Problem: https://leetcode.com/problems/missing-number/

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Standard approach: (n)(n+1)/2 - sum(nums)
        # Binary Search approach (requires sorting):
        nums.sort()
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                # Missing number is to the right
                left = mid + 1
            else:
                # nums[mid] > mid, so missing number is to left or is missing index
                right = mid - 1
                
        return left

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingNumber([3,0,1]))  # Output: 2
    print(solution.missingNumber([0,1]))    # Output: 2
