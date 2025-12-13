# Combination Sum
# Problem: https://leetcode.com/problems/combination-sum/
# Solution:

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(remaining, start, path):
        if remaining == 0:
            result.append(list(path))
            return
        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(remaining - candidates[i], i, path)
            path.pop()

    result = []
    backtrack(target, 0, [])
    return result

if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(combinationSum(candidates, target))
