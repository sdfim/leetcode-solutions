# Minimum Number of Removals to Make Mountain Array
# Problem: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

from typing import List
import bisect

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # LIS from left
        lis = [1] * n
        tails = []
        for i in range(n):
            idx = bisect.bisect_left(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
            lis[i] = idx + 1
            
        # LDS from right (LIS on reversed)
        lds = [1] * n
        tails = []
        for i in range(n - 1, -1, -1):
            idx = bisect.bisect_left(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
            lds[i] = idx + 1
            
        max_mountain = 0
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:
                max_mountain = max(max_mountain, lis[i] + lds[i] - 1)
                
        return n - max_mountain

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumMountainRemovals([2,1,1,5,6,2,3,1])) # Output: 3
