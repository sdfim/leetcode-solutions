# Next Permutation
# Problem: https://leetcode.com/problems/next-permutation/
# Solution:

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        
        # 1. Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
            
        if i >= 0:
            # 2. Find the element just larger than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        # 3. Reverse the rest
        self.reverse(nums, i + 1)
        
    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,3]
    solution.nextPermutation(nums1)
    print(f"Next permutation of [1,2,3]: {nums1}")
    
    nums2 = [3,2,1]
    solution.nextPermutation(nums2)
    print(f"Next permutation of [3,2,1]: {nums2}")
    
    nums3 = [1,1,5]
    solution.nextPermutation(nums3)
    print(f"Next permutation of [1,1,5]: {nums3}")
