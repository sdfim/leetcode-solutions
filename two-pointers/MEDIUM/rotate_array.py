# Rotate Array
# Problem: https://leetcode.com/problems/rotate-array/
# Solution:

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
            
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        # 1. Reverse entire array
        reverse(0, len(nums) - 1)
        # 2. Reverse first k elements
        reverse(0, k - 1)
        # 3. Reverse the rest
        reverse(k, len(nums) - 1)

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    solution.rotate(nums1, k1)
    print(f"Rotated [1..7] by 3: {nums1}")
    
    nums2 = [-1,-100,3,99]
    k2 = 2
    solution.rotate(nums2, k2)
    print(f"Rotated [-1,-100,3,99] by 2: {nums2}")
