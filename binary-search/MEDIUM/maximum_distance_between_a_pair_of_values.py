# Maximum Distance Between a Pair of Values
# Problem: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        ans = 0
        
        # Both arrays are sorted non-increasing
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance([55,30,5,4,2], [100,20,10,10,5])) # 2
