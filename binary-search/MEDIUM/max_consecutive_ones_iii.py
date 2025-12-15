# Max Consecutive Ones III
# Problem: https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding window.
        left = 0
        zeros = 0
        ans = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
