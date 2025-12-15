# Find the Smallest Divisor Given a Threshold
# Problem: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            s = sum(math.ceil(n / mid) for n in nums)
            if s <= threshold:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestDivisor([1,2,5,9], 6))  # Output: 5
