# Minimize Maximum Pair Sum in Array
# Problem: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# Solution:

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        l, r = 0, len(nums) - 1
        
        while l < r:
            max_sum = max(max_sum, nums[l] + nums[r])
            l += 1
            r -= 1
            
        return max_sum

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3,5,2,3]
    print(f"Min max pair sum of {nums1}: {solution.minPairSum(nums1)}")
    
    nums2 = [3,5,4,2,4,6]
    print(f"Min max pair sum of {nums2}: {solution.minPairSum(nums2)}")
