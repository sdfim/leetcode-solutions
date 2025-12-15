# Minimum Size Subarray Sum
# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Two pointers approach is O(N)
        # Binary Search approach is O(N log N)
        # 1. Prefix sums
        n = len(nums)
        if n == 0: return 0
        
        # O(N) approach (Two Pointers)
        ans = n + 1
        left = 0
        s = 0
        for right in range(n):
            s += nums[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        
        return ans if ans <= n else 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
