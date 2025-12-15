# Longest Subsequence With Limited Sum
# Problem: https://leetcode.com/problems/longest-subsequence-with-limited-sum/

from typing import List
import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
            
        res = []
        for q in queries:
            count = bisect.bisect_right(prefix, q) - 1
            res.append(count)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.answerQueries([4,5,2,1], [3,10,21]))  # Output: [2, 3, 4]
