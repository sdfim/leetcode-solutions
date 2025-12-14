# Subsets II
# Problem: https://leetcode.com/problems/subsets-ii/
# Solution:

from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:

    def backtrack(start, path):
        result.append(list(path))

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)

            path.pop()

    nums.sort()
    result = []
    backtrack(0, [])
    return result

if __name__ == "__main__":
    nums = [1, 2, 2]
    print(subsetsWithDup(nums))
