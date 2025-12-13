# Sliding Puzzle
# Problem: https://leetcode.com/problems/sliding-puzzle/
# Solution:

from typing import List
from collections import deque

def slidingPuzzle(board: List[List[int]]) -> int:
    def neighbors(state):
        zero = state.index("0")
        x, y = zero // 3, zero % 3
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < 3:
                new_state = list(state)
                new_state[zero], new_state[nx * 3 + ny] = new_state[nx * 3 + ny], new_state[zero]
                yield "".join(new_state)

    start = "".join(str(num) for row in board for num in row)
    target = "123450"
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, steps = queue.popleft()
        if state == target:
            return steps

        for neighbor in neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

    return -1

if __name__ == "__main__":
    board = [[1, 2, 3], [4, 0, 5]]
    print(slidingPuzzle(board))
