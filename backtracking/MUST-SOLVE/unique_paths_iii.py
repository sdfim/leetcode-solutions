# Unique Paths III
# Problem: https://leetcode.com/problems/unique-paths-iii/
# Solution:

from typing import List

def uniquePathsIII(grid: List[List[int]]) -> int:
    def backtrack(r, c, remain):
        if grid[r][c] == 2:
            return remain == 0

        temp = grid[r][c]
        grid[r][c] = -4
        paths = 0

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] >= 0:
                paths += backtrack(nr, nc, remain - 1)

        grid[r][c] = temp
        return paths

    rows, cols = len(grid), len(grid[0])
    start_r = start_c = end_r = end_c = empty = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                start_r, start_c = r, c
            elif grid[r][c] == 2:
                end_r, end_c = r, c
            elif grid[r][c] == 0:
                empty += 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    return backtrack(start_r, start_c, empty + 1)

if __name__ == "__main__":
    grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]
    ]
    print(uniquePathsIII(grid))
