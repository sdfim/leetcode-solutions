# Maximum Product of First and Last Elements of a Subsequence
# Problem: https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/
# Solution:

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # If subsequence length >= 2
        # Max product of first and last is just max pair product (order matters if it was subarray, 
        # but subsequence maintains relative order).
        # We need nums[i] * nums[j] where i < j.
        
        res = float('-inf')
        n = len(nums)
        
        # Optimized: track max/min seen so far
        # But we need O(N^2) for all pairs? No. 
        # Max product = max(nums[i] * nums[j])
        # Just find two numbers?
        
        # Iterate and keep track of max/min values seen on left
        max_seen = nums[0]
        min_seen = nums[0]
        
        for i in range(1, n):
            res = max(res, nums[i] * max_seen, nums[i] * min_seen)
            max_seen = max(max_seen, nums[i])
            min_seen = min(min_seen, nums[i])
            
        return res if n > 1 else 0

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    print(f"Max product: {solution.maxProduct(nums)}")
