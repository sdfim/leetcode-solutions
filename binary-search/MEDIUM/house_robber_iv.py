# House Robber IV
# Problem: https://leetcode.com/problems/house-robber-iv/

from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Minimize the maximum capability (max value of stolen house).
        # Binary search on capability C.
        # Check if we can steal k houses such that all <= C, no adj.
        # Greedy check: iterate, if nums[i] <= C, take it and skip next.
        
        def check(c):
            count = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= c:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k
            
        left, right = min(nums), max(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCapability([2,3,5,9], 2)) # 5
