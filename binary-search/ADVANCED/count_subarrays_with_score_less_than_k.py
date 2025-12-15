# Count Subarrays With Score Less Than K
# Problem: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Score = sum * length
        # Subarray [i...j]
        # Since nums > 0, score increases strictly as we extend right.
        
        count = 0
        left = 0
        current_sum = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # While score >= k, shrink from left
            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            
            # All subarrays ending at right and starting at s >= left are valid
            # Number of such subarrays = right - left + 1
            count += (right - left + 1)
            
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([2,1,4,3,5], 10)) # Output: 6
