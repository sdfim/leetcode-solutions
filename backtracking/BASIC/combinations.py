# Combinations
# Problem: https://leetcode.com/problems/combinations/
# Solution:

from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(1, [])
    return result

if __name__ == "__main__":
    n = 4
    k = 2
    print(combine(n, k))
