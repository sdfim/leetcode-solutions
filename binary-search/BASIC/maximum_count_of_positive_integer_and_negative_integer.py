# Maximum Count of Positive Integer and Negative Integer
# Problem: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

from typing import List
import bisect

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect.bisect_left(nums, 0) # Elements < 0
        pos = len(nums) - bisect.bisect_right(nums, 0) # Elements > 0
        return max(neg, pos)

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumCount([-2,-1,-1,1,2,3]))  # Output: 3
    print(solution.maximumCount([-3,-2,-1,0,0,1,2])) # Output: 3
