# Missing Element in Sorted Array
# Problem: https://leetcode.com/problems/missing-element-in-sorted-array/

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Missing count up to index i:
        # (nums[i] - nums[0] + 1) - (i + 1) = nums[i] - nums[0] - i
        
        def missing(idx):
            return nums[idx] - nums[0] - idx
            
        n = len(nums)
        # If k is larger than total missing in array
        if k > missing(n - 1):
            return nums[n - 1] + k - missing(n - 1)
            
        left, right = 0, n - 1
        
        # Binary search for rightmost index such that missing(index) < k
        while left < right:
            mid = (left + right + 1) // 2
            if missing(mid) < k:
                left = mid
            else:
                right = mid - 1
                
        # nums[left] is the largest number smaller than our target
        # k - missing(left) is how many more we need
        return nums[left] + k - missing(left)

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingElement([4,7,9,10], 1)) # 5
    print(solution.missingElement([4,7,9,10], 3)) # 8
