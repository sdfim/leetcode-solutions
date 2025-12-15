# Count Pairs Whose Sum is Less than Target
# Problem: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        
        while l < r:
            if nums[l] + nums[r] < target:
                count += (r - l)
                l += 1
            else:
                r -= 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPairs([-1,1,2,3,1], 2))  # Output: 3
