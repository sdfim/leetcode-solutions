# Minimum Absolute Sum Difference
# Problem: https://leetcode.com/problems/minimum-absolute-sum-difference/

from typing import List
import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        # We can replace one nums1[i] with nums1[j].
        # We want to maximize decrease in absolute diff.
        
        # Original sum
        orig_diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_diff = sum(orig_diffs)
        
        sorted_nums1 = sorted(nums1)
        max_decrease = 0
        
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            current_diff = orig_diffs[i]
            
            # Find closest element in sorted_nums1 to b
            idx = bisect.bisect_left(sorted_nums1, b)
            
            candidates = []
            if idx < len(sorted_nums1):
                candidates.append(sorted_nums1[idx])
            if idx > 0:
                candidates.append(sorted_nums1[idx - 1])
                
            for cand in candidates:
                new_diff = abs(cand - b)
                decrease = current_diff - new_diff
                max_decrease = max(max_decrease, decrease)
                
        return (total_diff - max_decrease) % (10**9 + 7)

if __name__ == "__main__":
    solution = Solution()
    print(solution.minAbsoluteSumDiff([1,7,5], [2,3,5]))  # Output: 3
