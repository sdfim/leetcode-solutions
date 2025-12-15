# Minimum Operations to Make the Array K-Increasing
# Problem: https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

from typing import List
import bisect

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        saved = 0
        
        for start in range(k):
            # Extract subsequence
            sub = []
            for i in range(start, n, k):
                sub.append(arr[i])
                
            # Find LIS (non-decreasing) of sub
            # For non-decreasing, use bisect_right
            tails = []
            for x in sub:
                idx = bisect.bisect_right(tails, x)
                if idx == len(tails):
                    tails.append(x)
                else:
                    tails[idx] = x
            
            # Length of LIS is length of subsequence we KEEP
            # Operations = len(sub) - len(LIS)
            saved += len(tails)
            
        return n - saved

if __name__ == "__main__":
    solution = Solution()
    print(solution.kIncreasing([5,4,3,2,1], 1)) # 4
