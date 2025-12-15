# Merge Operations to Turn Array Into a Palindrome
# Problem: https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/
# Solution:

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ops = 0
        
        while l < r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else:
                if nums[l] < nums[r]:
                    nums[l+1] += nums[l]
                    l += 1
                else:
                    nums[r-1] += nums[r]
                    r -= 1
                ops += 1
                
        return ops

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [4,3,2,1,2,3,1]
    print(f"Ops to palindrome {nums1}: {solution.minimumOperations(nums1)}")
