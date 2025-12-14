# Minimum Pair Removal to Sort Array II
# Problem: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
# Solution:

from typing import List

class Solution:
    def minRemovals(self, nums: List[int]) -> int:
        stack = []
        removals = 0

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
                removals += 1
            stack.append(num)

        return removals

if __name__ == "__main__":
    # Example use case
    solution = Solution()
    nums = [5, 3, 4, 2, 1]
    print(solution.minRemovals(nums))  # Example output
