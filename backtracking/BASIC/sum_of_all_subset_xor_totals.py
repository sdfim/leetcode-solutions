# Sum of All Subset XOR Totals
# Problem: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# Solution:

from typing import List

def subsetXORSum(nums: List[int]) -> int:
    def backtrack(index, current_xor):
        nonlocal total
        if index == len(nums):
            total += current_xor
            return

        backtrack(index + 1, current_xor ^ nums[index])
        backtrack(index + 1, current_xor)

    total = 0
    backtrack(0, 0)
    return total

if __name__ == "__main__":
    nums = [1, 3, 5]
    print(subsetXORSum(nums))
