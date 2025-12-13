# Distribute Repeating Integers
# Problem: https://leetcode.com/problems/distribute-repeating-integers/
# Solution:

from typing import List
from collections import Counter

def canDistribute(nums: List[int], quantity: List[int]) -> bool:
    def backtrack(index):
        if index == len(quantity):
            return True

        for i in range(len(counts)):
            if counts[i] >= quantity[index]:
                counts[i] -= quantity[index]
                if backtrack(index + 1):
                    return True
                counts[i] += quantity[index]

        return False

    counts = list(Counter(nums).values())
    quantity.sort(reverse=True)
    return backtrack(0)

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    quantity = [2]
    print(canDistribute(nums, quantity))
