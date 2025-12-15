# Find the Maximum Number of Marked Indices
# Problem: https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

from typing import List

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # Pair small with large such that 2*small <= large.
        # We can pick at most n/2 pairs.
        # Strategy: use first half for smalls, second half for larges.
        
        i, j = 0, n // 2
        count = 0
        while i < n // 2 and j < n:
            if 2 * nums[i] <= nums[j]:
                count += 2
                i += 1
                j += 1
            else:
                j += 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxNumOfMarkedIndices([3,5,2,4]))  # Output: 2
