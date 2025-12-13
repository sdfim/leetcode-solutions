# Number of Squareful Arrays
# Problem: https://leetcode.com/problems/number-of-squareful-arrays/
# Solution:

from typing import List
from math import sqrt
from collections import Counter

def numSquarefulPerms(nums: List[int]) -> int:
    def is_squareful(x, y):
        s = sqrt(x + y)
        return int(s) == s

    def backtrack(path):
        if len(path) == len(nums):
            return 1

        count = 0
        for num in counter:
            if counter[num] > 0 and (not path or is_squareful(path[-1], num)):
                counter[num] -= 1
                count += backtrack(path + [num])
                counter[num] += 1
        return count

    counter = Counter(nums)
    return backtrack([])

if __name__ == "__main__":
    nums = [1, 17, 8]
    print(numSquarefulPerms(nums))
