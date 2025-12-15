# Sort Array By Parity
# Problem: https://leetcode.com/problems/sort-array-by-parity/
# Solution:

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l < r:
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 1:
                r -= 1
                
        return nums

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3,1,2,4]
    print(f"Sorted by parity {nums1}: {solution.sortArrayByParity(nums1)}")
