# Max Consecutive Ones III
# Problem: https://leetcode.com/problems/max-consecutive-ones-iii/
# Solution:

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count = 0
        res = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
                
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1,1,1,0,0,0,1,1,1,1,0]
    k1 = 2
    print(f"Max consecutive ones III {nums1}, k={k1}: {solution.longestOnes(nums1, k1)}")
