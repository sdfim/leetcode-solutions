# Count Pairs in Two Arrays
# Problem: https://leetcode.com/problems/count-pairs-in-two-arrays/

from typing import List
import bisect

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        # Condition: nums1[i] + nums1[j] > nums2[i] + nums2[j]
        # Rewrite: (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0
        
        n = len(nums1)
        diff = []
        for i in range(n):
            diff.append(nums1[i] - nums2[i])
            
        diff.sort()
        
        # pairs (i, j) with i < j and diff[i] + diff[j] > 0
        # For each i, find count of j > i such that diff[j] > -diff[i].
        # Since we sorted diff, indices don't correspond to original i,j.
        # But order doesn't matter for "pairs" (i,j) distinct.
        # We just need count of pairs of indices (x, y) with x != y such that diff[x] + diff[y] > 0.
        # Divide by 2 at end? Or iterate.
        # Two pointers approach.
        
        left, right = 0, n - 1
        ans = 0
        while left < right:
            if diff[left] + diff[right] > 0:
                # If diff[left] + diff[right] > 0, then diff[k] + diff[right] > 0 for all k in [left, right-1].
                # Because diff is sorted increasing.
                # So (right-left) pairs can be formed with 'right'.
                ans += (right - left)
                right -= 1
            else:
                # Sum <= 0. Need larger values.
                left += 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs([2,1,2,1], [1,2,1,3])) # 1
