# Minimum Common Value
# Problem: https://leetcode.com/problems/minimum-common-value/
# Solution:

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
                
        return -1

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,2,3]
    nums2 = [2,4]
    print(f"Minimum common value: {solution.getCommon(nums1, nums2)}")
