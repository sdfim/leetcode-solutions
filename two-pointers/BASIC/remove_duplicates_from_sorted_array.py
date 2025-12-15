# Remove Duplicates from Sorted Array
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Solution:

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
        such that each unique element appears only once.
        Returns the number of unique elements.
        """
        if not nums:
            return 0
            
        write_pointer = 1
        
        for read_pointer in range(1, len(nums)):
            if nums[read_pointer] != nums[read_pointer - 1]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
                
        return write_pointer

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(f"Output: {k1}, nums: {nums1[:k1]}")
    
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = solution.removeDuplicates(nums2)
    print(f"Output: {k2}, nums: {nums2[:k2]}")
