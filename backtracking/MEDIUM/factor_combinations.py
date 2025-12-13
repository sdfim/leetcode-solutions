# Factor Combinations
# Problem: https://leetcode.com/problems/factor-combinations/
# Solution:

from typing import List

def getFactors(n: int) -> List[List[int]]:
    def backtrack(start, product, path):
        if product == n:
            if len(path) > 1:
                result.append(path[:])
            return

        for i in range(start, n // product + 1):
            if n % i == 0:
                path.append(i)
                backtrack(i, product * i, path)
                path.pop()

    result = []
    backtrack(2, 1, [])
    return result

if __name__ == "__main__":
    n = 16
    print(getFactors(n))
