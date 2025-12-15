# Split Array Largest Sum
# Problem: https://leetcode.com/problems/split-array-largest-sum/

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            splits = 1
            curr_sum = 0
            for n in nums:
                if curr_sum + n > max_sum:
                    splits += 1
                    curr_sum = n
                else:
                    curr_sum += n
            return splits <= k
            
        left, right = max(nums), sum(nums)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.splitArray([7,2,5,10,8], 2))  # Output: 18
