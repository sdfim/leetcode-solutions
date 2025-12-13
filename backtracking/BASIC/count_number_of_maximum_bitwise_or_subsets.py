# Count Number of Maximum Bitwise-OR Subsets
# Problem: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
# Solution:

from typing import List

def countMaxOrSubsets(nums: List[int]) -> int:
    def backtrack(index, current_or):
        nonlocal count
        if index == len(nums):
            if current_or == max_or:
                count += 1
            return

        backtrack(index + 1, current_or | nums[index])
        backtrack(index + 1, current_or)

    max_or = 0
    for num in nums:
        max_or |= num

    count = 0
    backtrack(0, 0)
    return count

if __name__ == "__main__":
    nums = [3, 1]
    print(countMaxOrSubsets(nums))
