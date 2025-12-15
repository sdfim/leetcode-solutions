# Remove Element
# Problem: https://leetcode.com/problems/remove-element/
# Solution:

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
        The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [3,2,2,3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"Output: {k1}, nums: {nums1[:k1]}")
    
    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"Output: {k2}, nums: {nums2[:k2]}")
