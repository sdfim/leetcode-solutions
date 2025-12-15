# Zero Array Transformation II
# Problem: https://leetcode.com/problems/zero-array-transformation-ii/

from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Binary search k (number of queries).
        n = len(nums)
        m = len(queries)
        
        def check(k):
            # Apply first k queries. Count diffs.
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r+1] -= val
            
            curr = 0
            for i in range(n):
                curr += diff[i]
                if curr < nums[i]:
                    return False
            return True
            
        left, right = 0, m
        ans = -1
        
        # Does 0 queries work? If sum(nums) == 0.
        if check(0): return 0
        
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                left = 1
                continue
                
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]])) # 2
