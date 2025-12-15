# Minimum Operations to Reduce X to Zero
# Problem: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        
        # Find longest subarray with sum == target
        max_len = -1
        curr_sum = 0
        left = 0
        n = len(nums)
        
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1
            
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return n - max_len if max_len != -1 else -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([1,1,4,2,3], 5))  # Output: 2
