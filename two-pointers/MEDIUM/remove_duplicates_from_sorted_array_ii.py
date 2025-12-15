# Remove Duplicates from Sorted Array II
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Solution:

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates appearing more than twice.
        """
        if len(nums) <= 2:
            return len(nums)
        
        # Initialize the counter for the position to write
        # We can keep the first two elements as they are technically allowed (at most 2)
        write_pos = 2
        
        for read_pos in range(2, len(nums)):
            # If the current element is different from the element 2 positions back
            # it means we haven't used this number twice yet in the current sequence
            if nums[read_pos] != nums[write_pos - 2]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
                
        return write_pos

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,1,1,2,2,3]
    k1 = solution.removeDuplicates(nums1)
    print(f"Output: {k1}, nums: {nums1[:k1]}")
    
    nums2 = [0,0,1,1,1,1,2,3,3]
    k2 = solution.removeDuplicates(nums2)
    print(f"Output: {k2}, nums: {nums2[:k2]}")
