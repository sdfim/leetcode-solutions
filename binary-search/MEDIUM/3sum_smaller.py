# 3Sum Smaller
# Problem: https://leetcode.com/problems/3sum-smaller/

from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < target:
                    # If (i, left, right) satisfies the condition,
                    # then (i, left, right-1), (i, left, right-2)... all satisfy
                    # because they are smaller than nums[right].
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
                    
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumSmaller([-2,0,1,3], 2))  # Output: 2
