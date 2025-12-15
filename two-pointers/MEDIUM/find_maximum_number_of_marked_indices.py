# Find the Maximum Number of Marked Indices
# Problem: https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/
# Solution:

from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l, r = 0, n // 2
        count = 0
        
        while l < n // 2 and r < n:
            if 2 * nums[l] <= nums[r]:
                count += 2
                l += 1
                r += 1
            else:
                r += 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3,5,2,4]
    print(f"Max marked indices {nums1}: {solution.maxNumOfMarkedIndices(nums1)}")
    
    nums2 = [9,2,5,4]
    print(f"Max marked indices {nums2}: {solution.maxNumOfMarkedIndices(nums2)}")
