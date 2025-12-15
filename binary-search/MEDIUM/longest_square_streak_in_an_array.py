# Longest Square Streak in an Array
# Problem: https://leetcode.com/problems/longest-square-streak-in-an-array/

from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        nums.sort()
        max_len = -1
        
        visited = set()
        
        for x in nums:
            if x in visited:
                continue
            
            curr = x
            streak = 0
            while curr in s:
                visited.add(curr)
                streak += 1
                curr = curr * curr
                
            if streak >= 2:
                max_len = max(max_len, streak)
                
        return max_len

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSquareStreak([4,3,6,16,8,2])) # 3 (2, 4, 16)
