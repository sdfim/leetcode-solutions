# Merge Two 2D Arrays by Summing Values
# Problem: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
# Solution:

from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 == id2:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                res.append([id1, val1])
                i += 1
            else:
                res.append([id2, val2])
                j += 1
                
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
            
        while j < len(nums2):
            res.append(nums2[j])
            j += 1
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    print(f"Merged 2D arrays: {solution.mergeArrays(nums1, nums2)}")
