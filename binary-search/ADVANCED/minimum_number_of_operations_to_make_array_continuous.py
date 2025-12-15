# Minimum Number of Operations to Make Array Continuous
# Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # We want to choose a range [x, x + n - 1].
        # We want to maximize the number of existing elements that fall into this range.
        # Duplicates in the final range are not allowed (must be continuous distinct integers).
        # But we can change duplicates to other numbers.
        # So essentially, we just need to count distinct numbers already in [x, x + n - 1].
        
        sorted_unique = sorted(set(nums))
        m = len(sorted_unique)
        max_kept = 0
        
        for i, start_val in enumerate(sorted_unique):
            end_val = start_val + n - 1
            # Find index of first element > end_val using bisect_right
            idx = bisect.bisect_right(sorted_unique, end_val)
            
            # Elements in range are from index i to idx - 1
            count = idx - i
            max_kept = max(max_kept, count)
            
        return n - max_kept

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([4,2,5,3])) # Output: 0
    print(solution.minOperations([1,2,3,5,6])) # Output: 1
