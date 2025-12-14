# Spiral Matrix IV
# Problem: https://leetcode.com/problems/spiral-matrix-iv/
# Solution:

from typing import List, Optional
from linked_list.utils import ListNode

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        row, col = 0, 0

        current = head
        for _ in range(m * n):
            if not current:
                break
            matrix[row][col] = current.val
            current = current.next

            next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
            if not (0 <= next_row < m and 0 <= next_col < n and matrix[next_row][next_col] == -1):
                direction_idx = (direction_idx + 1) % 4

            row, col = row + directions[direction_idx][0], col + directions[direction_idx][1]

        return matrix

if __name__ == "__main__":
    # Example use case
    from linked_list.utils import create_linked_list
    head = create_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
    solution = Solution()
    result = solution.spiralMatrix(3, 5, head)
    print("Spiral matrix:")
    for row in result:
        print(row)
