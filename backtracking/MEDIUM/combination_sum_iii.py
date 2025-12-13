# Combination Sum III
# Problem: https://leetcode.com/problems/combination-sum-iii/
# Solution:

from typing import List

def combinationSum3(k: int, n: int) -> List[List[int]]:
    def backtrack(start, remaining, path):
        if len(path) == k:
            if remaining == 0:
                result.append(path[:])
            return
        for i in range(start, 10):
            if i > remaining:
                break
            path.append(i)
            backtrack(i + 1, remaining - i, path)
            path.pop()

    result = []
    backtrack(1, n, [])
    return result

if __name__ == "__main__":
    k, n = 3, 7
    print(combinationSum3(k, n))
