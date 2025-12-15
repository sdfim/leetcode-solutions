# Move Zeroes
# Problem: https://leetcode.com/problems/move-zeroes/
# Solution:

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        insert_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    nums1 = [0,1,0,3,12]
    solution.moveZeroes(nums1)
    print(f"Moved zeroes: {nums1}")
    
    nums2 = [0]
    solution.moveZeroes(nums2)
    print(f"Moved zeroes: {nums2}")
