# Minimum Operations to Make All Array Elements Equal
# Problem: https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            
        ans = []
        for x in queries:
            # Find split point
            # nums[idx] >= x
            idx = bisect.bisect_left(nums, x)
            
            # Left part: nums[0...idx-1] are < x.
            # Cost: x * count_left - sum_left
            count_left = idx
            sum_left = prefix[idx]
            cost_left = (count_left * x) - sum_left
            
            # Right part: nums[idx...n-1] are >= x.
            # Cost: sum_right - x * count_right
            count_right = n - idx
            sum_right = prefix[n] - prefix[idx]
            cost_right = sum_right - (count_right * x)
            
            ans.append(cost_left + cost_right)
            
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([3,1,6,8], [1,5])) # [14, 10]
