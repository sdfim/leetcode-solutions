# Sudoku Solver
# Problem: https://leetcode.com/problems/sudoku-solver/
# Solution:

from typing import List

def solveSudoku(board: List[List[str]]) -> None:
    def is_valid(r, c, num):
        block_r, block_c = 3 * (r // 3), 3 * (c // 3)
        return (
            num not in rows[r] and
            num not in cols[c] and
            num not in blocks[block_r + block_c]
        )

    def place_number(r, c, num):
        rows[r].add(num)
        cols[c].add(num)
        blocks[3 * (r // 3) + (c // 3)].add(num)
        board[r][c] = str(num)

    def remove_number(r, c, num):
        rows[r].remove(num)
        cols[c].remove(num)
        blocks[3 * (r // 3) + (c // 3)].remove(num)
        board[r][c] = "."

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in range(1, 10):
                        if is_valid(r, c, num):
                            place_number(r, c, num)
                            if backtrack():
                                return True
                            remove_number(r, c, num)
                    return False
        return True

    rows, cols, blocks = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                num = int(board[r][c])
                rows[r].add(num)
                cols[c].add(num)
                blocks[3 * (r // 3) + (c // 3)].add(num)

    backtrack()

if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solveSudoku(board)
    print(board)
