# The K Weakest Rows in a Matrix
# Problem: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strengths = []
        m, n = len(mat), len(mat[0])
        
        for i, row in enumerate(mat):
            # Binary search first 0
            left, right = 0, n - 1
            ones = 0
            # Since 1s always before 0s, find first 0 index. 
            # If all 1s, count is n.
            
            # Find the position of the first 0
            pos = n
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 0:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            ones = pos
            strengths.append((ones, i))
            
        strengths.sort()
        return [idx for _, idx in strengths[:k]]

if __name__ == "__main__":
    solution = Solution()
    mat = [
        [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]
    ]
    print(solution.kWeakestRows(mat, 3))  # Output: [2, 0, 3]
