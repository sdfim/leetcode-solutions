# Number of Subsequences That Satisfy the Given Sum Condition
# Problem: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# Solution:

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
                # If nums[l] + nums[r] <= target, then all subsequences starting with nums[l] 
                # and ending with any element from index l to r are valid.
                # The number of such subsequences (fixing nums[l]) is 2^(r-l).
                res = (res + pow(2, r - l, mod)) % mod
                l += 1
                
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3,5,6,7]
    target1 = 9
    print(f"Num subsequences sum <= {target1} in {nums1}: {solution.numSubseq(nums1, target1)}")
    
    nums2 = [3,3,6,8]
    target2 = 10
    print(f"Num subsequences sum <= {target2} in {nums2}: {solution.numSubseq(nums2, target2)}")
