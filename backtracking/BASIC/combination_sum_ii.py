# Combination Sum II
# Problem: https://leetcode.com/problems/combination-sum-ii/
# Solution:

from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(remaining, start, path):
        if remaining == 0:
            result.append(list(path))
            return
        elif remaining < 0:
            return

        prev = -1
        for i in range(start, len(candidates)):
            if candidates[i] == prev:
                continue
            path.append(candidates[i])
            backtrack(remaining - candidates[i], i + 1, path)
            path.pop()
            prev = candidates[i]

    candidates.sort()
    result = []
    backtrack(target, 0, [])
    return result

if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combinationSum2(candidates, target))
