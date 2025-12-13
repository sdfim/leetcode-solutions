# Non-decreasing Subsequences
# Problem: https://leetcode.com/problems/non-decreasing-subsequences/
# Solution:

from typing import List

def findSubsequences(nums: List[int]) -> List[List[int]]:
    def backtrack(start, path):
        if len(path) > 1:
            result.append(path[:])
        seen = set()
        for i in range(start, len(nums)):
            if nums[i] in seen or (path and nums[i] < path[-1]):
                continue
            seen.add(nums[i])
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    nums = [4, 6, 7, 7]
    print(findSubsequences(nums))
