# Subarray Product Less Than K
# Problem: https://leetcode.com/problems/subarray-product-less-than-k/

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        prod = 1
        ans = 0
        left = 0
        
        # Sliding window, technically O(N).
        # Could be binary search if we used prefix logs?
        # But this is effectively standard for this problem.
        # Strict "Binary Search" approach involves computing prefix logs, then for each i,
        # finding max j such that prefix[j] - prefix[i] < log(k). O(N log N).
        # We'll use the optimal O(N) sliding window.
        
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK([10,5,2,6], 100))  # Output: 8
