# Permutations II
# Problem: https://leetcode.com/problems/permutations-ii/
# Solution:

from typing import List

def permuteUnique(nums: List[int]) -> List[List[int]]:

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        seen = set()

        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue

            seen.add(nums[i])

            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    nums.sort()
    result = []
    backtrack(0)
    return result

if __name__ == "__main__":
    nums = [1, 1, 2]
    print(permuteUnique(nums))
