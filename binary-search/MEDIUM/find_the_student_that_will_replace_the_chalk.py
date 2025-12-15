# Find the Student that Will Replace the Chalk
# Problem: https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

from typing import List
import bisect

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        
        # Find first i such that prefix_sum[i] > k.
        # Construct prefix sum array.
        
        prefix = []
        curr = 0
        for c in chalk:
            curr += c
            prefix.append(curr)
            
        # Binary search for k in prefix.
        # We want the first index where value > k.
        return bisect.bisect_right(prefix, k)

if __name__ == "__main__":
    solution = Solution()
    print(solution.chalkReplacer([5,1,5], 22)) # 0
