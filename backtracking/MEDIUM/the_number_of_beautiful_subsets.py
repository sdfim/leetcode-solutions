# The Number of Beautiful Subsets
# Problem: https://leetcode.com/problems/the-number-of-beautiful-subsets/
# Solution:

from typing import List

def beautifulSubsets(nums: List[int], k: int) -> int:
    def backtrack(index, subset):
        if index == len(nums):
            return 1 if len(subset) >= k else 0
        count = backtrack(index + 1, subset)
        subset.append(nums[index])
        count += backtrack(index + 1, subset)
        subset.pop()
        return count

    return backtrack(0, [])

if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 2
    print(beautifulSubsets(nums, k))
