# Unique Paths III
# Problem: https://leetcode.com/problems/unique-paths-iii/
# Solution:

from typing import List

def uniquePathsIII(grid: List[List[int]]) -> int:
    def backtrack(x, y, remain):
        if grid[x][y] == 2:
            return remain == 1

        temp, grid[x][y] = grid[x][y], -4
        paths = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] >= 0:
                paths += backtrack(nx, ny, remain - 1)
        grid[x][y] = temp
        return paths

    start_x = start_y = remain = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                start_x, start_y = i, j
            elif grid[i][j] == 0:
                remain += 1

    return backtrack(start_x, start_y, remain + 1)

if __name__ == "__main__":
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    print(uniquePathsIII(grid))
