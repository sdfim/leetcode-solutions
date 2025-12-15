# Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# Problem: https://leetcode.com/problems/maximum-side-length-of-a-square/

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1] + mat[i-1][j-1]
                
        def get_sum(x1, y1, x2, y2):
            return pref[x2+1][y2+1] - pref[x1][y2+1] - pref[x2+1][y1] + pref[x1][y1]
            
        def can(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if get_sum(i, j, i+k-1, j+k-1) <= threshold:
                        return True
            return False
            
        left, right = 0, min(m, n)
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                left = 1
                continue
            if can(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == "__main__":
    solution = Solution()
    mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
    print(solution.maxSideLength(mat, 4))  # Output: 2
