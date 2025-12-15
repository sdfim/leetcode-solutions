# Check If a Number Is Majority Element in a Sorted Array
# Problem: https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        # Find first occurrence of target
        import bisect
        first = bisect.bisect_left(nums, target)
        
        if first + n // 2 < n and nums[first + n // 2] == target:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.isMajorityElement([2,4,5,5,5,5,5,6,6], 5))  # Output: True
    print(solution.isMajorityElement([10,100,101,101], 101))    # Output: False
