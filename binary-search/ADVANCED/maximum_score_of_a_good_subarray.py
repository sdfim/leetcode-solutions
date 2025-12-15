# Maximum Score of a Good Subarray
# Problem: https://leetcode.com/problems/maximum-score-of-a-good-subarray/

from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = k, k
        min_val = nums[k]
        res = min_val
        
        while l > 0 or r < n - 1:
            if l == 0:
                r += 1
            elif r == n - 1:
                l -= 1
            elif nums[l-1] < nums[r+1]:
                r += 1
            else:
                l -= 1
                
            min_val = min(min_val, nums[l], nums[r])
            res = max(res, min_val * (r - l + 1))
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumScore([1,4,3,7,4,5], 3)) # Output: 15
