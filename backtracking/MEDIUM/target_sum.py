# Target Sum
# Problem: https://leetcode.com/problems/target-sum/
# Solution:

from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
    def backtrack(index, total):
        if index == len(nums):
            return 1 if total == target else 0
        return backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index])

    return backtrack(0, 0)

if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(findTargetSumWays(nums, target))
