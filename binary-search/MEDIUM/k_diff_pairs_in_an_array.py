# K-diff Pairs in an Array
# Problem: https://leetcode.com/problems/k-diff-pairs-in-an-array/

from typing import List
import bisect

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = nums[i] + k
            # Search for target starting from i+1
            # We can use bisect. But we just need to check existence.
            
            idx = bisect.bisect_left(nums, target, lo=i+1)
            if idx < n and nums[idx] == target:
                count += 1
                
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.findPairs([3,1,4,1,5], 2))  # Output: 2
