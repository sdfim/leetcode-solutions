# Frequency of the Most Frequent Element
# Problem: https://leetcode.com/problems/frequency-of-the-most-frequent-element/

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        # Sliding window
        left = 0
        curr_sum = 0
        res = 0
        
        for right in range(len(nums)):
            target = nums[right]
            curr_sum += target
            
            # Condition: (right - left + 1) * target - curr_sum <= k
            while (right - left + 1) * target - curr_sum > k:
                curr_sum -= nums[left]
                left += 1
                
            res = max(res, right - left + 1)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxFrequency([1,2,4], 5))  # Output: 3
