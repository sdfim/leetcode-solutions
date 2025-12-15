# Number of Subsequences That Satisfy the Given Sum Condition
# Problem: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                # nums[l] is min, nums[r] is max.
                # Any subsequence including nums[l] and subset of nums[l+1...r] is valid?
                # Condition: min + max <= target.
                # If we pick nums[l] as min, and any subset of the elements between l+1 and r (inclusive of r?),
                # then max will be <= nums[r].
                # Wait, if we pick a subset from nums[l...r], and we MUST include nums[l] as the minimum.
                # The maximum element in that subset will be some nums[k] where k <= r.
                # Since nums[l] + nums[r] <= target, and array is sorted, nums[l] + nums[k] <= target for any k <= r.
                # So any subsequence formed by nums[l] combined with any elements from nums[l+1...r] is valid.
                # Number of such elements is r - l.
                # Number of subsets is 2^(r-l).
                
                res = (res + pow(2, r - l, mod)) % mod
                l += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubseq([3,5,6,7], 9))  # Output: 4
