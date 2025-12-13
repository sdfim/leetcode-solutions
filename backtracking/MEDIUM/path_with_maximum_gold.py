# Path with Maximum Gold
# Problem: https://leetcode.com/problems/path-with-maximum-gold/
# Solution:

from typing import List

def getMaximumGold(grid: List[List[int]]) -> int:
    def backtrack(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0

        original = grid[r][c]
        grid[r][c] = 0
        max_gold = max(
            backtrack(r + 1, c),
            backtrack(r - 1, c),
            backtrack(r, c + 1),
            backtrack(r, c - 1)
        )
        grid[r][c] = original
        return original + max_gold

    return max(backtrack(r, c) for r in range(len(grid)) for c in range(len(grid[0])))

if __name__ == "__main__":
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    print(getMaximumGold(grid))
