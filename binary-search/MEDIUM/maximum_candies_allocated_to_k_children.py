# Maximum Candies Allocated to K Children
# Problem: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
            
        def check(x):
            if x == 0: return True
            count = 0
            for pile in candies:
                count += pile // x
            return count >= k
            
        left, right = 1, max(candies)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumCandies([5,8,6], 3)) # 5
