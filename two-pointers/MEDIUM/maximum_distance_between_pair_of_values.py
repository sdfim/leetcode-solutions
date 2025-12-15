# Maximum Distance Between a Pair of Values
# Problem: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
# Solution:

from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        res = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [55,30,5,4,2]
    nums2 = [100,20,10,10,5]
    print(f"Max distance {nums1}, {nums2}: {solution.maxDistance(nums1, nums2)}")
    
    nums1 = [2,2,2]
    nums2 = [10,10,1]
    print(f"Max distance {nums1}, {nums2}: {solution.maxDistance(nums1, nums2)}")
