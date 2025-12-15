# Find the Array Concatenation Value
# Problem: https://leetcode.com/problems/find-the-array-concatenation-value/
# Solution:

from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        concat_val = 0
        
        while l <= r:
            if l == r:
                concat_val += nums[l]
            else:
                val_str = str(nums[l]) + str(nums[r])
                concat_val += int(val_str)
            l += 1
            r -= 1
            
        return concat_val

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [7,52,2,4]
    print(f"Concatenation value of {nums1}: {solution.findTheArrayConcVal(nums1)}")
    
    nums2 = [5,14,13,8,12]
    print(f"Concatenation value of {nums2}: {solution.findTheArrayConcVal(nums2)}")
