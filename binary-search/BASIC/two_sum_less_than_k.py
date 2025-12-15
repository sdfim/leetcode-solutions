# Two Sum Less Than K
# Problem: https://leetcode.com/problems/two-sum-less-than-k/

from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        max_sum = -1
        
        # Two Pointers approach
        while i < j:
            s = nums[i] + nums[j]
            if s < k:
                max_sum = max(max_sum, s)
                i += 1
            else:
                j -= 1
        
        return max_sum
        
        # NOTE: This problem is categorized under Binary Search sometimes because
        # for each element you can BS the complement.
        # But Two Pointers is O(N log N) dominated by sort, same as N log N for BS.
        # Two Pointers is generally cleaner.

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSumLessThanK([34,23,1,24,75,33,54,8], 60))  # Output: 58
