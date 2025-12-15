# Minimum Limit of Balls in a Bag
# Problem: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

from typing import List
import math

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Check if max_balls is possible within maxOperations
        def can(max_balls):
            ops = 0
            for n in nums:
                if n > max_balls:
                    # ops += (n - 1) // max_balls
                    ops += math.ceil(n / max_balls) - 1
            return ops <= maxOperations
            
        left, right = 1, max(nums)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSize([9], 2))  # Output: 3
    print(solution.minimumSize([2,4,8,2], 4)) # Output: 2
