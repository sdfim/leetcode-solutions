# Make Array Strictly Increasing
# Problem: https://leetcode.com/problems/make-array-strictly-increasing/

from typing import List
import bisect
import collections

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        # Remove duplicates in arr2
        unique_arr2 = []
        if arr2:
            unique_arr2.append(arr2[0])
            for i in range(1, len(arr2)):
                if arr2[i] != arr2[i-1]:
                    unique_arr2.append(arr2[i])
        arr2 = unique_arr2
        
        # dp[val] = min_ops
        # We store the minimum operations to reach a state where the Last Element is 'val'.
        dp = { -1: 0 }
        
        for num in arr1:
            new_dp = collections.defaultdict(lambda: float('inf'))
            for val, ops in dp.items():
                # Option 1: Keep current num if valid
                if num > val:
                    new_dp[num] = min(new_dp[num], ops)
                
                # Option 2: Swap current num with smallest element in arr2 that is > val
                idx = bisect.bisect_right(arr2, val)
                if idx < len(arr2):
                    new_val = arr2[idx]
                    new_dp[new_val] = min(new_dp[new_val], ops + 1)
            
            if not new_dp:
                return -1
            dp = new_dp
            
        return min(dp.values())

if __name__ == "__main__":
    solution = Solution()
    print(solution.makeArrayIncreasing([1,5,3,6,7], [1,3,2,4])) # Output: 1
