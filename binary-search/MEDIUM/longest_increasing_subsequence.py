# Longest Increasing Subsequence
# Problem: https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for n in nums:
            idx = bisect.bisect_left(tails, n)
            if idx < len(tails):
                tails[idx] = n
            else:
                tails.append(n)
        return len(tails)

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Output: 4
