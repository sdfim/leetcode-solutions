# Max Sum of Rectangle No Larger Than K
# Problem: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        
        # Iterate over pair of columns? Or rows.
        # Try columns (left, right)
        
        for l in range(n):
            row_sums = [0] * m
            for r in range(l, n):
                # Add column r to row_sums
                for i in range(m):
                    row_sums[i] += matrix[i][r]
                    
                # Find max subarray sum <= k in row_sums
                # Use prefix sums and bisect
                sorted_prefix = [0]
                curr = 0
                for x in row_sums:
                    curr += x
                    # We want curr - prev <= k  =>  prev >= curr - k
                    idx = bisect.bisect_left(sorted_prefix, curr - k)
                    if idx < len(sorted_prefix):
                        res = max(res, curr - sorted_prefix[idx])
                    
                    bisect.insort(sorted_prefix, curr)
                    
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))  # Output: 2
