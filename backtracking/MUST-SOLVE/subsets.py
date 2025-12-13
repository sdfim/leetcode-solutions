# Subsets
# Problem: https://leetcode.com/problems/subsets/
# Solution:

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    def backtrack(start, path):
        result.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))
