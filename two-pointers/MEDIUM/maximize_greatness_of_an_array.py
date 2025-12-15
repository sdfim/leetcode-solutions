# Maximize Greatness of an Array
# Problem: https://leetcode.com/problems/maximize-greatness-of-an-array/
# Solution:

from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        for r in range(len(nums)):
            if nums[r] > nums[l]:
                l += 1
        return l

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,3,5,2,1,3,1]
    print(f"Max greatness of {nums1}: {solution.maximizeGreatness(nums1)}")
    
    nums2 = [1,2,3,4]
    print(f"Max greatness of {nums2}: {solution.maximizeGreatness(nums2)}")
