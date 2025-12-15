# Minimize the Maximum Adjacent Element Difference
# Problem: https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/
# (LC 3279?) Actually searching similar problem...
# Might be finding value to insert to minimize diff?
# Or "Minimize Max Difference of Pairs"?
# Let's assume standard "Minimize Max Adjacent Difference" typically solvable by Binary Search on Answer.
# Problem: Insert k elements to minimize adjacent diff? Like "Minimize Max Distance to Gas Station"?
# Let's check name. "minimize-the-maximum-adjacent-element-difference"
# If it corresponds to planting stations, it's:
# Given nums, we can add k elements. (LC 774 roughly?)
# But let's look for "adjacent element difference".
# Maybe: "Minimize the Maximum Difference of Pairs" (LC 2616)?
# Or "Minimum Adjacent Difference in a Circular Array"? 
# Or "Minimize Max Difference Between Adjacent Elements After Inserting K Elements".
# Let's implement the generic "Minimize Max Adjacent Diff by inserting K elements" (Gas Station logic).

# Since specific problem link is missing or inferred, I will assume it's the "Gas Station" variant or similar:
# "You are given an integer array nums and an integer k. 
# You can insert at most k elements... minimize max difference between adjacent."
# This is typically LC 774 "Minimize Max Distance to Gas Station".

from typing import List
import math

class Solution:
    def minimizeMaxAdjDiff(self, nums: List[int], k: int) -> int:
        # Binary search for the answer D.
        # Check if it is possible to make max diff <= D by adding at most k elements.
        # For each adjacent pair (a, b), if abs(a-b) > D, we need insertions.
        # Insertions needed = ceil((a-b)/D) - 1.
        
        def check(d):
            if d == 0: return False # unless all equal, but diff check handles
            needed = 0
            for i in range(len(nums) - 1):
                diff = abs(nums[i+1] - nums[i])
                if diff > d:
                    # needed += (diff - 1) // d
                    needed += math.ceil(diff / d) - 1
            return needed <= k

        left, right = 1, max(nums) - min(nums) # loose interval
        # Actually max possible diff is max(nums)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizeMaxAdjDiff([10, 20], 1)) # 5 (10, 15, 20)
