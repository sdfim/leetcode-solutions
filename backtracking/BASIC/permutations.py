# Permutations
# Problem: https://leetcode.com/problems/permutations/
# Solution:

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))

