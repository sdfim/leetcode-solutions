# Maximize Score After N Operations
# Problem: https://leetcode.com/problems/maximize-score-after-n-operations/
# Solution:

from typing import List
from math import gcd

def maxScore(nums: List[int]) -> int:
    def backtrack(mask, pairs):
        if pairs == 0:
            return 0

        if (mask, pairs) in memo:
            return memo[(mask, pairs)]

        max_score = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if not (mask & (1 << i)) and not (mask & (1 << j)):
                    new_mask = mask | (1 << i) | (1 << j)
                    score = pairs * gcd(nums[i], nums[j])
                    max_score = max(max_score, score + backtrack(new_mask, pairs - 1))

        memo[(mask, pairs)] = max_score
        return max_score

    memo = {}
    return backtrack(0, len(nums) // 2)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print(maxScore(nums))
