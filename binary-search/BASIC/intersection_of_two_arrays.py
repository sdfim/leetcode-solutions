# Intersection of Two Arrays
# Problem: https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
                
        return res
        
        # Alternatively using Binary Search for each element if sizes differ significantly
        # But Sort + Two Pointers is generally standard here alongside Set.

if __name__ == "__main__":
    solution = Solution()
    print(solution.intersection([1,2,2,1], [2,2]))  # Output: [2]
