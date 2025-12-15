# Kth Smallest Element in a Sorted Matrix
# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from typing import List
import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        start, end = matrix[0][0], matrix[n-1][n-1]
        
        while start < end:
            mid = (start + end) // 2
            # Count elements <= mid
            count = 0
            for row in matrix:
                count += bisect.bisect_right(row, mid)
            
            if count < k:
                start = mid + 1
            else:
                end = mid
                
        return start

if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))  # Output: 13
