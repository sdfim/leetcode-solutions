# Tiling a Rectangle with the Fewest Squares
# Problem: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
# Solution:

def tilingRectangle(n: int, m: int) -> int:
    def dfs(x, y, used):
        nonlocal min_squares
        if used >= min_squares:
            return
        if x >= n:
            min_squares = used
            return
        if y >= m:
            dfs(x + 1, 0, used)
            return
        if grid[x][y]:
            dfs(x, y + 1, used)
            return

        for size in range(min(n - x, m - y), 0, -1):
            if all(grid[x + dx][y + dy] == 0 for dx in range(size) for dy in range(size)):
                for dx in range(size):
                    for dy in range(size):
                        grid[x + dx][y + dy] = 1
                dfs(x, y + size, used + 1)
                for dx in range(size):
                    for dy in range(size):
                        grid[x + dx][y + dy] = 0

    grid = [[0] * m for _ in range(n)]
    min_squares = float("inf")
    dfs(0, 0, 0)
    return min_squares

if __name__ == "__main__":
    n, m = 2, 3
    print(tilingRectangle(n, m))
