# Apply Operations to an Array
# Problem: https://leetcode.com/problems/apply-operations-to-an-array/
# Solution:

from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1. Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                
        # 2. Move zeroes
        insert_pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1
                
        return nums

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,2,1,1,0]
    print(f"Applied operations on {nums1}: {solution.applyOperations(nums1)}")
    
    nums2 = [0,1]
    print(f"Applied operations on {nums2}: {solution.applyOperations(nums2)}")
